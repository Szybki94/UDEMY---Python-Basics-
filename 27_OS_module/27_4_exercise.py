import os

web_adresses = []
dirname = os.getcwd()
print(dirname)


while True:
    line = input("Write web adress [to EXIT press ENTER]:\t")
    if line == "":
        print("EXIT")
        break
    web_adresses.append(line)

file_name = input("Write file name:\t")

file_path = os.path.join(dirname + r"/Exercise/input", file_name + r".txt")

with open(file_path, "w") as file:
    for adress in web_adresses:
        file.write(adress + "\n")

