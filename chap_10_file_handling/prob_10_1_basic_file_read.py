from pathlib import Path

path = Path("pi_30.txt")
content = path.read_text().rstrip()
print(content)
print()

count = 0
for line in content.splitlines():
    count += 1
    print(f"Line {count}: {line}")

pi_single_line = ''
for line in content.splitlines():
    pi_single_line += line

print(f"\nPI value: {pi_single_line}")