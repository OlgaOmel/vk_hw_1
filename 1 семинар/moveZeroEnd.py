# Нули в конец
# Идея:
# Перебираем массив. Если значение не ноль, то меняем со значением нулевого указателя
# Если поменяли, двигаем нулевой указатель на 1 вправо

def moveZeroEnd(arr):
    zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[zero] = arr[zero], arr[i]
            zero += 1
    return arr

# Тест
def test_moveZeroEnd():
    test = [0, 0, 6, 0, 9, 8]
    assert moveZeroEnd(test) == [6, 9, 8, 0, 0, 0]
    return True

test_moveZeroEnd()
