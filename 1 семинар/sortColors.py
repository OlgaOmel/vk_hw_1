# Флаг Нидерландов
# Идея:
# Ставим 3 указателя. 
# Если текущий 0 - меняем текущий и следующий 0 местами. Двигаем их вправо.
# Если текущий 1 - двигаем текущий вправо.
# Если текущий 2 - меняем текущий и следующий 2 местами. Двигаем следующий 2 влево.

def sortColors(arr):
    
    low = 0 # следующий 0  
    high = len(arr) - 1 # следующий 2
    mid = 0 # текущий
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Тест
def test_sortColors():
    test = [2, 0, 2, 1, 1, 0]
    assert sortColors(test) == [0, 0, 1, 1, 2, 2]
    return True

test_sortColors()