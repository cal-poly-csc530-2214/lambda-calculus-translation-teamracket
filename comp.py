import sys
import sexpdata
from sexpdata import loads, dumps


def compiler(exp):
    parsed_exp = loads(exp)
    #"num ,id ,(+ num num)"

    if type(parsed_exp) is int:
        return dumps(parsed_exp)
    elif type(parsed_exp) is sexpdata.Symbol:
        return dumps(parsed_exp)
    elif len(parsed_exp) == 3:
        
        if(dumps(parsed_exp[0]) =='+'):
            return compiler(dumps(parsed_exp[1])) + ' + ' + compiler(dumps(parsed_exp[2]))
        elif (dumps(parsed_exp[0]) =='/'):
            return compiler(dumps(parsed_exp[1])) + ' / ' + compiler(dumps(parsed_exp[2]))


    


def main():
    res = compiler('(/ 1 2)')
    print(res)


if __name__ == '__main__':
    main()