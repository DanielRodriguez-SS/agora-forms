# Run this page with command "streamlit run Home.py"
import streamlit as st
import reqease

#reqease.Get("https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MOBILE/NEW").to_file('mobile.json')


# st.set_page_config(page_title="AgoraOps Hub | Home",
#                        page_icon="🎛️",layout="wide")




pages = {
    "New Requests": [
        st.Page("req_promos.py", title="🔥 Promotions"),
        st.Page("req_devices.py", title="📱 Devices"),
    ],
    "Monitor": [
        st.Page("live_promos.py", title="🔴 Promos Live Now"),
        st.Page("rewards_search.py", title="🏆 Rewards Search"),
    ],
    "Workload": [
        st.Page("workload_info.py", title="📄 Details")
    ],
    "Tools": [
        st.Page("linkcraft.py", title="🛠️ LinkCraft Pro"),
        st.Page("console_search.py", title="🖥️ Console Search")
    ]
}

pg= st.navigation(pages)
pg.run()


# st.markdown('# Welcome to AgoraOps Hub! 👋')
# st.markdown('''Welcome to our central hub, your go-to channel for seamless navigation through various
#                functionalities. Here, you can effortlessly request promotions, explore new device builds,
#                check our workload forecast, and much more. Streamline your tasks and access a world of possibilities
#                at your fingertips. Empower your experience, all in one place.''')

# col11, col12 = st.columns(2)
# with col11:
#     st.markdown(f'''<div style="{css.box_style()}">
#                         <h5>Workload Details</h5>
#                         Discover upcoming tasks and projects on our Workload Forecast page. Stay ahead, plan efficiently,
#                         and make informed decisions for successful project management.
#                     </div>
#                 {css.start_here_link('Workload_Details')}''',unsafe_allow_html=True)

# with col12:
#     st.markdown(f'''<div style="{css.box_style()}">
#                         <h5>Promotions</h5>
#                         Streamline promotion requests effortlessly on our dedicated page. Provide all necessary details upfront,
#                         ensuring a smooth process without the need for back-and-forth communication. Empower our team to efficiently
#                         gather the information needed to build successful promotions.
#                     </div>
#                 {css.start_here_link('Promotions')}''',unsafe_allow_html=True)

# col21, col22 = st.columns(2)

# with col21:
#     st.markdown(f'''<div style="{css.box_style()}">
#                         <h5>Devices</h5>
#                         Simplify device requests on our dedicated page. Efficiently gather all necessary information upfront,
#                         eliminating the need for back-and-forth communication. Empower our team to seamlessly build new devices
#                         without delays, ensuring a smooth and effective process for all stakeholders.
#                     </div>
#                 {css.start_here_link('https://swimplify.co/projects/telstra/telstra-promos-form/new-device.html',new_tab=True)}''',unsafe_allow_html=True)

# with col22:
#     st.markdown(f'''<div style="{css.box_style()}">
#                         <h5>LinkCraft Pro</h5>
#                         Explore our automated tool designed for effortless link creation and image resizing. Perfect for designers
#                         preparing products to go live, this tool streamlines the process, allowing you to easily generate various
#                         types of links for your images. Enhance your workflow and ensure optimal presentation with our user-friendly
#                         solution.
#                     </div>
#                 {css.start_here_link('LinkCraft_Pro')}''',unsafe_allow_html=True)
    
