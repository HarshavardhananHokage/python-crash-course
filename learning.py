from dotenv import load_dotenv
import os

load_dotenv()

for key, value in os.environ.items():
    if key == "TEST_KEY":
        print(f"{key}: {value}")

value = os.getenv("TEST_KEY")
print(f"TEST_KEY: {value}")

for i in range(1,4):
    print(i)