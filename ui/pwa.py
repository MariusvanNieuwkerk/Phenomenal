"""Favicon and PWA home-screen icon tags."""

import os

import streamlit as st

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_32 = os.path.join(APP_DIR, "static", "briefly-icon-32.png")

_PWA_HEAD_SCRIPT = """
<script>
(function () {
  if (window.__brieflyIconsApplied) return;
  window.__brieflyIconsApplied = true;
  var head = document.head;
  function addLink(rel, href, sizes) {
    if (document.querySelector('link[rel="' + rel + '"]')) return;
    var el = document.createElement('link');
    el.rel = rel;
    el.href = href;
    if (sizes) el.sizes = sizes;
    head.appendChild(el);
  }
  function addMeta(name, content) {
    if (document.querySelector('meta[name="' + name + '"]')) return;
    var el = document.createElement('meta');
    el.name = name;
    el.content = content;
    head.appendChild(el);
  }
  addLink('manifest', '/app/static/manifest.json');
  addLink('apple-touch-icon', '/app/static/briefly-icon-180.png', '180x180');
  addMeta('apple-mobile-web-app-title', 'Briefly');
  addMeta('apple-mobile-web-app-capable', 'yes');
  addMeta('mobile-web-app-capable', 'yes');
  addMeta('theme-color', '#1A365D');
})();
</script>
"""


def page_icon() -> str:
    """Tab favicon URL (requires server.enableStaticServing)."""
    if os.path.isfile(ICON_32):
        return "/app/static/briefly-icon-32.png"
    return "✈️"


def inject_pwa_head_tags() -> None:
    """Install manifest + apple-touch-icon in the main document head."""
    st.html(_PWA_HEAD_SCRIPT, unsafe_allow_javascript=True)
