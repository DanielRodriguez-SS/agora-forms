import streamlit as st
# from data.column_names import NewCellValuesFor

hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

def hide_streamlit_defualt_menu_footer():
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

# dic_style = {
#     NewCellValuesFor.IN_STOCK : get_colored_box('22, 112, 0','0.2'),
#     NewCellValuesFor.OUT_STOCK : get_colored_box('249, 0, 8','0.1'),
#     NewCellValuesFor.BACKORDER : get_colored_box('252, 148, 9','0.2'),
#     NewCellValuesFor.INCONSISTENCY : get_colored_box('242, 210, 18','0.2')
# }