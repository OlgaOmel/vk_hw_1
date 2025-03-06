# Является ли одна строка исходной для другой (метод двух указателей)
# Ставим счетчики на начало строк.Если значения равны то двигаем первый, а не равны - второй.
# Если счетчик первый и длина первой строки равны, то исходная для второй

def isSubsequence_pointers(a, b):
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

# Тест
def test_isSubsequence_pointers():
    test1 = 'abd' 
    test2 = 'uabqd'
    assert isSubsequence_pointers(test1, test2) == True
    return True

test_isSubsequence_pointers()