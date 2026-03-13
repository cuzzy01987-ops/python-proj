number = [] 


new_nember = -1

while new_nember != 0:
    new_nember = float(input("Enter a number (0 to stop): "))
    if new_nember != 0:
        number.append(new_nember)
    

sum = 0
for n in number:
    sum += n
    count = len(number)
    arvg = sum / count
    largesrt_num = number[0]
    if n > largesrt_num:
        largesrt_num = n
    
    
print("The sum is:", sum)
print("The average is:", arvg)
print("The maximum is:", largesrt_num)
