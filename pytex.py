# coding:utf-8

import sys
import re
import json


def data_repl(matchobj):
    try:
        val = eval(matchobj.group(1))
    except NameError:
        val = "ERROR"
    except SyntaxError:
        val = "SYNTAXERROR"
    return val


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        if line.startswith("%%% config"):
            flag = True
            continue
        elif line.startswith("%%%"):
            flag = False
        if flag:
            line = line.strip('%').strip()
            label, path = line.split(':')
            template = 'global {0}\n{0} = json.load(open("{1}"))'
            try:
                exec template.format(label, path)
            except IOError, err:
                print err
                exit(1)

        print re.sub("{#(.+)#}", data_repl, line.decode("utf-8"))


if __name__ == '__main__':
    main()
