#Anagram 
w1=input("Enter the first word:")
w2=input("Enter the second word:")
s1=sorted(w1)
s2=sorted(w2)
if s1==s2:
    print("The words",w1,"and ",w2,"are an Anagram")
else:
    print("The words",w1,"and ",w2,"are not an Anagram")
