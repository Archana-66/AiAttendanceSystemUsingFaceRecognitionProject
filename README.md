# AI-Powered Face Recognition Attendance System

An automated real-time attendance system built with Python, OpenCV, and Deep Learning face recognition encodings. The system captures live video via webcam, identifies registered individuals, and logs attendance into daily CSV files while preventing duplicate entries.

---

## 🌟 Key Features
- **Real-time Recognition:** Sub-second face detection and embedding comparison.
- **Automated CSV Logging:** Generates structured daily logs (`Attendance_YYYY-MM-DD.csv`).
- **Duplicate Protection:** Logs each person only once per session/day.
- **Modular Codebase:** Clean separation of detection engine, logging, and UI display logic.

---

## 📂 Project Architecture
```text
ai-face-attendance-system/
├── dataset/                # Face images for known users
├── attendance_records/     # Output CSV attendance logs
├── config.py              # Central configurations
├── face_engine.py         # Face encoding & distance evaluation
├── attendance_logger.py   # Daily CSV record manager
├── main.py                # OpenCV execution pipeline
└── requirements.txt       # Dependencies
```

---

## 🚀 Quick Setup & Execution

### 1. Prerequisites
Ensure Python 3.9+ and C++ Build Tools (required for `dlib`) are installed.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/ai-face-attendance-system.git
cd ai-face-attendance-system
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Adding Students/Users
Place clear, single-face images inside the `dataset/` directory:
- Example: `dataset/John_Doe.jpg`
- The file name automatically becomes the registered user name.

### 4. Running the Application
```bash
python main.py
```
Press **`q`** on the video window to stop the application.

---

## 📋 License
Distributed under the MIT License.
