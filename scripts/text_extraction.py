import time
from tika import parser

def extract_text(file_path):
    for _ in range(3):  # Retry 3 times
        try:
            raw = parser.from_file(file_path)
            return raw['content']
        except Exception as e:
            print(f"Warning: {e}")
            time.sleep(1)  # Wait for 1 second before retrying
    raise Exception("Failed to parse file after 3 retries")
