import os

web_adresses = []
file_name = None

while True:
    file_name = input("Give file path [to EXIT press ENTER]:\t")
    if os.path.exists(file_name):
        break
    elif file_name == "":
        print("FORCED EXIT".center(60))
        break
    else:
        print("There is no such file directory\n".center(60))
    

with open(file_name, "r") as file:
    for line in file:
        web_adresses.append(line.replace("\n", ""))


for adress in web_adresses:
    if adress.endswith('pl'):
        print(f"{adress} is polih site")
    else:
        print(f"{adress} is other country site")

