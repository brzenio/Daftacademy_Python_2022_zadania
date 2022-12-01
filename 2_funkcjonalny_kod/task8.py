# Ulepsz kalkulator z `task6` tak aby był w stanie
# wykonać działanie dowolnej długości.
#
# Przykład:
# calculator(1)('+')(4)('-')(2)('=') == 3
#
# * Kalkulator musi wspierać działania dodawania
#   i odejmowania
# * Każde działanie kończy się znakiem '='
# * Nie korzystaj ze zmiennych globalnych i importów
#
# Powodzenia!


def calculator(*args):    
    def operand(operation):
        def calc(y):
            if operation == '-':
                return x - y
            elif operation == '*':
                return x * y
            elif operation == '**':
                return x ** y
            elif operation == '|':
                return x | y
            elif operation == '&':
                return x & y
            else:
                return x + y
        return calc
    return operand

print(calculator(1)('-')(2))
