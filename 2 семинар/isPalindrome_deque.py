# Является ли слово палиндромом (дек)
# Идея:
# Задаем дек и сравниваем левое и правое значения
from collections import deque
def isPalindrome_deque(word):
    d = deque(word)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Тест
def test_isPalindrome_deque():
    test = 'abcba'
    assert isPalindrome_deque(test) == True
    return True

test_isPalindrome_deque()