# Развернуть часть массива
# Идея:
# Нужно переместить вперед k чисел с конца. Используем функцию разворота полного + частичного по указателю k

def reverseArray(arr, left, right): # теперь указатели - параметры
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
def moveEnd(arr, k):
    n = len(arr)
    reverseArray(arr, 0, n - 1) # [7, 6, 5, 4, 3, 2, 1] Развернули весь
    reverseArray(arr, 0, k % n - 1) # [5, 6, 7, 4, 3, 2, 1] Развернули 3 первых
    reverseArray(arr, k % n, n - 1) # [5, 6, 7, 1, 2, 3, 4] Развернули после 3 первых
    return arr

# Тест
def test_moveEnd():
    # Тест 1
    test = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    assert moveEnd(test, k) == [5, 6, 7, 1, 2, 3, 4]
    # Тест 2: k > len(arr)
    test = [1, 2, 3, 4, 5, 6, 7]
    k = 8
    assert moveEnd(test, k) == [7, 1, 2, 3, 4, 5, 6]
    return True

test_moveEnd()