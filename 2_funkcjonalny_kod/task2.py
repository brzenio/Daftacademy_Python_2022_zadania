# Uzupełnij deklarację funkcji `multi_calculator` tak,
# aby funkcja działała analogicznie do funkcji `simple_calculator`,
# z tą różnicą, że obsługuje więcej niż dwa argumenty pozycyjne.
#
# * Jeśli funkcja nie otrzyma żadnych argumentów powinna
#   zwrócić `0` niezależnie od `operation`
# * Jeśli funckja otrzyma jeden argument pozycyjny powinna
#   zwrócić jego wartość niezależnie od `operation`
# * Domyślną operacją jest dodawanie
#
# Przykład 1:
# multi_calculator(1, 1, 1, 1, 1, 1) == 6
#
# Przykład 2:
# multi_calculator(10, 1, 1, operation='-') == 8
#
# Przykład 3:
# multi_calculator(operation='|') == 0
#
# Przykład 4:
# multi_calculator(3) == 3


# def multi_calculator():
#     pass


# def simple_calculator(*args, operation='+'):
#     if operation == '-':
#       return args 
#     elif operation == '*':
#         return x * y
#     elif operation == '**':
#         return x ** y
#     elif operation == '|':
#         return x | y
#     elif operation == '&':
#         return x & y
#     else:
#         return sum(args)


# lambda args : expression


def multi_calculator(*args: int, operation: str = '+') -> None:
    # print(args)
    if args == tuple():
        return 0
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]

    if operation == '+':
        return sum(args)

    if operation == '-':
        substract = args[0]
        for arg in args[1:]:
            substract -= arg
        return substract

    if operation == '*':
        multiplication = 1
        for arg in args:
            multiplication *= arg
        return multiplication

    if operation == '**':
        pow = args[0]
        for arg in args:
            pow **= arg
        return  pow

    if operation == '|':
        dif = args[0]
        for arg in args:
            dif |= arg
        return dif

    if operation == '&':
        binary_op = args[0]
        for arg in args:
            binary_op &= arg
        return binary_op