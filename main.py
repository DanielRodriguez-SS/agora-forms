import streamlit as st

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
        st.Page("console_search.py", title="🖥️ Console Search"),
        st.Page("rewards_pricing.py", title="💲 Rewards Pricing")
    ]
}

pg= st.navigation(pages)
pg.run()