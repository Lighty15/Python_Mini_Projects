print("Welcome to python quiz!")

playing=input("Do you want to play? ")
if playing.lower()!="yes":
    quit()
print("Okay!Let's play")
score=0

answer=input("1.Is a list mutable or immutable? ")
if answer.lower()=="mutable":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("2.Which method can be used to return a string in uppercase letters? ")
if answer.lower()=="upper()":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("3.Which operator is used to multiply numbers? ")
if answer.lower()=="*":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("4.Which operator can be used to compare two values? ")
if answer.lower()=="==":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("5.How is list represented? ")
if answer.lower()=="[]":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("6.Who was the designer of Python? ")
if answer.lower()=="guido van rossum":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("7.Which datatype can be used to store the percentage obtained by a student? ")
if answer.lower()=="float":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("8.In which year was the Python language developed? ")
if answer.lower()=="1991":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("9.What will be the output of the following python code? print(int(3.9)) ")
if answer.lower()=="3":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("10.What will this code output? print(1>5) ")
if answer.lower()=="false":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
print("You got "+str(score)+ " questions correct")
print("You got "+str((score/10)*100)+ "%.")

    
