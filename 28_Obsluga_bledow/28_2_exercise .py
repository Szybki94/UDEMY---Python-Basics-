import os
import sys


file_path = r'%s/orders.csv' % os.getcwd()
order = []

print(file_path)
 
with open(file_path,"r") as file:

    cnt = 1
 
    for line in file:
    
        try:
 
            line = line.replace('\n','')
            order = (line.split(','))

            pharmacy_name =     order[0]
            item =              order[1]
            amount =            int(order[2])
            print('Order from drugstore "%15s", item "%15s", amount %10d'\
                  % (pharmacy_name, item, amount))

        except ValueError as e:
            print(">It is not integer: ", e , "\n>In line: ", cnt)

        except IndexError as e:
            print(">There is not enough fields: ", e, "\n>In line: ", cnt)
        
        except:
            print("%15s%30s%40s" % \
                  (">There is error:", f"Error in line {cnt}", sys.exc_info()[0]))

        cnt += 1
            
               
    
 
print("Processing finished")
