📌 Face Mesh Detection using MediaPipe
🧠 Project Overview

This project uses MediaPipe to perform Face Mesh Detection, which identifies and tracks facial landmarks in real-time from a video or webcam.

🎯 Features
Detect multiple faces in real-time
Draw face mesh (facial landmarks)
Count number of detected faces
Display FPS (Frames Per Second)
Works with both video files and webcam
🛠️ Technologies Used
Python
OpenCV
MediaPipe
📂 How to Run
1️⃣ Install dependencies:
pip install opencv-python mediapipe
2️⃣ Run the project:
python face_mesh.py
📹 Input Source

You can change the input source here:

cap = cv2.VideoCapture("WIN_20260329_15_33_09_Pro.mp4")

Or use your webcam:

cap = cv2.VideoCapture(0)
🧩 Code Explanation
faceMeshDetector → Class responsible for face mesh detection
findMeshFaces → Returns:
Processed frame
Landmark positions for each detected face
The program also calculates and displays FPS
📸 Output
Face mesh drawn on the video
Number of detected faces
FPS displayed on screen
🚀 Future Improvements
Add face recognition
Save landmark data
Integrate with AR applications
Facial expression analysis
👨‍💻 Author

Ahmed Hany Sallam

⭐ Notes

Make sure not to upload:

mp_env/
__pycache__/
Large video files

Use a .gitignore file to keep your repository clean and professional.
