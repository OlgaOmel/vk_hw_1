# Слияние двух отсортированных массивов (с аллокацией)
# Идея:
# Создаем хранилище под сортированный массив. Сравниваем значения по указателям в 1 и 2 массивах.
# То что меньше - добавляем в хранилище и двигаем указатель того массива.
# Добавляем остатки массивов

def merge_sorted_arrays(arr1, arr2):
    sortMergeArr = []
    point_1, point_2 = 0, 0
    while point_1 < len(arr1) and point_2 < len(arr2):
        if arr1[point_1] < arr2[point_2]:
            sortMergeArr.append(arr1[point_1]) 
            point_1 +=1
        else: 
            sortMergeArr.append(arr2[point_2])
            point_2 +=1
    sortMergeArr.extend(arr1[point_1:])
    sortMergeArr.extend(arr2[point_2:])
    return sortMergeArr

# Тест
def test_merge_sorted_arrays():
    test_1 = [3, 8, 10, 11]
    test_2 = [1, 7, 9]
    assert merge_sorted_arrays(test_1, test_2) == [1, 3, 7, 8, 9, 10, 11]
    return True

test_merge_sorted_arrays()