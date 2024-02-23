import streamlit as st
from datetime import datetime


def set_footer():
   footer = f'''
            <footer style="background-color: rgb(16, 18, 22);color: rgb(69, 70, 76);text-align: right;padding: 10px;position: fixed;bottom: 0;border-top-left-radius: 15px;border-top-right-radius: 15px;z-index: 1000;">
               <p>&copy; {datetime.now().strftime('%Y')} Daniel Rodriguez. All rights reserved.</p>
            </footer>
            '''
   st.markdown(footer, unsafe_allow_html=True)

def hide_streamlit_defualt_menu_footer():
   hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
   st.markdown(hide_menu_style, unsafe_allow_html=True)
   
def get_colored_box(rgb_color:str, backgorund_tranparence:str)->str:
   color = f'''rgb({rgb_color})'''
   backgorund_color = f'''rgba({rgb_color},{backgorund_tranparence})'''
   return f'''
               "border-left: 6px solid {color};
               border-radius: 6px;
               font-size:2rem;
               text-align:right;
               padding: 10px;
               margin-top: 2px;
               background-color:{backgorund_color};"
            '''


PRODUCTS_SECTION_TEXT = '''
                "font-size:1.5rem;
                color:gray;"
            '''

SEGMENT_CARD = '''
                "background-color:rgb(29, 29, 29);
                font-size:1.2rem;
                padding-left:1rem;
                color:rgb(158, 155, 160);
                border-radius: .3rem;
                margin-top: 1rem;"
                '''

COUNTER_CARD = '''
                "font-size:1.5rem;
                color:rgb(218, 217, 219)"
                '''

MORE_DETAILS = '''
                "font-size:1rem;
                color:rgb(158, 155, 160);"
              '''




def get_link_button(rgb_color:str)->str:
   return f'''
               "text-decoration: none;
               border:solid;
               border-width:.1rem;
               border-radius: .5rem;
               padding-right: 0.5rem;
               padding-left: 0.5rem;
               font-size:1rem;
               color:rgb({rgb_color});"
            '''


def box_style()->str:
   return f'border-radius: 10px; padding: 1.5rem; background-color: blueviolet; color: whitesmoke; margin-top: 2rem;'

def start_here_link(page:str, new_tab:bool=None)->str:
   if new_tab:
      return f'<a style="text-decoration: none;" href="{page}">Start Here ➔</a>'
   else:
      return f'<a style="text-decoration: none;" href="{page}" target="_self">Start Here ➔</a>'