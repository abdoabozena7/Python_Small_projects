import time
import random
n=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
total=0
total1=0
x1=random.choice(n)
x2=random.choice(n)
y1=random.choice(n)
y2=random.choice(n)
t1=random.choice(n)
t2=random.choice(n)
game=1
def display():
    global game
    global total
    global total1
    print(f"U have: {x1} and {x2} = {x1+x2}")
    print(f"computer have: {y1} and X ")
    total=x1+x2
    total1=y1+y2
def check():
    global game
    global total
    global total1
    display()
    if total ==21:
        print("صاحبي يا خلصت مبروك")
        game=0

    elif total==21:
        print("صاحبي يا خسرت")
        game=0

    if total >total1 and total <21:
        comPLAY()
        print(f"computer have total: {total1}")
        print("you win !")
        game=0

    elif total1 >total and total1 <21:
        uPLAY()
        print("computer win")
        game=0
def uPLAY():
    global total
    global total1
    global t1
    if total <17 :
        while total<21 :
            oo=input(f"you have {total} do you want more ?")
            if oo == 'y':
                total+=t1
            else:
                break
         
def comPLAY():
    global total
    global total1
    global t2
    while total1<17:
        if total1+t1 <21:
            total1+=t2
   
def game():
    while game!=0:
        display()
        check()
        
game()