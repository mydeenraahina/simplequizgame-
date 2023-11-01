

#type 1
def play():
    score=0
    question1=input("india is a ________ contry : ")
    if question1.lower()=="developing":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question2=input("capital of india : ")
    if question2.lower()=="newdelhi":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question3=input("capital of tamilnadu : ")
    if question3.lower()=="chennai":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question4=input("unity in ________")
    if question4.lower()=="diversity":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question5=input("nellai is famous for _____")
    if question5.lower()=="halwa":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question6=input("how many days in a week : ")
    if question6.lower()=="seven":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question7=input("national bird :")
    if question7.lower()=="peacock":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question8=input("national fruit :")
    if question8.lower()=="mango":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question9=input("national animal :")
    if question9.lower()=="tiger":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question10=input("In india english is ___________ language  :")
    if question10.lower()=="communication":
        print("correct")
        score=score+1
    else:
        print("incorrect")
    print("Total score=",score)
print("welcome to our quiz")
choice=input("do you want do play this game:")
if choice.lower()=="yes":
    print("let's play")
    play()
else:
    print("type no to exit/yes to continue")
while True:
    choice=input("do you want continue this game:")
    if choice.lower()=="yes":
        print("let's play")
        play()
    else:
        print("exited!")
        break
#type 2
def play():
    score=0
    score1=0
    question1=input("india is a ________ contry : \n a)developing b)developed\nyour answer is ")
    if question1.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question2=input("capital of india : \n a)newdelhi  b)bombay\nyour answer is")
    if question2.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question3=input("capital of tamilnadu : \n a)chennai  b)madurai\nyour answer is")
    if question3.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question4=input("unity in ________  \n a)diversity   b)varity\nyour answer is")
    if question4.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question5=input("nellai is famous for _____  \n a)halwa b)laddu\nyour answer is")
    if question5.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question6=input("how many days in a week : \n  a)seven b)six\nyour answer is")
    if question6.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question7=input("national bird : \n a)peacock b)kiwi\nyour answer is")
    if question7.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question8=input("national fruit :\n  a)mango b)apple\nyour answer is")
    if question8.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question9=input("national animal :\n a)tiger  b)lion\nyour answer is")
    if question9.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    question10=input("In india english is ___________ language  :\n  a)comunicative  b)mother language\nyour answer is:")
    if question10.lower()=="a":
        print("correct")
        score=score+1
    else:
        print("incorrect")
        score1=score1+1
    print("Total score \n correct",score,"incorrect",score1)
print("welcome to our quiz")
choice=input("do you want do play this game:")
if choice.lower()=="yes":
    print("let's play")
    play()
else:
    print("type no to exit/yes to continue")
while True:
    choice=input("do you want continue this game:")
    if choice.lower()=="yes":
        print("let's play")
        play()
    else:
        print("exited!")
        break
        


        

