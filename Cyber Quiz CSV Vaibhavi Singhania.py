import csv
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
    F=open("ScoreQuiz.csv","r+")
    List=csv.reader(F)
    LL=[]
    found=0
    for ele in List:
        LL.append(ele)
        if (ele[0]==name):
            ele[1]=score
            found=1
            F.close()
            F=open("ScoreQuiz.csv","w")
            ro=csv.writer(F)
            ro.writerows(LL)
            F.close()
            break
    if (found==0):
        ro=csv.writer(F)
        Data=[name,score]
        ro.writerow(Data)
        F.close()
def GetScore(name):
    F=open("ScoreQuiz.csv","r")
    List=csv.reader(F)
    found=0
    for ele in List:
        if (ele[0]==name):
            print(ele[1])
            found=1
    if (found==0):
        print("No record found!")
    F.close()

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

