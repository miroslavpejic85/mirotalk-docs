#!/usr/bin/env node

"use strict";

const fs = require("fs");
const vm = require("vm");

const source = fs.readFileSync("docs/javascripts/analytics-events.js", "utf8");
let clickHandler;
const emitted = [];

const context = {
  URL,
  CustomEvent: class CustomEvent {
    constructor(type, options) {
      this.type = type;
      this.detail = options.detail;
    }
  },
  window: {
    location: { href: "https://docs.mirotalk.com/", pathname: "/" },
    dispatchEvent(event) {
      emitted.push(event);
    },
  },
  document: {
    addEventListener(type, handler) {
      if (type === "click") clickHandler = handler;
    },
  },
};

vm.runInNewContext(source, context);

function classify(pathname, href) {
  emitted.length = 0;
  context.window.location.pathname = pathname;
  context.window.location.href = `https://docs.mirotalk.com${pathname}`;
  const link = {
    href: new URL(href, context.window.location.href).href,
    closest() {
      return { tagName: "MAIN" };
    },
  };
  clickHandler({ target: { closest: () => link } });
  return emitted[0]?.detail;
}

const cases = [
  ["/", "https://webrtc.mirotalk.com", "cta_cloud_start", "cloud"],
  ["/self-host/", "https://webrtc.mirotalk.com", "cta_cloud_from_self_host", "cloud"],
  ["/mirotalk-sfu/api/", "/license/", "developer_api_to_license", "licensing"],
  ["/mirotalk-p2p/api/", "https://webrtc.mirotalk.com", "developer_api_to_cloud", "cloud"],
  ["/", "/license/", "cta_commercial_license", "licensing"],
  ["/story/", "https://github.com/miroslavpejic85", "cta_github_view", "source"],
  ["/mirotalk-ultimate/", "https://buy.stripe.com/example", "cta_codecanyon", "purchase"],
  ["/mirotalk-sfu/", "https://sfu.mirotalk.com", "cta_demo_open", "demo"],
  ["/enterprise/", "mailto:miroslav.pejic.85@gmail.com", "cta_enterprise_contact", "email"],
];

const failures = [];
for (const [pathname, href, eventName, destinationType] of cases) {
  const detail = classify(pathname, href);
  if (!detail || detail.event_name !== eventName || detail.destination_type !== destinationType) {
    failures.push(`${pathname} -> ${href}: expected ${eventName}/${destinationType}`);
    continue;
  }
  const allowed = new Set([
    "event_name",
    "page_path",
    "product",
    "journey",
    "cta_location",
    "destination_type",
  ]);
  const unexpected = Object.keys(detail).filter((key) => !allowed.has(key));
  if (unexpected.length) failures.push(`${eventName}: unexpected fields ${unexpected.join(", ")}`);
}

if (failures.length) {
  console.error("Analytics event validation failed:");
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`Validated ${cases.length} analytics event classifications and approved payload fields.`);