def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] >= element and array[middle - 1] < element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

array = list(map(int, input().split()))
element = int(input())

sort(array)

left = 0
right = len(array)

try:
    binary_search(array, element, left, right)
except IndexError as error:
    print('Ты ввел_а неправильное число')
else:
    if binary_search(array, element, left, right) is False:
        print('Неправильно. Попробуй еще раз')
    else:
        print('Индекс элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу – ', binary_search(array, element, left, right))
