# Является ли слово палиндромом (метод двух указателей)
# Идея:
# Задаем указатели начала и конца и пока они не встретились сравниваем значения
# Убираем по 1 каждый раз

def isPalindrome_pointers(word):
    left, right = 0,0
    while left < right:
        if word[left] != word[right]:
            return False
        left +=1
        right -=1
    return True

# Тест
def test_isPalindrome_pointers():
    test = 'abcba'
    assert isPalindrome_pointers(test) == True
    return True

test_isPalindrome_pointers()