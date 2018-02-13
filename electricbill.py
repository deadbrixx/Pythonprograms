print("Hey user ..enter your electric unit you consumed..")
unit = int(input("enter:-"))
print(unit)
unitprice=0
totalbill=0
discount=3.25

if(unit<25):
    unitprice=unit*5
    print("U have to pay:-",unitprice,"ruppes")
    totalbill = unitprice
    print("your total bill is of rupess:-", totalbill)
elif(unit<50):
    unitprice=unit*6.35
    print("u have to pay:-",unitprice," ruppes")
    totalbill = unitprice
    print("your total bill is of rupess:-", totalbill)
elif(unit<100):
    unitprice=unit*9.88
    print("u have to pay:-",unitprice,"rupeess")
    totalbill = unitprice
    print("your total bill is of rupess:-", totalbill)
elif(unit>100):
    unitprice=unit*11
    print("u have to pay:-",unitprice,"rupeess")
    totalbill = unitprice
    print("your total bill is of rupess:-",totalbill)
if(totalbill>500):
    discount_bill = totalbill-(3.25*10)
    print("your discounted bill is:-",discount_bill)
else:
    print("Sorry.... increase your unit to take discount advantage")
print("Hyderabad electric department..")

