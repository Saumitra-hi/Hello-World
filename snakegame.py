import random
i=1
score=0
compscore=0
while i<=3:
        random_number= random.randint(0,2)
        print("enter 0 for snake 1 for water or 2 for gun")
        userinp= int(input())
        if userinp==0:
            if random_number==1:
                score = score+1
            elif random_number==2:
                compscore= compscore+1
        elif userinp==1:
            if random_number==0:
                compscore= compscore+1
            elif random_number==2:
                score= score+1
        elif userinp==2:
            if random_number==0:
                score=score+1
            elif random_number==1:
                compscore= compscore+1
        else:
            print("wrong input")
            break
        game= ["snake","water","gun"]
        print("computer chose",game[random_number])
        i=i+1
print ("user score is", + score)
print("computer score is",+ compscore)
if score>compscore:
    print("you win")
elif compscore>score:
    print("you lost")
else:
    print("draw")