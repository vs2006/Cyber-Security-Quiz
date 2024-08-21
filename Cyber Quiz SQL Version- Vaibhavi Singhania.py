import mysql.connector as SQL
MyDB=SQL.connect(host='localhost', user='root', password='manushree', database='CyberSecurity')
MyCursor=MyDB.cursor()
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
    return str(score)
def AddModify(name, score):
    Command="Select * from Score;"
    MyCursor.execute(Command)
    List=MyCursor.fetchall()
    found=0
    if (len(List)!=0):
        for ele in List:
            if (ele[0]==name):
                Command1="Update Score set Score=%s where Name=%s;"
                Value=(score, name)
                MyCursor.execute(Command1, Value)
                MyDB.commit()
                found=1   
    if (found==0):
        Command1= "Insert into Score Values(%s, %s);"
        Value=(name,score)
        MyCursor.execute(Command1, Value)
        MyDB.commit()
def GetScore(name):
    Command="Select * from Score;"
    MyCursor.execute(Command)
    List=MyCursor.fetchall()
    found=0
    for ele in List:
        if (ele[0]==name):
            print(ele[1])
            found=1
    if (found==0):
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
