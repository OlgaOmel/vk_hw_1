# Развернуть весь массив
# Идея:
# Меняем местами значения индексов указателей
# Двигаем указатели вправо и влево к сближению


def reverseArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Тест
def test_reverseArray():
    test = [3, 8, 6, 9, 9, 8, 6]
    assert reverseArray(test) == [6, 8, 9, 9, 6, 8, 3]
    return True

test_reverseArray()