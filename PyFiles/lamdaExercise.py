import math as m
import inspect as ins
def traceTask(func):
    def calOperation(*args,**kargs):

        returned_value = func(*args,**kargs)
        length = args.__len__()
        funcName = ins.getsource(func).split()
        operation = getOperation(funcName)
        print("The Method Called is : ",operation[1])
        if(length == 2):
            print(f"Operation : {args[0]} " + operation[0] + f" {args[1]}  :  =",returned_value)
        else:
            print(f"Operation : {args[0]} " + operation[0] +" =",returned_value)
        
        print('Execution of the method is completed\n')
        return returned_value
    return calOperation

class Calculator:
    @traceTask
    def addedInto (num1 , num2):
        return num1 + num2
    @traceTask
    def subtractedBy (num1 , num2):
        return num1 - num2
    @traceTask
    def multipliedBy (num1 , num2):
        return num1 * num2
    @traceTask
    def dividedBy (num1 , num2):
        return num1 / num2

class ScientificCalculator(Calculator):
    log = traceTask(lambda x : m.log(x))
    power = traceTask(lambda x,y : x ** y)
    exponent = traceTask(lambda x : m.exp(x))
    factorial = traceTask(lambda x : m.factorial(x))

def getOperation(operation):
    if "addedInto" in operation[2]:
        return ["+",operation[2]]
    elif "multipliedBy" in operation[2]:
        return ["*",operation[2]]
    elif "subtractedBy" in operation[2]:
        return ["-",operation[2]]
    elif "dividedBy" in operation[2]:
        return ["/",operation[2]]
    elif "log" in operation[0]:
        return ["log",operation[0]]
    elif "power" in operation[0]:
        return ["^",operation[0]]
    elif "factorial" in operation[0]:
        return ["!",operation[0]]
    elif "exponent" in operation[0]:
        return ["E",operation[0]]            

ScientificCalculator.factorial(4)
ScientificCalculator.power(3,3)
ScientificCalculator.log(10)
ScientificCalculator.exponent(4)
ScientificCalculator.addedInto(2,2)
ScientificCalculator.multipliedBy(9,7)
ScientificCalculator.subtractedBy(89,56)
ScientificCalculator.dividedBy(9,18)
