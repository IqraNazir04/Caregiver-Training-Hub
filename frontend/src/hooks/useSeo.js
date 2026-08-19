import { useEffect } from "react";

const SITE_NAME = "Caregiver Training Hub";

function setMeta(attr, key, content) {
  let el = document.head.querySelector(`meta[${attr}="${key}"]`);
  if (!el) {
    el = document.createElement("meta");
    el.setAttribute(attr, key);
    document.head.appendChild(el);
  }
  el.setAttribute("content", content);
}

function setLink(rel, href) {
  let el = document.head.querySelector(`link[rel="${rel}"]`);
  if (!el) {
    el = document.createElement("link");
    el.setAttribute("rel", rel);
    document.head.appendChild(el);
  }
  el.setAttribute("href", href);
}

/**
 * Sets the document title, meta description, robots directive, canonical
 * link, and Open Graph/Twitter tags for the current page. Call once per
 * page component. Authenticated/personalized pages should pass noindex:true
 * so they're excluded from search results.
 */
export function useSeo({ title, description, noindex = false, jsonLd } = {}) {
  useEffect(() => {
    document.title = title ? `${title} — ${SITE_NAME}` : SITE_NAME;

    if (description) {
      setMeta("name", "description", description);
      setMeta("property", "og:description", description);
      setMeta("name", "twitter:description", description);
    }

    setMeta("name", "robots", noindex ? "noindex, nofollow" : "index, follow");
    setMeta("property", "og:title", title ? `${title} — ${SITE_NAME}` : SITE_NAME);
    setMeta("name", "twitter:title", title ? `${title} — ${SITE_NAME}` : SITE_NAME);
    setLink("canonical", window.location.origin + window.location.pathname);
    setMeta("property", "og:url", window.location.origin + window.location.pathname);

    let script = null;
    if (jsonLd) {
      script = document.createElement("script");
      script.type = "application/ld+json";
      script.textContent = JSON.stringify(jsonLd);
      document.head.appendChild(script);
    }

    return () => {
      if (script) document.head.removeChild(script);
    };
  }, [title, description, noindex, jsonLd]);
}
