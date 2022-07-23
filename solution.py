import time


# Задание 1

def time_of_funct(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res

    return wrapped


@time_of_funct
def is_even_opt_1(value):
    return value % 2 == 0


@time_of_funct
def is_even_opt_2(value):
    return value // 2 == value / 2


@time_of_funct
def is_even_opt_3(value):
    return value & 1 == 0


# Задание 2
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


# Задание 3
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

@time_of_funct
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
