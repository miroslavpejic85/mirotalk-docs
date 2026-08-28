function initializeExternalPreviews() {
  document.querySelectorAll("[data-embed-src]:not([data-embed-ready])").forEach((preview) => {
    const embedButton = preview.querySelector("[data-embed-button]");
    let embedUrl;

    try {
      embedUrl = new URL(preview.dataset.embedSrc);
    } catch {
      return;
    }

    const allowedHosts = ["www.youtube-nocookie.com", "www.canva.com"];
    if (!embedButton || !allowedHosts.includes(embedUrl.hostname)) {
      return;
    }

    preview.dataset.embedReady = "true";
    embedButton.addEventListener(
      "click",
      () => {
        const iframe = document.createElement("iframe");
        iframe.className = preview.dataset.embedClass || "external-embed-frame";
        iframe.src = embedUrl.toString();
        iframe.title = preview.dataset.embedTitle || "Embedded content";
        iframe.allow = preview.dataset.embedAllow || "fullscreen";
        iframe.referrerPolicy = "strict-origin-when-cross-origin";
        iframe.allowFullscreen = true;

        preview.replaceChildren(iframe);
        iframe.focus();
      },
      { once: true },
    );
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(initializeExternalPreviews);
} else if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeExternalPreviews, { once: true });
} else {
  initializeExternalPreviews();
}
