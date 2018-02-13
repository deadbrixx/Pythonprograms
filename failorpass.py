print("Enter of marks of three subjects")

sub1 = int(input("first subject is : -"))
sub2 = int(input("second subject is : -"))
sub3 = int(input("third subject is : -"))

marks = [sub1,sub2,sub3]
total_marks = sum(marks)
print("total marks is :-",total_marks)

average_marks = total_marks/len(marks)
print("average marks is :-",average_marks)

if(sub1>=35):
    print("you are fucking....sub1")
else:
    print("you fail in subject 1")
print(".........")
if(sub2>=35):
    print("you are fucking....sub2")
else:
    print("you fail in subject 2")
print(".........")
if(sub3>=35):
    print("you are fucking....sub3")
else:
    print("you fail in subject 3")
print(".........")
