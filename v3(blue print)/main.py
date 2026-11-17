import base64
import time
import streamlit as st

st.set_page_config(page_title="Normal_pad",page_icon="📝",
                   layout="wide")


def getting_base64(path):
    with open(path,"rb")as f:
        return base64.b64encode(f.read()).decode()

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
    color:##199157FF}
</style>""",unsafe_allow_html=True)
title.title("Notepad")


if "start_time" not in st.session_state:
    st.session_state.start_time=time.time()

@st.fragment(run_every=1)
def timer():
    if 10==(time.time()-st.session_state.start_time):
        st.toast('something is trying to occupy space',icon="⚠️")
        img1=getting_base64("v2/assets/green_line.png") 
        st.markdown(f"""
        <style>

        .screen-crack {{

            position:fixed;
            inset:0;

            width:100%;
            height:100%;

            background-url("data:image/png;base64,{img1}");
            background-size:cover;

            background-position:center;
            background-repeat:no-repeat;

            pointer-events:none;

            z-index:999999;
        }}
        </style>

        <div class="screen-crack"> </div>
        """, unsafe_allow_html=True)
        
    if 20==(time.time()-st.session_state.start_time):
        st.toast('something has occupied space',icon="🔴")
    if 30==(time.time()-st.session_state.start_time):
        pass

        


wel_p=st.empty()
wel_p.write("Welcome to Normal pad")


st.text_area('type')


#why we need to add ; this after each line 
#this piece of code is for adding image on top the streamlit ui and layout
#for those who dont know in streamlit we can use html and css from st.markdown
#and there is also a st.html it can run html code but i dont use it because i can use whatever i want since i created it
timer()






