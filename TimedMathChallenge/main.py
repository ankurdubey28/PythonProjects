import random
import time

OPERATORS=['+','-','*','/']
MIN_OPERAND=3
MAX_OPERAND=12
MAX_PROBLEMS=25

def generate_problem()->(int,int):
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)

    expr=str(left)+str(operator)+str(right)
    answer=eval(expr)
    return expr,answer


start=time.time()
while(True):
    MAX_PROBLEMS-=1
    problem,ans=generate_problem()
    print(problem)
    user_answer=input("Enter your solution : ")
    if user_answer==str(ans):
        end=time.time()
        print("Correct answer!")
        print(round(end-start,2))
        break
    elif MAX_PROBLEMS<0:
        print("Too many attempts , you lose")
        print(round(time.time()-start,2))
    else:
        print("Wrong Answer")
        continue