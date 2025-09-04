import string
letters=string.ascii_lowercase
print (letters)
word=input("please enter a word\n").lower()
wor=""
   
for i in word:
 
     
    pos=letters.index(i)
    new_pos=(pos+2)
   # for wor in word:
    wor+=letters[new_pos]
    
    
print(f"the encrypted word is:{wor}")
