def basic_int_operations(a, b):
    # Policz kolejno: sumę, różnicę, iloczyn i iloraz liczb a i b
    # Wyniki powyższych operacji przypisz do odpowiadających im zmiennych
    # zadeklarowanych poniżej
    sum: int = int(a + b)
    difference: int = int(a - b)
    product: int = int(a * b)
    quotient: int = int(a / b)

    return sum, difference, product, quotient


def string_length(a: str):
    # Przypisz do zmiennej `length` długość ciągu znaków otrzymanego jako argument `a`
    length: int = len(a)
    return length


def first_and_last_chars(a: str):
    # Do zmiennych `first` i `last` przypisz kolejno pierwszy i ostatni znak
    # z otrzymanego ciągu znaków w argumencie `a`
    first: str = a[0]
    last: str = a[len(a)-1]

    return first, last


def string_capitalization(a: str):
    # Do zmiennych zadeklarowanych poniżej przypisz otrzymany w argumencie `a` ciąg znaków
    # po przekonwertowaniu go odpowiednio na same wielkie litery (zmienna `upper`) i same
    # małe litery (zmienna `lower`)
    upper: str = a.upper()
    lower: str = a.lower()

    return upper, lower


def add_exclamation_mark(a: str):
    # Do zmiennej `result` przypisz ciąg znaków otrzymany w argumencie `a`
    # jeśli ciąg znaków `a` nie posiada na końcu znaku `!`, dodaj go
    if a[len(a)-1] != "!":
        result: str = a + "!"
        return result
    else:
        result: str = a
        return result


def cut_string(a: str):
    # Do zmiennej `result` przypisz ciąg znaków `a` po wycięciu z niego ciągu `python`
    # co najwyżej jednokrotnie
    # Przykład: JDSKJBGEpythonDD -> JDSKJBGEDD
    first_pos = a.find('python')
    if first_pos > 0:
        last_pos = first_pos + len("python")
        result: str = a[0:first_pos] + a[last_pos::]
        return result
    elif first_pos == 0:
        last_pos = first_pos + len("python")
        result: str = a[last_pos::]
        return result
    else:
        result: str = a
        return result