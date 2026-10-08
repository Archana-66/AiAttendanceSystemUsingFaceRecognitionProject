import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
ATTENDANCE_DIR = os.path.join(BASE_DIR, "attendance_records")

# Matching threshold (lower means stricter recognition)
MATCH_THRESHOLD = 0.5

# Frame scaling factor for faster processing (0.25 = 1/4 size)
FRAME_RESIZE = 0.25
