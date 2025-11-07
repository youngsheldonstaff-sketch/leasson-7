print ("enter subject marks out of 100")

m1=int(input("enter marks:"))
m2=int(input("enter marks:"))
m3=int(input("enter marks:"))
m4=int(input("enter marks:"))   
m5=int(input("enter markes:"))
tot=m1+m2+m3+m4+m5
avg=tot/5

if avg>=90:
    print("grade A1")
elif avg>=80:
    print ("grade A2")
elif avg>=65:
    print ("grade B1")
elif avg>=50:
    print ("Grade B2")
elif avg>=35:
    print ("grade C")
elif avg<35:
    print ("fail")
else:
    print ("invalid input")