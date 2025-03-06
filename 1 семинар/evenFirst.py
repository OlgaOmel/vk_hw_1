# Передвинуть четные числа вперед
# Идея:
# Проверяем остаток при делении на 2. Если 0, то меняем местами со значением указателя четности.
# Двигаем указатель четности вправо

def evenFirst(arr):
    evenindex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenindex] = arr[evenindex], arr[i]
            evenindex += 1
    return arr


# Тест
def test_evenFirst():
    test = [7, 3, 2, 4, 1, 11, 8, 9]
    assert evenFirst(test) == [2, 4, 8, 3, 1, 11, 7, 9]
    return True

test_evenFirst()