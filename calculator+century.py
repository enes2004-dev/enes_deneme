num_1  = float(input("Enter second number : "))

num_2  = float(input("Enter second number : "))


op = input("Enter your opetare like minus  : " )

if op == "#" and num_2 == 0 :
    year_str = str(int(num_1))
    century_op = int(year_str[:2])
    century_op += 1
    print(f"The century is: {century_op}")


elif op == "-" and num_1 > num_2 :
    print(num_1 - num_2)
elif op =="-"  and  num_2 > num_1 :
    print(num_2 - num_1)
elif op == "+" :
    print(num_2 + num_1)
elif op == "*" :
    print(num_2 * num_1)
elif op == "/" :
    print(num_1 / num_2)

else:
    print("Hah you  did not find acceptable operate !!")









