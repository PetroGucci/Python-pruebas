my_list=[1,2,3,4,5,6,7,8,9,10]
to_find =6
found=False

for i in range(len(my_list)):
    found = to_find in my_list
    break
if found:
    print("elemento encontrado")
else:
    print("ausente")    