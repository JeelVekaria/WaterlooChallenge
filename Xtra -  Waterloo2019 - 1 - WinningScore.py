a3=int(input("Enter amount of team A 3 points: "))
a2=int(input("Enter amount of team A 2 points: "))
a1=int(input("Enter amount of team A 1 points: "))
b3=int(input("Enter amount of team B 3 points: "))
b2=int(input("Enter amount of team B 2 points: "))
b1=int(input("Enter amount of team B 1 points: "))
aa3=a3*3
aa2=a2*2
bb3=b3*3
bb2=b2*2
aaa=aa3+aa2+a1
bbb=bb3+bb2+b1
if aaa>bbb:
    print("A")
if aaa<bbb:
    print("B")
if aaa==bbb:
    print("T")