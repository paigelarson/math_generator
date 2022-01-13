#imports (Are not my own work)
from random import randint
from time import time


#list of random numbers for the functions to pick from
nums=[]
for i in range(500):
    nums.append(randint(-100,100))

#creates addition problems
def addition_problem(num_list):
    #randint is a method from the random library that returns a random number between or equal to the max and min. I did not write it
    num1 = num_list[randint(0,len(num_list)-1)]
    num2 = num_list[randint(0,len(num_list)-1)]
    answer = num1 + num2
    print(str(num1) + " + " + str(num2) + " = ?")
    correct = False
    while not correct:
        response = int(input("Enter your answer: "))
        correct = (answer == response)
        if correct:
            print("Correct!")
        else:
            print("Incorrect. Try again")

#creates subtraction problems
def subtraction_problem(num_list):
    #randint is a method from the random library that returns a random number between or equal to the max and min. I did not write it
    num1 = num_list[randint(0,len(num_list)-1)]
    num2 = num_list[randint(0,len(num_list)-1)]
    answer = num1 - num2
    print(str(num1) + " - " + str(num2) + " = ?")
    correct = False
    while not correct:
        response = int(input("Enter your answer: "))
        correct = (answer == response)
        if correct:
            print("Correct!")
        else:
            print("Incorrect. Try again")

#creates multiplication problems
def multiplication_problem(num_list):
    #randint is a method from the random library that returns a random number between or equal to the max and min. I did not write it
    num1 = num_list[randint(0,len(num_list)-1)]
    num2 = num_list[randint(0,len(num_list)-1)]
    answer = num1 * num2
    print(str(num1) + " * " + str(num2) + " = ?")
    correct = False
    while not correct:
        response = int(input("Enter your answer: "))
        correct = (answer == response)
        if correct:
            print("Correct!")
        else:
            print("Incorrect. Try again")

#creates division problems
def division_problem(num_list):
    #randint is a method from the random library that returns a random number between or equal to the max and min. I did not write it
    num1 = num_list[randint(0,len(num_list)-1)]
    num2 = num_list[randint(0,len(num_list)-1)]
    answer = num1 // num2
    print(str(num1) + " / " + str(num2) + " = ?")
    correct = False
    while not correct:
        response = int(input("Enter your answer (if it's a decimal, round down):  "))
        correct = (answer == response)
        if correct:
            print("Correct!")
        else:
            print("Incorrect. Try again")

#Asks for how many problems the user wants to try and decided which type of problem to give them. Gives them the problem and, when they are finished,
#prints out the amount of time that it took them to answer the problems.
def main():
    num_problems = int(input("How many problems would you like to try?"))

    #time() is a method from the time library that returns the time since the program started. I did not write it
    start_time = time()

    for i in range(num_problems):
        problem=randint(1,4)
        if problem==1:
            addition_problem(nums)
        elif problem==2:
            subtraction_problem(nums)
        elif problem==3:
            multiplication_problem(nums)
        elif problem==4:
            division_problem(nums)
  
        print("")

    #time() is a method from the time library that returns the time since the program started. I did not write it
    end_time = time()

    time_taken = end_time - start_time

    print("You took " + str(time_taken) + " seconds to answer " + str(num_problems) + " question(s)")

#main function call
main()
  
