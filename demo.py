import streamlit as st
import pandas as pd

login_cred = pd.read_csv('C:/Users/swssa/Codes/v2/login_cred.csv')
client_ids = list(login_cred['user_id'])

st.set_page_config(layout="wide")

st.title('Algo Guys')

st.write("""
where TEAMWORK makes the DREAM work
""")

st.sidebar.header('Client ID')

client_id = st.sidebar.selectbox('Choose ID',
                client_ids)

# Multiselect test
xx = (client_ids)
selected_id = st.sidebar.multiselect('Multiple IDs', xx, xx)

# Input csv dashboard files
try:
    sut_one = pd.read_csv('C:/Users/swssa/Codes/v2/dashboard files/' + client_id[:2].lower() + '_sut_one.csv')
except:
    pass
try:
    sut_two = pd.read_csv('C:/Users/swssa/Codes/v2/dashboard files/' + client_id[:2].lower() + '_sut_two.csv')
except:
    pass
try:
    b120_one = pd.read_csv('C:/Users/swssa/Codes/v2/dashboard files/' + client_id[:2].lower() + '_b120_one.csv')
except:
    pass
try:
    b120_two = pd.read_csv('C:/Users/swssa/Codes/v2/dashboard files/' + client_id[:2].lower() + '_b120_two.csv')
except:
    pass


st.write("""
## Banknifty
""")

st.write("""
* SUT - 1
""")

try:
    st.write(sut_one)
except:
    pass

st.write("""
* SUT - 2
""")

try:
    st.write(sut_two)
except:
    pass

st.write("""
* B120 - 1
""")

try:
    st.write(b120_one)
except:
    pass

st.write("""
* B120 - 2
""")

try:
    st.write(b120_two)
except:
    pass
