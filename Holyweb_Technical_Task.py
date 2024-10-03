def my_range(stop_num):
    start_num = 0
    while start_num < stop_num:
        yield start_num
        start_num += 1


odd_numbers = [x for x in my_range(20) if x % 2!= 0]
print(odd_numbers)

odd_numbers_2 = list(filter(lambda x: x % 2 != 0, my_range(20)))
print(odd_numbers_2)


class MyRange:
    def __iter__(self):
        pass

    def __next__(self):
        pass
