# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

from random import randint


def heapify(arr, n, i):
    largest = i   # Инициализируем наибольший элемент как корень кучи
    l = 2 * i + 1   # Левый дочерний элемент
    r = 2 * i + 2   # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if l < n and arr[i] < arr[l]:
        largest = l

    # Если правый дочерний элемент больше наибольшего элемента
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Изменяем корень, если нужно
    if largest != i:
        # меняем корень и наибольший элемент
        arr[i], arr[largest] = arr[largest], arr[i]

        # рекурсивно применяем heapify к измененной поддереву
        heapify(arr, n, largest)

# Функция сортировки кучей


def heapSort(arr):
    n = len(arr)

    # Построение кучи (перегруппируем массив)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи в упорядоченном порядке
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # меняем корень и i-ый элемент
        heapify(arr, i, 0)


array = [randint(1, 100) for i in range(100)]
heapSort(array)
print(array)