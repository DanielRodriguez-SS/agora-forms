import streamlit as st
import frontend.styling as css
import database as db
import pandas as pd
from datetime import datetime, time
import calendar
import altair as alt
import copy
#'''
#Dynamic Tabs Creation Ref:
#https://docs.kanaries.net/topics/Streamlit/streamlit-tabs
#'''
st.set_page_config(page_title="AgoraOps Hub | Workload Details",
                       page_icon="🎛️",layout="wide")
css.hide_streamlit_defualt_menu_footer()

def plural_word(len_items:int,word:str) -> str:
    if len_items > 1:
        return f'{word}s'
    else:
        return word

with st.sidebar:
    st.markdown('# 📝 JIRA Tickets Entry')
    data = {}
    data['Ticket #'] = st.text_input('Ticket #')
    data['Summary'] = st.text_input('Summary')
    is_double_impact = st.checkbox('This Ticket will have double impact')
    data['Epic'] = st.text_input('Epic')
    data['Due Date'] = datetime.combine(st.date_input('Due Date'),time(0,0))
    data['Notes'] = st.text_input('Notes')
    magic_pass = st.text_input(label='Magic Pass',type='password')
    save = st.button('Save')
    
    
    if save:
        if data['Ticket #'] or data['Summary'] or data['Epic'] or magic_pass:
            if magic_pass == f'AgoraOps{datetime.now().strftime("%d%m%y")}':
                client = db.connect_to_db()
                is_exting_jira = db.find_jira(client,data={'Ticket #':data['Ticket #']})
                if not is_exting_jira:
                    db.insert_jira(client,data)
                    if is_double_impact:
                        #data2 = data
                        data2 = copy.deepcopy(data)
                        data2.pop('_id', None)
                        data2['Ticket #'] = f"{data['Ticket #']}_+"
                        db.insert_jira(client,data2)
                    st.toast(f'{data["Ticket #"]} JIRA Added!', icon='👍')
                else:
                    st.toast('JIRA Already Exists on Database', icon='🚫')
            else:
                st.toast('Incorrect Magic Pass!', icon='🚫')
        else:
            st.toast('JIRA Details are missing!', icon='🚫')
    
    st.markdown('# 🧹 Clean Database')

    target_ticket = st.text_input('Ticket # to remove')
    delete = st.button('Delete')
    if delete:
        if target_ticket and magic_pass:
            if magic_pass == f'AgoraOps{datetime.now().strftime("%d%m%y")}':
                client = db.connect_to_db()
                is_exting_jira_todelete = db.find_jira(client,data={'Ticket #':target_ticket})
                if is_exting_jira_todelete:
                    db.delete_jira(client,{'Ticket #':target_ticket})
                    st.toast(f'{target_ticket} JIRA Deleted!', icon='👍')
                else:
                    st.toast('JIRA Does Not Exists on Database', icon='🚫')
            else:
                st.toast('Incorrect Magic Pass!', icon='🚫')
        else:
            st.toast('Ticket or Magic Pass are missing!', icon='🚫')



# Get client from DB connection
client = db.connect_to_db()
# Get all documents on JIRAs collection from the gtt_trading database
jiras_collection = client['gtm_trading']['jiras']
# Set a dataframe with results from the cursor and sorted in order by Due Date
df = pd.DataFrame(jiras_collection.find().sort('Due Date', -1))
# Drop the _id column
df = df.drop(columns=['_id'])
# From str to datetime format on "Due Date" Column
df['Due Date'] = pd.to_datetime(df['Due Date'])
# Add 3 columns to df from "Due Date" get the Month, Year and Week number of the month
df['Month'] = df['Due Date'].dt.month
df['Year'] = df['Due Date'].dt.year
df['Week'] = df['Due Date'].dt.day // 7+1
# Save the current date
current_date = datetime.now()
# Get a new dataframe with only Jiras which Due Date is in future and sort them ascending
future_dates_df = df[df['Due Date'] >= current_date].sort_values(by='Due Date', ascending=True)
# Gruped the new filtered dataframe by 'Year' 'Month' and 'Week'
grouped = future_dates_df.groupby(['Year','Month','Week'])
future_dates_df = future_dates_df.drop(columns=['Month', 'Year','Week'])

graph_dict = {}
grouped_dfs = {}

for (year,month,week), group in grouped:
    group = group.drop(columns=['Month', 'Year','Week'])
    grouped_dfs[f'{calendar.month_abbr[month]} {year} wk{week}'] = group
    graph_dict[f'{calendar.month_abbr[month]} {year} wk{week}'] = len(group)

st.markdown(f'# 📊 Task Pipeline Forecast')
st.markdown(f'{len(future_dates_df)} {plural_word(len(future_dates_df),"Ticket")}')

# Convert data dictionary to a DataFrame
graph_df = pd.DataFrame(list(graph_dict.items()), columns=['Week', 'Tickets'])
graph_df['Color'] = graph_df['Tickets'].apply(lambda x: 'green' if x < 4 else ('orange' if x < 8 else 'red'))
#st.dataframe(graph_df)
chart = alt.Chart(graph_df).mark_bar(color='#ffaa0088').encode(x=alt.X('Week',sort=None,title='Week'),y='Tickets')
chart = alt.Chart(graph_df).mark_bar().encode(
    x=alt.X('Week',sort=None,title='Week'),
    y='Tickets',
    color=alt.Color('Color', scale=alt.Scale(domain=['green', 'orange', 'red'], range=['#4caf50', '#ffa726','#f44336']), legend=None)
)
st.altair_chart(chart, use_container_width=True)

st.markdown('# 🗓️ Weekly Task Breakdown')
tab_list = list(grouped_dfs)
tabs = st.tabs(tab_list)

for df,tab in zip(grouped_dfs, tabs):
    with tab:
        st.write(f'{len(grouped_dfs[df])} {plural_word(len(grouped_dfs[df]),"Ticket")}')
        st.dataframe(grouped_dfs[df],hide_index=True,use_container_width=True)

st.markdown(f'# 📋 Work Queue Catalog')
st.dataframe(future_dates_df, hide_index=True, use_container_width=True)