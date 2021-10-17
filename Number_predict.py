import random;
a=0;
b=random.randrange(1,100);
c=1;
print("it is a game in which u have to predict the correct number in the range of 1 to 100 in five attempts")
while (c!=6):
    print("Choose a number betwwen 1 to 100")
    d=input();
    d=int(d)
    if d>b:
        print("enter a smaller number and u have "+str(5-c)+" attempts left")
    elif d<b:
        print("enter a larger number 5and u have "+str(5-c)+" attempts left")
    else :
        print("u won")
    c=c+1;
print("u loss")
