# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

from random import randint
from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'На вход должен подаваться непустой целочисленный список')
    return sorted(arr, reverse=True)


if __name__ == '__main__':
    numbers = [randint(0, 100) for i in range(7)]
    print(numbers)
    print(selection_sort(numbers))
