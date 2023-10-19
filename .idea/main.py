table = [["0", "-", "-", "-",], ["1", "-", "-", "-",], ["2", "-", "-", "-",]]

win_conds = [(table[0][1], table[0][2], table[0][3]), (table[1][1], table[1][2], table[1][3]), (table[2][1], table[2][2], table[2][3]),(table[0][1], table[1][1],table[2][1]), (table[0][2], table[1][2], table[2][2]), (table[0][3], table[1][3], table[2][3]), (table[0][1], table[1][2], table[2][3]), (table[0][3], table[1][2], table[2][1])]

def pr_table():
    print(" ", 1, 2, 3)
    for rows in table:
        print(*rows)


def autocount():
    counter = 0
    while True:
        yield counter
        counter += 1


def hodim_x():
    while True:
        print("ход крестика")
        i = int(input("Выбери строку: "))
        j = int(input("Выбери столбец: "))
        if i not in range(3) or j not in range(1,4):
             print("Неверный ввод. Попробуйте снова.")
             continue
        if table[i][j] == "X" or table[i][j] == "O":
            print("Место уже занято. Выберите другое.")
            continue
        else:
            table[i][j] = "X"
        pr_table()
        break

def hodim_o():
    while True:
        print("ход нолика")
        i = int(input("Выбери строку: "))
        j = int(input("Выбери столбец: "))
        if i not in range(3) or j not in range(1,4):
            print("Неверный ввод. Попробуйте снова.")
            continue
        if table[i][j] == "O" or table[i][j] == "X":
            print("Место уже занято. Выберите другое.")
            continue
        else:
            table[i][j] = "O"
        pr_table()
        break


def check_win():
    if (table[0][1] == "X" and table[0][2] == "X" and table[0][3] == "X") or (table[1][1] == "X" and table[1][2] == "X" and table[1][3] == "X") or (table[2][1] == "X" and table[2][2] == "X" and table[2][3] == "X") or (table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X") or (table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X") or (table[0][3] == "X" and table[1][3] == "X" and table[2][3] == "X") or (table[0][1] == "X" and table[1][2] == "X" and table[2][3] == "X") or (table[0][3] == "X" and table[1][2] == "X" and table[2][1] == "X"):
        print("Крестики победили!")
        return True
    elif (table[0][1]  == "O" and table[0][2] == "O" and table[0][3] == "O") or (table[1][1] == "O" and table[1][2] == "O" and table[1][3] == "O") or (table[2][1] == "O" and table[2][2] == "O" and table[2][3] == "O") or (table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "O") or (table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "O") or (table[0][3] == "O" and table[1][3]  == "O" and table[2][3] == "O") or (table[0][1] == "O" and table[1][2] == "O" and table[2][3]  == "O") or (table[0][3] == "O" and table[1][2] == "O" and table[2][1] == "O"):
        print("Нолики победили!")
        return True

#Главный механизм игры:
hod = autocount()
pr_table()
for h in range(10):
    if check_win():
        break
    print("Текущий ход", next(hod))
    if h % 2 == 0:
        hodim_x()
    else:
        hodim_o()
    if h > 8:
        print("Ничья!")
        break
