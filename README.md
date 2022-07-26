###  ! Запуск производить из файла `main.py`, предварительно установив зависимости из `requirements.txt` !
###  ! Решение находится в файле `solution.py`!
# Тестовое задание для отклика компании Lesta Studio

## Задание 1

##### Реализовано ещё две функции определения четности целого числа:
1. С помощью целочисленного и обычного деления (value // 2 == value / 2)
2. С помощью операции побитового сравнения (value & 1 == 0)

Мы используем побитовое сравнение с 1, что фактически
равняется проверки последнего бита числа, и если он равен нулю - число четное, в противном случае нечетное.
Использование целочисленного и обычного деления же работает медленнее всего, так как мы запускаем сразу две
операции вместо одной.
##### На мой взгляд плюсом использование функции c % является то, что её проще воспринимать в коде. Минус - в общем случае, не такая быстрая как побитовое сравнение.

##### Функция с использованием операции & быстрее в основном работает чуть быстрее, но сложнее для понимания, если вам трудно переводить числа в двоичную систему.
##### У функции же value // 2 == value / 2 плюсов нет.
### Код:


```python
def is_even_opt_1(value):
    return value % 2 == 0

def is_even_opt_2(value):
    return value // 2 == value / 2

def is_even_opt_3(value):
    return value & 1 == 0
```

## Задание 2

#####   Реализовать минимум по 2 класса реализовывающих циклический буфер FIFO

CircularQueueOpt1 самая простая реализация из представленных – при инициализации создается лист с заданным размером и заполняется типом None. В последствии при добавлении элемента, первый просто удаляется, а в конец добавляется новый элемент.   Плюсом является лаконичность кода, и, пожалуй, всё.  Минусы – отсутствие возможности динамически получать очередь без None элементов. Медленные операции add – O(n) и pop – O(n). Отсутствие исключения переполненной очереди.

CircularQueueOpt2 реализация лучше - при инициализации создается очередь, заполненная None, с заданной вместимостью, инициализируются атрибуты tail и head для корректной работы методов add и pop. Из плюсов можно выделить динамическое получение не до конца заполненной очереди, быстрые операции add – O (1) и pop – O (1). 

CircularQueueOpt3 реализация, немного отличающаяся от предыдущей -  при инициализации создается атрибут max, который отвечает за корректную работу метода add. В этой реализации до того, как все элементы будут заполнены используются методы класса CircularQueueOpt3. После того как все элементы будут заполнены объект будет переопределён в объект приватного класса __Complete. После этого методы будут работать иначе. Из плюсов можно выделить динамическое получение не до конца заполненной очереди, быструю операцию после заполнения add – O (1). Из минусов – медленная операция до заполнения add – O(N) и отсутствие операции pop. Отсутствие исключения пустой или переполненной очереди.

### Код:
```python
class CircularQueueOpt1:
    def __init__(self, size):
        self.data = [None for _ in range(size)]

    def add(self, item):
        self.data.pop(0)
        self.data.append(item)

    def pop(self):
        item = self.data.pop(0)
        self.data.append(None)
        return item

    def get(self):
        return self.data


class CircularQueueOpt2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def add(self, item):
        if self.size == self.capacity:
            print("Error : Queue is Full")
            # raise Exception
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item
            self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            print("Error : Queue is Empty")
            return None
        else:
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
        return tmp

    def get(self):
        if self.size == 0:
            print("Queue is Empty \n")
        else:
            tmp = []
            index = self.head
            for i in range(self.size):
                tmp.append(self.queue[index])
                index = (index + 1) % self.capacity
            return tmp


class CircularQueueOpt3:

    def __init__(self, size_max):
        self.cur = None
        self.max = size_max
        self.data = []

    class __Complete:
        def __init__(self):
            self.max = None
            self.data = None
            self.cur = None

        def add(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur + 1) % self.max

        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def add(self, item):
        self.data.append(item)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Complete

    def get(self):
        return self.data
```

## Задание 3

#####  Реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).

Честно говоря, с заданными параметрами лучшей сортировки просто не существует, все хорошие сортировки работают в среднем за 0(n log n). Была реализована функция быстрой сортировки, но с тем же результатом можно запустить встроенные в питон функции сортировки, и получить примерно такой же результат. Я выбрал её просто потому что мне нравится стратегия «разделяй и властвуй», и эта сортировка хорошо описана в «Грокаем Алгоритмы» Бхаргава Адитья, которую было невероятно интересно читать =).
 Сортировку стоит выбирать исходя из специфики конкретного случая. 

### Код:
```python
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
```

# Текст тестового задания:
Данное задание призвано оценить работу с Python, уровень владения культурой программирования, а также показать пример того, с чем придется столкнуться в работе. Несмотря на это, данные в задании имеют очень упрощенную схему относительно реальных.

### Задание:

1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
2. Python example:
```
  def isEven(value):return value%2==0
```
2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.
