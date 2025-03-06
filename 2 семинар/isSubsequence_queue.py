# Является ли одна строка исходной для другой (очередь)
# Создаем очередь. Перебираем строку 1 и добавляем все в очередь.
# Перебираем строку 2 и сравниваем с текущим элементом очереди. При совпадении удаляем.
import queue
def isSubsequence_queue(a, b):
    q = queue.Queue()
    for letter in a:
        q.put(letter)
    for letter in b:
        if q.queue[0] == letter:
            q.get()
    return q.empty()

# Тест
def test_isSubsequence_queue():
    test_1 = 'abd'
    test_2 = 'uabqd'
    assert isSubsequence_queue(test_1, test_2) == True
    return True

test_isSubsequence_queue()