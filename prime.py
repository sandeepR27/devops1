prime_num=int(input("enter a number:"))
for num in range(2,prime_num):
    count_divisor=0
    for a in range(1,num+1):
        if num%a==0:
            count_divisor+=1
    if count_divisor==2:
            print(num)