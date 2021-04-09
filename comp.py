import sys
import sexpdata
from sexpdata import loads, dumps


def compiler(exp, local_symbols = []):
    parsed_exp = loads(exp)

    # checks for num
    if type(parsed_exp) is int:
        return dumps(parsed_exp)

    # checks for symbols
    elif type(parsed_exp) is sexpdata.Symbol:
        local_symbols.append(parsed_exp)
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
            res = compiler(dumps(parsed_exp[3]))
            arguments = ""
            for symbol in local_symbols:
                arguments += dumps(symbol)
            return compiler(dumps(parsed_exp[1])) + " = lambda " + arguments + " : " + res
    # check f the functions are being applied or if there is a print statement
    elif len(parsed_exp) == 2:
        if dumps(parsed_exp[0]) == 'println':
            return "print(\"" + dumps(parsed_exp[1]) + "\")"
        else:
            res = compiler(dumps(parsed_exp[0]))
            return"" + res+"\n"+"(" + res[0]+")" + "("+  compiler(dumps(parsed_exp[1]))+")"
    
           

def main():
    print(compiler('2', []))
    print(compiler('a', []))
    print(compiler('(/ plusone => (+ x 1))', []))
    print(compiler('(+ 1 2)', []))
    print(compiler('(* 1 2)', []))
    print(compiler('(ifleq0 1 2 3)', []))
    print(compiler('((/ y => (+ x 1)) 2)', []))
    print(compiler('(println 1)', []))
    

if __name__ == '__main__':
    main()