# Сортировка массива из 0 и 1
# Идея:
# Перебираем до встречи указателей, которые идут навстречу друг другу.


def sort_binary_array(arr):
    left, right = 0, len(arr) - 1 
    while left < right:
        # если слева равно 0 то двигаем левый
        if arr[left] == 0:
            left += 1
        # если справа равно 1 то двигаем правый
        elif arr[right] == 1:
            right -= 1
        # если слева значение больше, то меняем местами значения и двигаем оба указателя
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

# Тест
def test_sort_binary_array():
    test = [0, 1, 1, 0, 1, 0, 1, 0]
    assert sort_binary_array(test) == [0, 0, 0, 0, 1, 1, 1, 1]
    return True

test_sort_binary_array()