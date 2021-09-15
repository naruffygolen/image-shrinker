# Coding: utf-8
# Version : 3.0
# Author : Urzaiz

def cmd_options_value(arguments: list) -> dict:
    opt = {}
    if len(arguments) > 1:
        for i, item in enumerate(arguments):
            if item.startswith('-'):
                if (i + 1) < len(arguments):
                    if arguments[i + 1].startswith('-'):
                        opt[item] = ''
                    else:
                        opt[item] = arguments[i + 1]
                else:
                    opt[item] = ''
    elif len(arguments) == 1:
        opt[f'{arguments[0]}'] = ''

    return opt


def xor(operand_one: bool, operand_two: bool):
    return (operand_one or operand_two) and (not operand_one or not operand_two)


if __name__ == '__main__':
    import sys

    args = sys.argv[1:]

    print(cmd_options_value(args))
