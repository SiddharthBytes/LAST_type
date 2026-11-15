import time
import streamlit as st
if "start_time" not in st.session_state:
    st.session_state.start_time=time.time()

st.text_area('type')
@st.fragment(run_every=1)
def timer(count):

    if count<(time.time()-st.session_state.start_time):
        st.text('time is up')
        st.success("_")
timer(20)





