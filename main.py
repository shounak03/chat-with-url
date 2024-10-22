import streamlit as st
from scrape import (scrape_url,clean_body,extract_body,split_content)



st.title("Blog Summarizer")
st.write("This is a simple blog summarizer that uses the Hugging Face Transformers library to summarize")
url = st.text_input("URL")

if st.button("Scrape url"):
    st.write("Scrapping the website")

    res = scrape_url(url)
    body_content = extract_body(res)
    clean_content = clean_body(body_content)
    # split_content = split_content(clean_conetent)

    st.session_state.dom_content = clean_content

    with st.expander("View Dom content"):
        st.text_area("DOM CONTENT",clean_content,height=300)