from pathlib import Path

path = Path("pi_million_digits.txt")
content = path.read_text().rstrip()

pi_single_line = ''
for line in content.splitlines():
    pi_single_line += line

dob = input("Enter your age in ddmmyy format: ")

if dob in pi_single_line:
    print("Your birthday exists in first 1 million chars of PI")
else:
    print("Your birthday does not exists in first 1 million chars of PI")