my_list = list(range(10,101,10))
print("My list:",my_list)
n = int(input("\nEnter number of times: "))
cir = my_list[n:] + my_list[:n]
print("\nCirculated list:",cir)
