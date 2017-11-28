import random
sports=["basketball", "football", "cricket", "badminton", "tennis", "carom", "baseball", "volleyball"]
countries=["india", "pakistan" "israel", "afghanistan","bangladesh","china", "japan","france", "italy", "germany"]
flowers=["rafflesia", "lotus", "rose", "sunflower", "lily", "orchid", "marigold"]
instruments=["guitar", "harmonium", "sitar", "violin", "flute", "mouth organ", "piano"]
print("Enter your choice.")
ch=int(input("1.Sports\n2.Countries\n3.Flowers\n4.Musical Instruments"))


if ch==1:
  s=random.choice(sports)
elif ch==2:
  s=random.choice(countries)
elif ch==3:
  s=random.choice(flowers)
else:
  s=random.choice(instruments)

print("Guess the word.")
print("It is {} letters long.".format(len(s)))
n="_"*len(s)

for j in range(len(s)):
    flag=0
    s1=input()
    if(s1==s):
        print("CONGRATULATIONS!!!")
        print("Your answer is right!")
        break
    for i in range(len(s)):
         if s[i]==s1:
             #print("_"*i,s1,"_"*(len(s)-i-1))
             n=n[0:i]+s1+n[i+1:len(s)]
    print(n)


if s==n:
    print("CONGRATULATIONS!!")
    print("You guessed it right!")
else:
    print("SORRY!!")
    print("Chances over!!")
    print("You are not right!")
