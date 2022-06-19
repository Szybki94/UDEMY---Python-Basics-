import os


file_path = r"/home/kamil/workspace/UDEMY/01_Python_dla_początkujących/27_OS_module/Exercise/input/orders.csv"

#Check directory exists
print("Does directory exists?\t", os.path.isdir(os.path.split(file_path)[0]))

#Check file exists
print("Does file exists?\t", os.path.isfile(file_path))
print("\n"*3)

with open(file_path, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        order = line.split(",")
        if len(order) == 3:
            print(f"Order from drugstore {order[0]}, item {order[1]}, amount {order[2]}")

        else:
            print(f"Line \"{line}\" malformed!!!")

    print("Processing finished")
