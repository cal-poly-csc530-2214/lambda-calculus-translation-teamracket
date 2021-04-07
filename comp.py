import sys
import re

def compiler(exp):
    print 'Number of arguments:', len(exp), 'arguments.'
    print 'Argument List:', str(exp)
    



def main():
    compiler(sys.argv)


if __name__ == '__main__':
    main()