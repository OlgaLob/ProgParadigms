 # Таблица умножения
# Домашнее задание
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print('')


def main():
    n = int(input("Введите число n: "))
    multiplication_table(n)


if __name__ == "__main__":
    main()

 # В данном примере выбрана процедурная парадигма, так как в этой парадигме разработчики создают хорошо организованные,
 # модульные и многократно используемые процедуры, также известные как процедуры или функции, которые выполняют
 # конкретные задачи или вычисления в нисходящей последовательности.