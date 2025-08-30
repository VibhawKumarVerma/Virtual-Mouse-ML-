# 🖱️ Virtual Mouse

A **Virtual Mouse** system that allows users to control the mouse cursor using hand gestures, leveraging computer vision techniques. Built with Python and OpenCV, this project offers a hands-free alternative for interacting with your computer.

---

## 🚀 Features

- Move mouse cursor using hand gestures  
- Perform click actions (left-click, right-click)  
- Scroll vertically with gestures  
- Gesture-based control using webcam feed  
- Real-time hand tracking and gesture recognition  

---

## 🛠️ Technologies Used

- Python 3  
- OpenCV  
- MediaPipe (for hand tracking)  
- PyAutoGUI (for controlling the mouse)

---

## 📸 Demo

> _Add a GIF or short video showing how the virtual mouse works in real time._

---

## 📦 Installation

### Requirements

- Python 3.7+  
- Webcam  
- pip (Python package installer)
- pip install opencv-python mediapipe pyautogui

### Clone the Repository

```bash
git clone https://https://github.com/VibhawKumarVerma/Virtual-Mouse-ML-.git
cd VirtualMouse
```

## 🧠 How It Works

- Webcam captures real-time video.

- MediaPipe detects and tracks hand landmarks.

- Specific gestures (e.g., index finger up) are interpreted as commands.

- PyAutoGUI translates gesture commands into mouse actions.

## ▶️ Usage

Run the main script:
```bash
python VirtualMouseProject.py
```

## 📁 File Structure
```bash
Virtual Mouse/
├── __pycache__
├── Hand
├── package.json
└── README.md
```
