str="[12,7],[13,14]"
numbers=[]
num=''
for c in str:

    if c.isdigit():
        num+=c
    else:
        if num!='':
            temp=int(num)
            numbers.append(temp)
            num=''

print(numbers)
