import os
import cv2
import face_recognition
import numpy as np
import config

class FaceEngine:
    def __init__(self):
        self.known_encodings = []
        self.known_names = []
        self.load_known_faces()

    def load_known_faces(self):
        if not os.path.exists(config.DATASET_DIR):
            os.makedirs(config.DATASET_DIR)
            print(f"[WARNING] Created empty dataset directory at {config.DATASET_DIR}")

        valid_extensions = ('.jpg', '.jpeg', '.png')
        for file in os.listdir(config.DATASET_DIR):
            if file.lower().endswith(valid_extensions):
                path = os.path.join(config.DATASET_DIR, file)
                name = os.path.splitext(file)[0].replace("_", " ").title()

                image = face_recognition.load_image_file(path)
                encodings = face_recognition.face_encodings(image)

                if len(encodings) > 0:
                    self.known_encodings.append(encodings[0])
                    self.known_names.append(name)
                    print(f"[LOADED] Face encoding for: {name}")
                else:
                    print(f"[WARNING] No face found in {file}")

    def recognize_faces(self, frame):
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=config.FRAME_RESIZE, fy=config.FRAME_RESIZE)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for encoding in face_encodings:
            if not self.known_encodings:
                face_names.append("Unknown")
                continue

            distances = face_recognition.face_distance(self.known_encodings, encoding)
            best_match_index = np.argmin(distances)

            if distances[best_match_index] <= config.MATCH_THRESHOLD:
                name = self.known_names[best_match_index]
            else:
                name = "Unknown"

            face_names.append(name)

        # Scale back face locations to original frame size
        scaled_locations = []
        scale_factor = int(1 / config.FRAME_RESIZE)
        for (top, right, bottom, left) in face_locations:
            scaled_locations.append((
                top * scale_factor,
                right * scale_factor,
                bottom * scale_factor,
                left * scale_factor
            ))

        return scaled_locations, face_names
