# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import time - for method8
import Complex
import Methods



if __name__ == "__main__":

    # obj1 = Complex.Complex(2, -5)
    # obj2 = Complex.Complex(3, 10)

    def switchMethod(argument):

        switcher = {
            1: Methods.sum(122, 2),       #return int method
            2: Methods.difference(5, 2),        #return difference
            3: Methods.remainder(11, 12),        #return double method
            4: Methods.division(10, 5),
            5: Complex.sumComplex_numbers(Complex.Complex(30,-5), Complex.Complex(2, 10)),          #method that sums up 2 Complex numbers
            6: Complex.subComplex_numbers(Complex.Complex(2,10), Complex.Complex(4,-10)),           #method that substracts 2 Complex numbers
            7: Complex.modulusComplex_numbers(),                             #method that calculates modulus of a Complex number
            8: Methods.power(44, 4),           #read from a file and display
            9: Methods.power_from_file("file.txt"),               #power method from file
            10: Methods.random_list_generator(10),               #method that obtains a random list
            11: Methods.rangedListFabric(15),            #builds an increasing list of <argument> elements (starting from 10)
            12: Methods.random_generator_and_selection_sort(5),          #poor method of sorting - selection sort
            13: Methods.random_generator_and_quicksort(6),       #better method to sort - quick sort
            14: Methods.timer_function_quicksort(20),                         #method to quantify the elapsed time after sorting a random list - quick sort
            15: Methods.timer_function_selection_sort(20),                      #method to quantify the elapsed time after sorting a random list - selection sort
            16: Methods.phoneValidator("+40775219705"),           #validate phone number
            17: 'none here'


        }
        func = switcher.get(argument, "Invalid choice")
        print(func)

    #write numbers in a file ---> this function will take longer
    # def method8():
    #     start = time.time()
    #     f = open("tests.txt", "w")
    #     for i in range(0,20000000):
    #         f.write(str(i))
    #     f.close()
    #     end = time.time()
    #     return (str(end - start) + " seconds")


#format the + or - signs and display 2 Complex numbers    ---> used to test the fullnumber() method
    # def sumComplex():
    #     obj1 = complex_class_factoring(2, -10)
    #     obj2 = complex_class_factoring(-5, 13)
    #     return obj1.fullnumber() + "\n" + obj2.fullnumber()


    while(input):
        try:
            mode = int(input("\n1-Sum\n2-Difference\n3-Remainder\n4-Divison\n5-Sum of complex numbers\n6-Difference of complex numbers\n7-Modulus of complex numbers\n8-Power\n9-Power from file\n10-Random list generator\n11-Increasing fixed list fabric\n12-Random list and selection sort\n13-Random list and quick sort\n14-Quick sort time performance\n15-Selection sort time performance\n16-Phone validator\nChoose a number: "))
            switchMethod(mode)

        except ValueError:
            print("Oooops try again but with a number this time -.-")



#license and credits to vpirciulescu.github.com