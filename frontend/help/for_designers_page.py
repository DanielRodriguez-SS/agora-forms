import streamlit as st

def display_help():
    with st.expander("Need Help?"):
        col1, col2 = st.columns([1,1],gap="medium")
        with col1:
            st.markdown("""<div style="background-color:rgb(239,48,57);height:1.5rem;width:1.5rem;border-radius:50%;text-align:center;margin-bottom:.5rem;margin-top:.5rem;">1</div>""", unsafe_allow_html=True)
    
            st.markdown('''
                        :orange[Product Name:] Type the name of the product for images you want to create links for.
                        ''')
            st.divider()
            st.markdown('''
                        :orange[Category:] This one needs to match with the category on the :blue[*repo*] dir where you will be uploading images.\n
                        * For AGORA :blue[repo]: /content/dam/tcom/lego/2022/accessories/products/:red[category]/
                        * For Non-AGORA :blue[repo]: /content/dam/tcom/devices/general/hardware/:red[category]/
                        ''')
            st.divider()
            st.markdown('''
                        :orange[Sub-Category:] This should align with a general name for the product excluding its color.\n
                        * For AGORA :blue[repo]: /content/dam/tcom/lego/2022/accessories/products/category/:red[sub-category]/
                        * For Non-AGORA :blue[repo]: /content/dam/tcom/devices/general/hardware/category/:red[sub-category]/
                        ''')
            st.divider()
            st.markdown('''
                        :orange[Color:] This should align with the product's color.\n
                        * For AGORA :blue[repo]: /content/dam/tcom/lego/2022/accessories/products/category/sub-category/:red[color]/
                        * For Non-AGORA :blue[repo]: /content/dam/tcom/devices/general/hardware/category/sub-category/:red[color]/
                        ''')
            st.divider()
            st.markdown('''
                        :orange[Hexcode:] Type the color of product on Hexadicimal and hit ENTER
                        ''')
    
        with col2:
            st.markdown("""<div style="background-color:rgb(239,48,57);height:1.5rem;width:1.5rem;border-radius:50%;text-align:center;margin-bottom:.5rem;margin-top:.5rem;">2</div>""", unsafe_allow_html=True)
            st.markdown('''
                        :orange[Select all images:] Once "Browse files" appear, click on it and select all images you have for that product, for AGORA and Non-AGORA :blue[repo] all combined.
                ''')
            st.image('select_files.png')
            st.divider()
            st.markdown('''
                        :orange[Save:] Once all files are uploaded clicl on Save and repeat the process from step 1 to add as many products you need.
                    ''')
            st.divider()
            st.markdown('''
                        :orange[Export .xlsx:] When you have saved all products, next click on "Export .xlsx".
                    ''')
