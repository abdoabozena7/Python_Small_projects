
import random

words = ["python", "java", "javascript", "kotlin", "ruby", "swift","flutter"]
rand = random.choice(words)
x=len(rand)
n =["_"]*x
k =["$","$$","$$$","$$$$"]
print("number of letters :"+str(x))


lives=5
while "_" in n  and lives > 0:
    gussed = input("guss a letter\n").lower()
    if gussed not in rand:
        lives -= 1
        nn -= 1
        print(rand[n])

        print("just" + str([lives]) + "tries")
    for pos in range(x):
        if rand[pos] == gussed:
            n[pos] = gussed
    print(' '.join(n))
     if lives == 0:
    print(""" +---+
      |   |
      O   |
     /|\  |
     / \  |
          | 
     LOSER
          """)

    else:
       print("""
       *****
         YOU WIN 
        *****
      """)

