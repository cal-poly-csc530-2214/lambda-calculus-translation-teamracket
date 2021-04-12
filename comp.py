import sys
import sexpdata
from sexpdata import loads, dumps


def compiler(exp):
    parsed_exp = loads(exp)

    # checks for num
    if type(parsed_exp) is int:
        return dumps(parsed_exp)

    # checks for symbols
    elif type(parsed_exp) is sexpdata.Symbol:
        return dumps(parsed_exp)
        
    # checks plus and multiplication    
    elif len(parsed_exp) == 3:     
        if (dumps(parsed_exp[0]) =='+'):
            return compiler(dumps(parsed_exp[1])) + ' + ' + compiler(dumps(parsed_exp[2]))
        elif (dumps(parsed_exp[0]) =='*'):
            return compiler(dumps(parsed_exp[1])) + ' * ' + compiler(dumps(parsed_exp[2]))
    # checks the if then else and lambda expression 
    elif len(parsed_exp) == 4:
        if (dumps(parsed_exp[0]) == 'ifleq0'):
            return "if " + compiler(dumps(parsed_exp[1])) + ":\n\t" + compiler(dumps(parsed_exp[2])) +"\nelse:\n\t"+compiler(dumps(parsed_exp[3]))
        elif dumps(parsed_exp[0]) == '/':
            return "lambda " + compiler(dumps(parsed_exp[1])) + " : " + compiler(dumps(parsed_exp[3]))
    # check f the functions are being applied or if there is a print statement
    elif len(parsed_exp) == 2:
        if dumps(parsed_exp[0]) == 'println':
            return "print(\"" + dumps(parsed_exp[1]) + "\")"
        else:
            return "(" + compiler(dumps(parsed_exp[0])) + ")(" + compiler(dumps(parsed_exp[1])) + ")"
 
    
           

def main():
    print(compiler('2'))
    print(compiler('a'))
    print(compiler('(+ 1 2)'))
    print(compiler('(* 1 2)'))
    print(compiler('(ifleq0 1 2 3)'))
    print(compiler('(println 1)'))
    print(compiler('(/ x => (+ x 1))'))
    print(compiler('((/ x => (+ x 1)) 2)'))
    

if __name__ == '__main__':
    main()