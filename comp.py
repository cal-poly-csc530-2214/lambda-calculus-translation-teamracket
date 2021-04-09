import sys
import sexpdata
from sexpdata import loads, dumps


def compiler(exp, local_symbols = []):
    parsed_exp = loads(exp)

    if type(parsed_exp) is int:
        return dumps(parsed_exp)
    elif type(parsed_exp) is sexpdata.Symbol:
        local_symbols.append(parsed_exp)
        return dumps(parsed_exp)
    elif len(parsed_exp) == 3:
        if (dumps(parsed_exp[0]) =='+'):
            return compiler(dumps(parsed_exp[1])) + ' + ' + compiler(dumps(parsed_exp[2]))
        elif (dumps(parsed_exp[0]) =='*'):
            return compiler(dumps(parsed_exp[1])) + ' * ' + compiler(dumps(parsed_exp[2]))
    elif len(parsed_exp) == 4:
        if (dumps(parsed_exp[0]) == 'ifleq0'):
            return "if " + compiler(dumps(parsed_exp[1])) + ":\n\t" + compiler(dumps(parsed_exp[2])) +"\nelse:\n\t"+compiler(dumps(parsed_exp[3]))
        elif dumps(parsed_exp[0]) == '/':
            res = compiler(dumps(parsed_exp[3]))
            arguments = ""
            for symbol in local_symbols:
                arguments += dumps(symbol)
            return compiler(dumps(parsed_exp[1])) + " = lambda " + arguments + " : " + res
    elif len(parsed_exp) == 2:
        if dumps(parsed_exp[0]) == 'println':
            return "print(\"" + dumps(parsed_exp[1]) + "\")"
        else:
            res = compiler(dumps(parsed_exp[0]))
            return"" + res+"\n"+"(" + res[0]+")" + "("+  compiler(dumps(parsed_exp[1]))+")"
    
           

def main():
    res = compiler('(println 1)')
    print(res)


if __name__ == '__main__':
    main()