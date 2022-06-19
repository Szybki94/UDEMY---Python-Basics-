import os


file_name =     None
web_adresses =  []


while True:
    file_name = input("Give file path [to EXIT press ENTER]:\t")
    if os.path.exists(file_name):
        break
    elif file_name == "":
        print("FORCED EXIT".center(60))
        break
    else:
        print("There is no such file directory\n".center(60))
    
print()
with open(file_name, "r") as file:
    for line in file:
        web_adresses.append(line.replace("\n",''))
        
dir_name =          os.path.dirname(os.path.split(file_name)[0])\
                       + r"/output/"
webs_path_pl =      os.path.join(dir_name,'webs_pl.txt')
webs_path_other =   os.path.join(dir_name,'webs_other.txt')

file_pl =           open(webs_path_pl, "w")
file_other =        open(webs_path_other, "w")

for adress in web_adresses:
    if adress.endswith(".pl"):
        file_pl.write(adress + "\n")
    else:
        file_other.write(adress + "\n")

file_pl.close()
file_other.close()

print("Web pages are sorted".center(60))
print("-----END PROGRAM-----".center(60))
