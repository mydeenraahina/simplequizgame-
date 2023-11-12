def main_block():
    def play():
        answers={'question1':'developing',
                 'question2':'newdelhi',
                 'question3':'chennai',
                 'question4':'diversity',
                 'question5':'halwa',
                 'question6':'seven',
                 'question7':'peacock',
                 'question8':'mango',
                 'question9':'tiger',
                 'question10':'communication'}
        score_loss=0
        score_gain=0
        question1=input("india is a ________ contry : ")
        if question1.lower()==answers['question1']:
            print("correct")
            score_gain+= 1
        else:
           print("incorrect")
           score_loss+= 1
        question2=input("capital of india : ")
        if question2.lower()==answers['question2']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question3=input("capital of tamilnadu : ")
        if question3.lower()==answers['question3']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question4=input("unity in ________")
        if question4.lower()==answers['question4']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question5=input("nellai is famous for _____")
        if question5.lower()==answers['question5']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
        question6=input("how many days in a week : ")
        if question6.lower()==answers['question6']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question7=input("national bird :")
        if question7.lower()==answers['question7']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question8=input("national fruit :")
        if question8.lower()==answers['question8']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question9=input("national animal :")
        if question9.lower()==answers['question9']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        question10=input("In india english is ___________ language  :")
        if question10.lower()==answers['question10']:
            print("correct")
            score_gain+=1
        else:
            print("incorrect")
            score_loss+= 1
        print("Total score")
        print("correct: ",score_gain)
        print("incorrect: ",score_loss)
    print("let's play")
    play()
    while True:
        choice=input(f"Do you want continue this game[yes/no]:")
        if choice.lower()=="yes":
            print("let's play")
            play()
        elif choice.lower()=="no":
            print("Exit!")
            break
        else:
            print("you are enterd wrong value")
            while True:
                print("try again!")
                choice=input(f"Do you want do play this game[yes/no]:")
                if choice.lower()=="yes":
                    main_block()
                elif choice.lower()=="no":
                    print("Exit!")
print("welcome to our quiz")
choice=input(f"Do you want do play this game[yes/no]:")
if choice.lower()=="yes":
    main_block()
elif choice.lower()=="no":
     print("Exit!")
else:
    print("you are enterd wrong value")
    while True:
        print("try again!")
        choice=input(f"Do you want do play this game[yes/no]:")
        if choice.lower()=="yes":
            main_block()
        elif choice.lower()=="no":
            print("Exit!")
