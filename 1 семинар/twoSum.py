# Сумма всех чисел
# Идея: 
# Cравниваем сумму для значений индексов 2-x указателей с искомой суммой. 
# Если меньше, то двигаем левый указатель вправо
# Если больше, то двигаем правый указатель влево

def twoSum(arr,sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        tmp = arr[left] + arr[right]
        if tmp == sum:
            return arr[left], arr[right]
        elif tmp < sum:
            left += 1
        elif tmp > sum:
            right -= 1
    return None

# Тест
def test_twoSum():
    test = [3, 8, 9, 11, 16, 18, 19, 21]
    sum = 25
    assert twoSum(test, sum) == (9, 16)
    return True

test_twoSum()
