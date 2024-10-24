#Условия 
##int-cmp
Дается два числа a и b. Вернуть:
1, если a > b
0, если a = b
-1, если a < b
Sample Input:
1 0
Sample Output:
1

##max-of-three
Дается три числа a, b и c. Вернуть максимальное число из них.
Sample Input:
42 1 0
Sample Output:
42


#Циклы
##sqr-sum-1-n
Вернуть сумму квадратов чисел от 1 до n включительно.
Ограничения
1 <= n <= 10860



Sample Input:
3
Sample Output:
14





##print-even-a-b
Вывести в консоль четные числа в диапазоне от a включительно до b включительно.
Sample Input:
0 4
Sample Output:
0 2 4


##pow-a-b
Вернуть число a в степени b. Используя цикл.
Ограничения
b > 0
a^b входит в ограничения типа int
Sample Input:
2 6
Sample Output:
64



##calc-deposit
Написать функцию, которая возвращает сколько будет денег на депозите через n месяцев при ставке k и изначальном балансе b тенге.
Вознаграждения по депозиту начисляются каждый месяц.
Ограничения
0 <= n <= 10000
0 <= k <= 100
0 <= b <= 10000
Пример
Если положить на депозит 1000 тенге на срок в 1 месяц со ставкой в 5%, то через месяц на счете будет 1050 тенге.
Sample Input:
1 5 1000
Sample Output:
1050.0




#Массивы
##Min


Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0.
Ограничения
0 <= array.length <= 10_000
Sample Input:
[1, 2, 3]
Sample Output:
1


##range
Реализовать функцию range, которая создает массив размером n, заполняет ячейки значениями от 1 до n и возвращает созданный массив.
Пример
int[] arr = range(5);

for (int i = 0; i < arr.length; i++) {   
    System.out.print(arr[i] + " ");
}
// Напечатает
// 1 2 3 4 5
Ограничения
0 < n <= 10_000
Sample Input:
5
Sample Output:
[1, 2, 3, 4, 5]


##sum
Реализовать функцию sum, которая возвращает сумму чисел массива.
Пример
int array[] = {7, 5, 9, 1, 4};
int sum_number = sum(array);

print(sum_number); // <-- выведет 26
Ограничения
0 <= array.length <= 10_000
Sample Input:
[1, 2, 3]
Sample Output:
6

##sort
Реализовать функцию sort, которая принимает массив array(int[]). Функция должна отсортировать массив по возрастанию.
Подсказка: https://habr.com/ru/post/204600/
Запрещено использовать Arrays.sort.
Пример
int array[] = {7, 5, 9, 1, 4};
sort(array);

for (int i = 0; i < array.length; i++) {   
    System.out.print(array[i] + " ");
}
// Напечатает
// 1 4 5 7 9
Ограничения
0 <= array.length <= 10_000
Sample Input:
[3, 2, 1]
Sample Output:
[1, 2, 3]


def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

a, b = map(int, input().split())  
print(int_cmp(a, b))
#////////////////////////////////////////////////////////////////////////////////////////////////////

def max_of_three(a,b,c):
    return max(a,b,c)

a, b, c = map(int, input("Введите три числа: "))
print(max_of_three(a, b, c))

#///////////////////////////////////////////////////////////////////////////////////////////////////

def sqr_sum_1_n(n):
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input("Введите n: "))
print(sqr_sum_1_n(n))
#///////////////////////////////////////////////////////////////////////////////////////////////////


def print_even_a_b(a, b):
    if a % 2 != 0:
        a += 1

    for num in range(a, b + 1, 2):
        print(num)

a, b = map(int, input("Введите два числа: "))
print_even_a_b(a, b)

#///////////////////////////////////////////////////////////////////////////////////////////////////

def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *=a
    return result

a, b = map(int, input("Введите два числа (остнование и степень): "))
print(pow_a_b(a, b))
 

 #///////////////////////////////////////////////
def calc_deposit(b, k, n):
    for _ in range(n):
        b += b * (k / 100)
    return b 

b = float(input("Введите начальный баланс в тенге: "))
k = float(input("Введите процентную ставку в процентах: "))
n = int(input("Введите количество месяцев: "))

print(f"Итоговая сумма на депозите: {calc_deposit(b, k, n):.2f} тенге")

#///////////////////////////////////////////////////////////////////////////////////////////////////



def find_min(arr):
    if len(arr) == 0:
        return
    minimum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

array = list(map(int, input("Введите числа массива: ")))
print(find_min(array))


#///////////////////////////////////////////////////////////////////////////////////////////////////

def range_array(n):
    return list(range(1, n + 1))

n = int(input("Введите значение n: "))
if n > 0:
    arr = range_array(n)
    print(" ".join(map(str, arr)))  
else:
    print("Значение n должно быть больше 0.")

#///////////////////////////////////////////////////////////////////////////////////////////////////


def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

array = list(map(int, input("Введите числа массива через пробел: ").split()))
sum_number = sum_array(array)
print(sum_number)


#///////////////////////////////////////////////////////////////////////////////////////////////////

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
    
        for j in range(0, n - i - 1):
    
            if arr[j] > arr[j + 1]:
    
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = list(map(int, input("Введите числа массива через пробел: ").split()))
bubble_sort(array)
print("Отсортированный массив:", " ".join(map(str, array)))


#//////////////// задачи среденей сложности
number = int(input("Введите число: "))

if number % 2 == 0:
    print(f"{number} является четным числом.")
else:
    print(f"{number} является нечетным числом.")






