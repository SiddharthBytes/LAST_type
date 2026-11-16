import time
import streamlit as st

st.set_page_config(page_title="Normal_pad",page_icon="📝",
                   layout="wide")
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
    if 10<(time.time()-st.session_state.start_time):
        st.toast('something is trying to occupy space',icon="⚠️")
        st.markdown("""
        <style>

        .screen-crack {

            position:fixed;
            inset:0;

            width:100%;
            height:100%;

            background-image:url("https://images.rawpixel.com/dark_image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTAyL3Jhd3BpeGVsX29mZmljZV80MF9taW5pbWFsX292ZXJsYXlfYmFja2dyb3VuZF90ZXh0dXJlX29mX3JldHJvX19hMzA0MjJmNi1mNDdmLTQxZGYtYWIyZS04MjJkNjVhZjg4NjgucG5n.png");
            background-size:cover;

            background-position:center;
            background-repeat:no-repeat;

            pointer-events:none;

            z-index:999999;
        }
        </style>

        <div class="screen-crack"> </div>
        """, unsafe_allow_html=True)
        
    if 20<(time.time()-st.session_state.start_time):
        st.toast('something has occupied space',icon="🔴")
    if 30<(time.time()-st.session_state.start_time):
        pass

        


wel_p=st.empty()
wel_p.write("Welcome to Normal pad")


st.text_area('type')


#why we need to add ; this after each line 
#this piece of code is for adding image on top the streamlit ui and layout
#for those who dont know in streamlit we can use html and css from st.markdown
#and there is also a st.html it can run html code but i dont use it because i can use whatever i want since i created it
timer()






