import streamlit as st
import frontend.styling as css
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import database as db
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AgoraOps | Workload",
                       page_icon="🧊",layout="wide")
# css.hide_streamlit_defualt_menu_footer()


client = db.connect_to_db()
jiras_collection = client['gtm_trading']['jiras']
df = pd.DataFrame(jiras_collection.find().sort('Due Date', -1))
df = df.drop(columns=['_id'])
df['Due Date'] = pd.to_datetime(df['Due Date'])
# df['Month'] = df['Due Date'].dt.month
df['Month'] = df['Due Date'].dt.strftime('%B')
df['Year'] = df['Due Date'].dt.year
df['Week'] = df['Due Date'].dt.day // 7+1

current_date = datetime.now()
future_dates_df = df[df['Due Date'] >= current_date]


grouped = future_dates_df.groupby(['Year','Month','Week'])

# df['Due Date'] = df['Due Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
# for jira in jiras_collection.find():
#     st.write(jira)
st.dataframe(df,hide_index=True,use_container_width=True)
graph_dict = {}
# graph_dict['x'] = []
# graph_dict['y'] = []
for (year,month,week), group in grouped:
    st.write(f'wk {week} / {month}, {year}')
    group = group.drop(columns=['Month', 'Year','Week'])
    # group['Week Of Month'] = group['Due Date'].dt.day // 7+1
    st.write(len(group))
    st.dataframe(group,hide_index=True,use_container_width=True)
    graph_dict[f'{year} wk {week} / {month}'] = len(group)
    # graph_dict['x'].append(f'wk {week} / {month}, {year}')
    # graph_dict['y'].append(len(group))
st.write(graph_dict)
st.bar_chart(graph_dict)