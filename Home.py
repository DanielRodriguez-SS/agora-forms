# Run this page with command "streamlit run Home.py"
import streamlit as st
import frontend.styling as css
st.set_page_config(page_title="Forms | Home",
                       page_icon="🧊")
css.hide_streamlit_defualt_menu_footer()
st.info("Sit tight, this page will be live soon.",icon='😀')