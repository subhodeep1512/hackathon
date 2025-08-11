import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime, date
from sagemakerapp import *
#from test_model import *
#import tempfile
#import os

st.set_page_config(page_title="AI Titans", layout="wide")
st.title("AI Titans")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "My Calendar", "My Training"])
st.markdown("""
<style>
       .main > div {
           padding-top: 0rem;
           padding-bottom: 0rem;
       }
       .block-container {
           padding: 0 !important;
       }
       .stApp {
           margin-top: -3rem;
       }
       .fc {
           height: 92vh !important;
       }
</style>
""", unsafe_allow_html=True)
# Page: Home
if selection == "Home":
    st.markdown("<h1 style='text-align: center;'>🧠 Together - Home</h1>", unsafe_allow_html=True)
    st.write("We're happy to have you here. Please use the navigation menu to explore what's available.")
    # st.video("./uploads/suffering_part.mp4")
    video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if video_file is not None:
        st.video(video_file)
    # if video_file is not None:
        # filename = video_file.name
        # save_path = os.path.join(SAVE_DIR, filename)
    
        # # Save uploaded file
        # with open(save_path, "wb") as f:
        #     f.write(video_file.read())
    
        # st.success(f"✅ File saved to: {save_path}")
        # st.info("⏳ Processing the video... Please wait.")
    
        # try:
        #     result = process_video(save_path)
    
        #     if result is None or not isinstance(result, tuple) or len(result) != 3:
        #         st.error("⚠️ Processing failed. Please check your video or try again.")
        #     else:
        #         transcription, summary, emotion_suggestion = result
    
        #         st.subheader("📝 Transcription")
        #         st.write(transcription)
    
        #         st.subheader("📄 Summary")
        #         st.write(summary)
    
        #         st.subheader("💡 Emotion Suggestion")
        #         st.write(emotion_suggestion)
    
        # except Exception as e:
        #     st.error(f"An error occurred while processing the video: {str(e)}")
    
        # finally:
        #     # Optional: remove the video file to save space
        #     if os.path.exists(save_path):
        #         os.remove(save_path)
        st.write("Please wait for the model to process the result. Stay tuned...")
        if True:
        # print("-" * 60)
        # if not text:
        #     print("No transcription found. Exiting.")
        # else:
            print("\n--- Summarizing ---")
            summarized_text = summarize_text(text)
    
            print("\n--- Emotion Analysis ---")
            suggestion = analyze_state_and_suggest(text)
    
            print("\n--- Recommendation ---")
            st.write(suggestion)
    
# Page: My Calendar
elif selection == "My Calendar":
    st.markdown("<h1 style='text-align: center;'>🧠 Together - Calendar</h1>", unsafe_allow_html=True)
    selected_date = st.date_input("Pick a date", date.today())
    st.write(f"You selected: {selected_date}")
    events = [
    {
       "title": "Yoga Session",
       "start": "2025-08-03T10:00:00",
       "end": "2025-08-03T11:00:00"
    },
    {
       "title": "Doctor Appointment",
       "start": "2025-08-05T10:00:00",
       "end": "2025-08-05T11:00:00"
    }
    ]
    # Show calendar in main area (not possible in sidebar directly)
    calendar_options = {
        "initialView": "dayGridMonth",
        "editable": True,
        "selectable": True,
        "headerToolbar": {
            "left": "prev, next today",
            "center": "title",
            "right": "dayGridMonth, timeGridWeek, timeGridDay"
        }
    }
    calendar(events=events, options=calendar_options)