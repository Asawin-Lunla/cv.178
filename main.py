import streamlit as st
import cv2
import numpy as np
from tempfile import NamedTemporaryFile
from yolo_engine import video_detection
import io

RATIO = 0.9
def webcam_video():
    st.title("Registerplate for webcam")
    button = st.button("Stop")
    frame_placeholder = st.empty()

    cap = cv2.VideoCapture(0)
    # Display the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_processed = video_detection(frame)

        frame_placeholder.image(frame_processed)

        # st.image(frame)  # Display video frame

        if cv2.waitKey(1) == ord('q') or button:
            break

    # Release the webcam and close OpenCV
    cap.release()
    cv2.destroyAllWindows()

def uploaded_video():
    st.title("MP4 File Uploader with OpenCV")
    button = st.button("Stop")
    frame_placeholder = st.empty()

    # Display a file uploader widget
    uploaded_file = st.file_uploader("Upload MP4 file", type=["mp4"])

    temporary_location = False

    if uploaded_file is not None:
        # Display some information about the uploaded file
        g = io.BytesIO(uploaded_file.read())
        temporary_location = "testout_simple.mp4"

        with open(temporary_location, 'wb') as out:
            out.write(g.read())  # Read bytes into file

        # Close the file
        out.close()

        cap = cv2.VideoCapture(temporary_location)
        # Display the video frame by frame
        while cap.isOpened():
            ret, frame = cap.read()

            frame_processed = video_detection(frame)

            frame_placeholder.image(frame_processed)

            # st.image(frame)  # Display video frame

            if cv2.waitKey(1) == ord('q') or button:
                break

        # Release the webcam and close OpenCV
        cap.release()
        cv2.destroyAllWindows()

def main():
    st.sidebar.title("Choose Functionality")
    choice = st.sidebar.radio("Select Functionality", ("Webcam Video", "Uploaded Video"))

    if choice == "Webcam Video":
        webcam_video()
    elif choice == "Uploaded Video":
        uploaded_video()

if __name__ == "__main__":
    main()

