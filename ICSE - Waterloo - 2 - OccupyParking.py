s=int(input("Space"))
day1=input("yesterday")
day2=input("today")

count=0
a=0
for i in day1:
    if i =="c" and i ==day2[count]:
            a+=1
    count+= 1
    
print(a)
