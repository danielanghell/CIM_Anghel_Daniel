import time

import phonenumbers
import random
import timeit
import math
import os

if __name__ == "__main__":
    print("executed as main")
else:

    #sum
    def sum(number1, number2):
        sum = number1 + number2
        return sum

    #rest
    def remainder(number1, number2):
        try:
            if number2 == 0:
                throwing_error()
            else:
                return int(number1 % number2)
        except ZeroDivisionError:
            return "divisor is less than 1"


    #division
    def division(number1, number2):
        try:
            if number2 == 0:
                throwing_error()
            else:
                return int(number1 / number2)
        except ZeroDivisionError:
            return "divisor is less than 1"


    #difference
    def difference(number1, number2):
        diff = number1 - number2
        return diff

    #raise Exception for asserRaises tests
    def throwing_error():
        raise Exception

    #power
    def power(b, p):
        try:
            if b == p == 0 or b < 0 or p < 0:
                throwing_error()
            else:
                return int(math.pow(int(b), int(p)))
        except OverflowError:
            throwing_error()
            return "too big number"     #I guess this is not reachable



    # write to file 2 numbers each on a different line
    def writing_to_file(path, b, p):
        f = open(path, "w")
        f.write(str(b) + '\n')
        f.write(str(p) + '\n')
        f.close()
        pass

        # try:
        #     return math.pow(b, p)
        # except OverflowError:
        #     return "too big number"

    #read from a file
    def power_from_file(path):
        try:
            if os.path.isfile(path):
                f = open(path, "r")
                numbers = verify_file(path)
                base = int(numbers[0])          #"integarize" the elements, otherwise they are str type
                power = int(numbers[1])
                if base == power == 0 or base < 0 or power < 0:     #check for corner cases
                    throwing_error()
                else:
                    return int(math.pow(base, power))
            else:
                throwing_error()

        except OverflowError:
            throwing_error()
            return "too big number"
        finally:
            f.close()

    #verify if there are only digits on the file + stripping the \n character
    def verify_file(path):
        try:
            f = open(path, "r")
            numbers = []
            for number in f:
                number = number.rstrip()   #strip \n
                numbers.append(number)     #form the list
            for number in numbers:
                if number.isdigit() == True:
                    pass
                else:
                    throwing_error()
            return numbers
        finally:
            f.close()





    # def power_from_file():
    #     f = open("file.txt", "r")
    #     for line in f:
    #         line = line.rstrip()
    #     return line

    def raise_number_parse_exception():
        raise phonenumbers.NumberParseException


    #verify a string
    def phoneValidator(phone_number):
        phone_number_parsed = phonenumbers.parse(phone_number)
        if phonenumbers.is_possible_number(phone_number_parsed) == True:
            return True
        else:
            raise Exception


    #working with values from a defined range --- build an increasing list of a fixed length
    def rangedListFabric(number):
        list = [*range(int(number))]
        for i in list:
            list[i] = list[i]+10
        return list


    #poor sorting alghortim ----> selection sort
    def random_generator_and_selection_sort(values):
        argument = random_list_generator(values)
        for i in range(len(argument)):
            min_idx = i
            for j in range(i + 1, len(argument)):
                if argument[min_idx] > argument[j]:
                    min_idx = j
            argument[i], argument[min_idx] = argument[min_idx], argument[i]
        return argument

    #poor sorting alghortim ----> selection sort -----> passing a list instead of value
    def selection_sort_list(list):
        argument = list
        for i in range(len(argument)):
            min_idx = i
            for j in range(i + 1, len(argument)):
                if argument[min_idx] > argument[j]:
                    min_idx = j
            argument[i], argument[min_idx] = argument[min_idx], argument[i]
        return argument


    def partition(start, end, array):
        # Initializing pivot's index to start
        pivot_index = start
        pivot = array[pivot_index]

        while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            if (start < end):
                array[start], array[end] = array[end], array[start]
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return end


    def quick_sort(start, end, array):
        if (start < end):
            p = partition(start, end, array)
            quick_sort(start, p - 1, array)
            quick_sort(p + 1, end, array)
        return array


    #generate random list and sort it with quicksort - no shit sherlock
    def random_generator_and_quicksort(argument):
        list = random_list_generator(argument)
        return quick_sort(0, len(list)-1, list)

    def random_list_generator(argument):
        list = random.sample(range(10, 100), argument)
        return list


    #measure time elapsed when sorting a list
    def timer_function_quicksort(argument):
        start = timeit.timeit()
        random_generator_and_quicksort(argument)
        end = timeit.timeit()
        dif = start - end
        if dif < 0:
            dif = dif * (-1)
        return dif

    def timer_function_selection_sort(argument):
        start = timeit.timeit()
        random_generator_and_selection_sort(argument)
        end = timeit.timeit()
        dif = start - end
        if dif < 0:
            dif = dif * (-1)
        return dif

    #pass a list as argument and sort with quicksort ---- maybe for future purposes
    def quick_sort_list(list):
        return quick_sort(0, len(list)-1, list)
