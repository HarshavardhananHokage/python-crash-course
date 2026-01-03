from pathlib import Path

path = Path("learning_python.txt")

content = path.read_text().rstrip()
print(f"Raw content:\n{content}")

print("\nAs List:")
content_as_list = content.splitlines()
line_count = 0
for line in content_as_list:
    line_count += 1
    print(f"Line {line_count}: {line}")

print("\nAfter replacing Python with Java")
line_count = 0
for line in content_as_list:
    line_count += 1
    print(f'Line {line_count}: {line.replace("Python", "Java")}')