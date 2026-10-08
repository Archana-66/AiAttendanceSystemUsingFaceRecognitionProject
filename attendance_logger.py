import os
import csv
from datetime import datetime
import config

class AttendanceLogger:
    def __init__(self):
        os.makedirs(config.ATTENDANCE_DIR, exist_ok=True)
        today_str = datetime.now().strftime("%Y-%m-%d")
        self.file_path = os.path.join(config.ATTENDANCE_DIR, f"Attendance_{today_str}.csv")
        self.logged_names = set()
        self._initialize_csv()

    def _initialize_csv(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Date", "Time", "Status"])
        else:
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if row:
                        self.logged_names.add(row[0])

    def mark_attendance(self, name: str) -> bool:
        if name in self.logged_names or name == "Unknown":
            return False

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date_str, time_str, "Present"])

        self.logged_names.add(name)
        print(f"[INFO] Attendance logged for: {name} at {time_str}")
        return True
