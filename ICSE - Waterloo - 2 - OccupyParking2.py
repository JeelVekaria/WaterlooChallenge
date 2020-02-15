n=int(input("Enter Parking spots: "))
str1=input("Yesterday spots: ")
str2=input("Today spots: ")
occ=0
x=0
while x < n:
  if str1[x] == str2[x]:
    occ+=1  
  x+=1
print(occ)
