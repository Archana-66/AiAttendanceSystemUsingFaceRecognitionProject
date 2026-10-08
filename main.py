import cv2
from face_engine import FaceEngine
from attendance_logger import AttendanceLogger

def main():
    print("[INFO] Initializing Face Recognition Attendance System...")
    engine = FaceEngine()
    logger = AttendanceLogger()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open camera feed.")
        return

    print("[INFO] Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        locations, names = engine.recognize_faces(frame)

        for (top, right, bottom, left), name in zip(locations, names):
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

            # Mark attendance if valid face recognized
            if name != "Unknown":
                logger.mark_attendance(name)

            # Draw bounding box and label
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 30), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        cv2.imshow("AI Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] System stopped successfully.")

if __name__ == "__main__":
    main()
