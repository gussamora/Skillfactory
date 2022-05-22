f_field = [["_", "_", "_"],
           ["_", "_", "_"],
           ["_", "_", "_"]]


def greeting():  # Приветственное окно
    print("Крестики-нолики")
    print("---------------")
    print("X - строки")
    print("Y - столбцы")


greeting()


def win_it_x(f_field):  # Проверка условий заполнения по игроку X

    lf_field = [[False, False, False],
                [False, False, False],
                [False, False, False]]

    lf_field_cross_1 = [[True, False, False],
                        [False, True, False],
                        [False, False, True]]
    lf_field_cross_2 = [[False, False, True],
                        [False, True, False],
                        [True, False, False]]
    lf_field_col_0 = [[True, False, False],
                      [True, False, False],
                      [True, False, False]]
    lf_field_col_1 = [[False, True, False],
                      [False, True, False],
                      [False, True, False]]
    lf_field_col_2 = [[False, False, True],
                      [False, False, True],
                      [False, False, True]]
    # Проверка горизонтального заполнения

    for i in range(3):
        for k in range(3):
            if f_field[i][k] == "x":
                lf_field[i][k] = True

    for i in range(3):
        if (all(lf_field[i])):
            return True

    # Проверка вертикального заполнения

    if lf_field == lf_field_col_0:
        return True

    if lf_field == lf_field_col_1:
        return True

    if lf_field == lf_field_col_2:
        return True

    # Проверка заполнения по диагонали слева сверху направо вниз

    if lf_field == lf_field_cross_1:
        return True

    # Проверка заполнения по диагонали справа сверху налево вниз

    if lf_field == lf_field_cross_2:
        return True

    return False


def win_it_y(f_field):  # Проверка условий заполнения по игроку Y

    lf_field = [[False, False, False],
                [False, False, False],
                [False, False, False]]

    lf_field_cross_1 = [[True, False, False],
                        [False, True, False],
                        [False, False, True]]
    lf_field_cross_2 = [[False, False, True],
                        [False, True, False],
                        [True, False, False]]
    lf_field_col_0 = [[True, False, False],
                      [True, False, False],
                      [True, False, False]]
    lf_field_col_1 = [[False, True, False],
                      [False, True, False],
                      [False, True, False]]
    lf_field_col_2 = [[False, False, True],
                      [False, False, True],
                      [False, False, True]]
    #     f_field_reverse = []

    # Проверка горизонтального заполнения

    for i in range(3):
        for k in range(3):
            if f_field[i][k] == "y":
                lf_field[i][k] = True

    for i in range(3):
        if (all(lf_field[i])):
            return True

    # Проверка вертикального заполнения

    if lf_field == lf_field_col_0:
        return True

    if lf_field == lf_field_col_1:
        return True

    if lf_field == lf_field_col_2:
        return True

    # Проверка заполнения по диагонали слева сверху направо вниз

    if lf_field == lf_field_cross_1:
        return True

    # Проверка заполнения по диагонали справа сверху налево вниз

    if lf_field == lf_field_cross_2:
        return True

    return False

def field(f_field):  # Прорисовка поля
    #     f_field = [["_", "_", "_"],
    #                ["_", "_", "_"],
    #                ["_", "_", "_"]]

    for i in range(3):
        #         for k in range(3):
        #         print(f" {i} {[' | '.join(f_field[i][k]) for k in range(3)]}")
        print(i, ' | '.join(f_field[i]))


field(f_field)

def in_data():  # Ввод координат и проверка корректности ввода
    while True:
        try:
            x, y = map(int, input("Введите координаты x y:").split())
        except ValueError as error:
            print("Введите целые числа от 0 до 2")
            continue
        else:

            if x > 2 or x < 0 or y > 2 or y < 0:
                print("Введите значения x и у в диапазоне от 0 до 2")
                continue

            return x, y
            break


def x_set(x, y, f_field):  # Присваивание клетке значения x

    while True:

        if (f_field[x][y] == "_"):
            f_field[x][y] = "x"
            break
        else:
            print("Клетка занята - введите координаты другой клетки")
            x, y = in_data()
            continue
    return f_field


def y_set(x, y, f_field):  # Присваивание клетке значения y

    while True:
        if (f_field[x][y] == "_"):
            f_field[x][y] = "y"
            break
        else:
            print("Клетка занята - введите координаты другой клетки")
            x, y = in_data()
            continue
    return f_field


marker = 1
num = 0
while True:
    if marker == 1:
        print("Очередь игрока X...")
        x, y = in_data()
        print(x, y)
        f_field = x_set(x, y, f_field)
        field(f_field)
        marker = 0
        num += 1
        if win_it_x(f_field):
            print("Победитель X!")
            break
    else:
        print("Очередь игрока Y...")
        x, y = in_data()
        print(x, y)
        f_field = y_set(x, y, f_field)
        field(f_field)
        marker = 1
        num += 1
        if win_it_y(f_field):
            print("Победитель Y!")
            break
    if num == 9:
        print("Ничья")
        break