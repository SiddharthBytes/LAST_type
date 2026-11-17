import base64
import time
import streamlit as st

st.set_page_config(page_title="Normal_pad",page_icon="📝",
                   layout="wide")

#first i added images directly as url but that failed so we are declaring this function that allows us take 
#to take image locally
#since we were using the add image logic so many time i crwated a function out of it making it reuseable
def add_image(path):
    with open(path,"rb")as f:
        img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .line-overlay {{
            position: fixed;
            top:0;
            left:0;
            width:100vw;
            height:100vh;

            background-image:url("data:image/png;base64,{img}");
            background-repeat:no-repeat;
            background-position:center;
            background-size:100% 100%;

            pointer-events:none;
            z-index:999999;
        }}
        </style>

        <div class="line-overlay"></div>
        """,
        unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
        background-color:#0D0D0D;
}
</style>
""",unsafe_allow_html=True)
#this changes background colour
#lets change textarea color
st.markdown("""
<style>
.stTextArea textarea{
    caret-color:#FFFFFF;
    color:#FF0000FF;
}
</style>""",
unsafe_allow_html=True)
title=st.empty()
#lets also change the st.writes color
st.markdown("""
<style>
.stApp{
    color:#199157FF}
</style>""",unsafe_allow_html=True)
title.title("Notepad")


if "start_time" not in st.session_state:
    st.session_state.start_time=time.time()

@st.fragment(run_every=1)
def timer():
    if 10<(time.time()-st.session_state.start_time):
        st.toast('something is trying to occupy space',icon="⚠️")
        add_image("v2/assets/green.png")
        
    if 15<(time.time()-st.session_state.start_time):
        st.toast('something has occupied space',icon="🔴")
    if 17<(time.time()-st.session_state.start_time):
        add_image("v2/assets/glitch1.png")
    if 18<(time.time()-st.session_state.start_time):
        add_image("v2/assets/glitch2.png")
    
    if 20<(time.time()-st.session_state.start_time):
        add_image("v2/assets/crack.png")
        st.toast('something is trying to occupy space',icon="⚠️")
        st.video('v2/assets/jump.mp4',start_time=4)
        


wel_p=st.empty()
wel_p.write("Welcome to Normal pad")


st.text_area('type')


timer()
