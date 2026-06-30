import streamlit as st

from search.index import search


def render_home_search(navigate_fn):
    _, search_col, _ = st.columns([1, 2, 1])
    with search_col:
        st.markdown('<p class="briefly-search-label">SEARCH</p>', unsafe_allow_html=True)
        query = st.text_input(
            "Search",
            placeholder="MTOW · fuel · EGLC · smoke · hydraulics…",
            key="home_search",
            label_visibility="collapsed",
        )

    if not query.strip():
        return

    results = search(query)
    if not results:
        with search_col:
            st.info("No results — try another term.")
        return

    for i, result in enumerate(results):
        label = result["title"]
        if result["subtitle"]:
            label = f"{result['title']}  ·  {result['subtitle']}"
        slug = result["title"].replace(" ", "_")[:40]
        with search_col:
            if st.button(label, use_container_width=True, type="primary", key=f"search_hit_{i}_{slug}"):
                navigate_fn(
                    result["section"],
                    system=result.get("system"),
                    airport=result.get("airport"),
                    focus=result.get("focus"),
                )
                st.rerun()
