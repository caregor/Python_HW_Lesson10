"""
1. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке
возрастания.
    Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

2. Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось

3. Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных
слов содержится в этом тексте.
    Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
    пробелов или символами конца строки.
Sample Input:
4

She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

Sample Output:
19
"""
# Task 1
#
# list_a = [1, 4, 6, 79, 3, 5, 6, 8, 8, 9, 2]
# list_b = [1, 4, 56, 7, 8, 9, 5, 4, 3, 789]
#
# print(set(list_a).intersection(set(list_b)))
#
# Task 2
#
# s = '1 2 3 1 4 5 6 7 8 9 0 1 2 2 1'
# list_numbers = list(map(int, s.split()))
# store_numbers = []
# for item in list_numbers:
#     if item not in store_numbers:
#         store_numbers.append(item)
#         print('NO')
#     else:
#         print('YES')
