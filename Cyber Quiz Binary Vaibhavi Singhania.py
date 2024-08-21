import pickle
def Play():
    F=open("QuizVaibhavi.txt","r")
    q=F.readlines()
    score=0
    for i in range(0,len(q),3):
        print(q[i])
        print(q[i+1])
        ans=input("Enter your answer choice: ")
        cc=(q[i+2]).rstrip("\n")
        if ((ans.upper())==cc):
            score+=1
            print("Good Job! Your answer is correct!")
        else:
            print("Wrong Choice. The correct answer is",q[i+2])
    return score
def AddModify(name, score):
    F=open("ScoreQuiz.dat","rb")
    try:
        LL=pickle.load(F)
    except:
        LL=[]
    found=0
    for R in LL:
        if(R[0]==name):
            R[1]=score
            found=1
            F.close()
            F=open("ScoreQuiz.dat","wb")
            pickle.dump(LL,F)
            F.close()
    if (found==0):
        L=[name,score]
        LL.append(L)
        F.close()
        F=open("ScoreQuiz.dat","wb")
        pickle.dump(LL,F)
        F.close()
def GetScore(name):
    try:
        F=open("ScoreQuiz.dat","rb")
        LL=pickle.load(F)
        found=0
        for R in LL:
            if (R[0]==name):
                print(R[1])
                found=1
        if (found==0):
            print("No record found!")
        F.close()
    except:
        print("No record found!")

print("Please choose one of the following.")
print("1. Play Quiz")
print("2. Get Previous Score")
print("3. Quit")
name1=input("Enter your name: ")
choice=0
while (choice!='3'):
    choice=input("Enter your choice: ")
    if (choice=='1'):
        S=Play()
        AddModify(name1, S)
    elif (choice=='2'):
        name2=input("Enter the name of the record to be searched: ")
        GetScore(name2)
    elif (choice=='3'):
        print("Thank You")
    else:
        print("Invalid Choice!")
