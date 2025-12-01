import time
timetaken = []
marks = 0
questions = [
   'Question1: Which is the only letter in the ENglish alphabet not used in any US state name?',
   'Question2: What is the scientific study of earth quakes called?',
   'Question3: How many hearts does an octapus has?',
   'Question4: Which is planet in our solar system is knowm to be prominent ring?',
   'Question5: Who is the author of the Harry Potter book series?',
   'Question6: What is the highest grossing film all the time?',
   'Question7: In which year Berlin wall fall?',
   'Question8: Which country has the most natural lakes in the world?',
   'Question9: Which mountain range seperates the Europe and Asia?',
   'Question10: Capital of Australia?'
]
Options = [
   ['Q','A','L','K'],['Sesimograph',"geology",'lifterogrpah','magnitudo'],['3','6','8','4'],
   [' Saturn','uranus','earth','mars'],['J.K.Rowling','Charlies','Mani','nilam'],['Avatar','RRR','Bahnubali','U87'],
   ['1989','1789','1987','1990'],['Canada','India','Portugal','Russia'],['Ural','Aravali','Mount','Kani'],
   ['Cannberra','Berlin','Tokyo','joyo']
]

print("Going to start in 2sec....")
time.sleep(2)
print("------WElcome to the QUIZ Zone-----")
i = 1

for a,b in zip(questions,Options):
    print(a,"\n",b)
    a = input("Enter your choice as A | B | C | D: ")
    st = time.time()
    et = time.time()-st
    timetaken.append(et)
    
    if a == 'A':
        print("You are correct!!")
        marks+=10
    else:
        print("You lose")
print("Your Score:",marks)
print("You have fnished your quiz in just",sum(timetaken),"sec")

