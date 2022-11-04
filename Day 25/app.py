import streamlit as st

st.title('st.session_state')


local_list = []


if st.button('Interaction 1'):
    local_list.append("Interaction 1")
    st.session_state["Session " + str(len(st.session_state))] = "Interaction 1"
    
if st.button('Interaction 2'):
    local_list.append("Interaction 2")
    st.session_state["Session " + str(len(st.session_state))] = "Interaction 2"
    
if st.button('Interaction 3'):
    local_list.append("Interaction 3")
    st.session_state["Session " + str(len(st.session_state))] = "Interaction 3"
    
st.subheader("Local History")
st.write(local_list)

st.subheader("Session History")
st.write(st.session_state)
    

