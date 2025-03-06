# Является ли слово палиндромом (стек)
# Задаем списком стэк. Перебрали слово и сложили в стэк буквы. 
# Перебрали слово и проверили с совпадением стэка с конца.

def isPalindrome_stack(word):
    stack = []
    for letter in word:
        stack.append(letter)
        
    for letter in word:
        if letter != stack.pop():
            return False
    return True

# Тест
def test_isPalindrome_stack():
    test = 'abcba'
    assert isPalindrome_stack(test) == True
    return True

test_isPalindrome_stack()
