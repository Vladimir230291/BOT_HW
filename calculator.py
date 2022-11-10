ops = {
    '+': lambda x, y: eval(str(x)) + eval(str(y)),
    '*': lambda x, y: eval(str(x)) * eval(str(y)),
    '/': lambda x, y: eval(str(x)) / eval(str(y)),
}


def make_operation(lst, opr):
    i = lst.index(opr)
    try:
        lst.insert(i - 1, ops[lst.pop(i)](lst.pop(i - 1), lst.pop(i - 1)))
    except IndexError:
        raise Exception("Не обнаружен операнд")
    except ValueError:
        raise Exception("Передан неверный тип данных")
    except NameError:
        raise Exception("Невозможно привести данные к вычисляемому типу")
    except Exception as error:
        raise Exception(error)
    return lst


def calculate(lst):
    operator = ["*", "/", "+"]
    while len(lst) > 1:
        while len(operator) > 0:
            if operator[0] in lst:
                lst = make_operation(lst, operator[0])
            else:
                operator.pop(0)
                if len(operator) == 0 and len(lst) > 1:
                    raise Exception("Не найден оператор для оставшихся чисел")
    return lst[0]


def open_brackets(lst):
    if lst.count('(') != lst.count(')'):
        raise Exception("Обнаружен неполный комплект скобок")
    while '(' in lst:
        i1, i2 = 0, 0
        for s in lst:
            if s == '(':
                i1 = lst.index(s)
            elif s == ")":
                i2 = lst.index(s)
                break
        calculated_value = calculate(lst[i1 + 1: i2])
        del lst[i1: i2 + 1]
        lst.insert(i1, calculated_value)
    print(lst)
    return lst


def negative(x):
    try:
        x = eval(x)
    except NameError:
        raise Exception(f"Невозможно привести {x} к вычисляемому типу")
    except Exception as error:
        raise Exception(error)
    return -x


def reformatNegativeValues(lst):
    for n in lst:
        if n == '-':
            index = lst.index(n)
            lst[index] = '+'
            lst[index+1] = negative(lst[index+1])
    return lst


