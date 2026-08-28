function enhanceAccessibility() {
  const searchDialog = document.querySelector(".md-search[role='dialog']");
  if (searchDialog && !searchDialog.hasAttribute("aria-label")) {
    searchDialog.setAttribute("aria-label", "Search documentation");
  }

  document.querySelectorAll(".md-typeset__scrollwrap").forEach(function (region, index) {
    region.setAttribute("tabindex", "0");
    region.setAttribute("role", "region");
    region.setAttribute("aria-label", "Scrollable table " + (index + 1));
  });

  document.querySelectorAll(".md-code__nav").forEach(function (navigation, index) {
    navigation.setAttribute("aria-label", "Code block actions " + (index + 1));
  });

  document.querySelectorAll(".md-nav .md-nav[aria-label]").forEach(function (navigation, index) {
    const parentNavigation = navigation.parentElement.closest(".md-nav[aria-label]");
    const context = parentNavigation ? parentNavigation.getAttribute("aria-label") : "Documentation";
    const label = navigation.getAttribute("aria-label");
    navigation.setAttribute("aria-label", context + ": " + label + " " + (index + 1));
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(enhanceAccessibility);
} else {
  document.addEventListener("DOMContentLoaded", enhanceAccessibility);
}