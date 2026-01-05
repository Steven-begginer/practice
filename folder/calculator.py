#The purpose of function is to build the process of solution of problem.
def result(num):
    print(f"{round(num):.2f}") # 四舍五入
x = float(input("what is x? "))
y = float(input("what is y? "))
total = result(x + y)# the input and output address for function with leaving two digits.
