(function () {
  "use strict";

  const PRODUCT_PATHS = new Set(["sfu", "p2p", "c2c", "bro", "cme", "web", "admin", "ultimate"]);

  function pageContext() {
    const segments = window.location.pathname.split("/").filter(Boolean);
    const productSegment = segments.find(function (segment) {
      return segment.startsWith("mirotalk-");
    });
    const product = productSegment ? productSegment.replace("mirotalk-", "") : undefined;
    const journey = ["cloud", "self-host", "build", "commercial", "enterprise"].find(function (name) {
      return segments.includes(name);
    });

    return {
      page_path: window.location.pathname,
      product: PRODUCT_PATHS.has(product) ? product : undefined,
      journey: journey,
    };
  }

  function classifyLink(link) {
    const url = new URL(link.href, window.location.href);
    const sourcePath = window.location.pathname;
    const apiPage = sourcePath.endsWith("/api/");
    const selfHostPage = sourcePath.startsWith("/self-host/") || sourcePath.endsWith("/self-hosting/");

    if (url.hostname === "webrtc.mirotalk.com") {
      return {
        event_name: apiPage ? "developer_api_to_cloud" : selfHostPage ? "cta_cloud_from_self_host" : "cta_cloud_start",
        destination_type: "cloud",
      };
    }
    if (url.pathname.startsWith("/license/")) {
      return {
        event_name: apiPage ? "developer_api_to_license" : "cta_commercial_license",
        destination_type: "licensing",
      };
    }
    if (url.protocol === "mailto:") {
      return { event_name: "cta_enterprise_contact", destination_type: "email" };
    }
    if (url.hostname === "github.com") {
      return { event_name: "cta_github_view", destination_type: "source" };
    }
    if (url.hostname === "codecanyon.net" || url.hostname === "buy.stripe.com") {
      return { event_name: "cta_codecanyon", destination_type: "purchase" };
    }
    if (url.hostname.endsWith(".mirotalk.com") && url.hostname !== "docs.mirotalk.com") {
      return { event_name: "cta_demo_open", destination_type: "demo" };
    }
    return null;
  }

  function emitAnalyticsEvent(link, classification) {
    const context = pageContext();
    const detail = {
      event_name: classification.event_name,
      page_path: context.page_path,
      destination_type: classification.destination_type,
      cta_location: link.closest("header, main, footer")?.tagName.toLowerCase() || "page",
    };

    if (context.product) detail.product = context.product;
    if (context.journey) detail.journey = context.journey;

    window.dispatchEvent(new CustomEvent("mirotalk:analytics", { detail: detail }));
  }

  document.addEventListener("click", function (event) {
    const link = event.target.closest("a[href]");
    if (!link) return;

    const classification = classifyLink(link);
    if (classification) emitAnalyticsEvent(link, classification);
  });
})();