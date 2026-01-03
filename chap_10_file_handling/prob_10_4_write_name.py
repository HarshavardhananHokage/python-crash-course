from pathlib import Path

write_path = Path("guests.txt")

name = ''
input_value = ''
while input_value != "stop":
    input_value = input("Please enter your name: ")
    if input_value != "stop":
        name += input_value+"\n"

write_path.write_text(name.rstrip())