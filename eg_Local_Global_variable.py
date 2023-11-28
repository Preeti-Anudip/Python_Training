#Local variable and Global variable:-
#Local variables are those variables which are accessible only within the code block,we can not access outside the codeblock.

def localVariableTest():
    x=20
    print(x)
localVariableTest()
# if we try to access,will throw an error('x' is not defined)
print(x)

#Global variables are those variables which are accessible within the code block as well as outside the codeblock,we can use global variable throughout the whole program.
x=200
def globalVariableTest():
    print(x)
localVariableTest()
print(x)
