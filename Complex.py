import math
import main

if __name__ == "__main__":
    print("executed as main")
else:

    class Complex:
        def __init__(self, real, img):
            self.real = real
            self.img = img

        def fullnumber(self):
            if self.real >= 0:
                if self.img >= 0:
                    return str(self.real) + " + j" + str(self.img)
                else:
                    stripping = str(self.img)
                    stripping = stripping.lstrip('-')
                    return str(self.real) + " - j" + stripping
            else:
                if self.img >= 0:
                    return str(self.real) + " + j" + str(self.img)
                else:
                    stripping = str(self.img)
                    stripping = stripping.lstrip('-')
                    return str(self.real) + " - j" + stripping


    #overload the + operator
        def __add__(self, other):
            result_real = self.real + other.real
            restul_img = self.img + other.img
            return Complex(result_real, restul_img)


    #overload the - operator
        def __sub__(self, other):
            result_real = self.real - other.real
            result_img = self.img - other.img
            return Complex(result_real, result_img)


    #modulus calculus
        def modulus(self):
            real = self.real
            img = self.img
            return math.floor((math.sqrt(pow(real,2) + pow(img, 2))))


    #fabric of Complex numbers
    def complex_class_factoring(real, img):
        obj = Complex(real, img)
        return obj

            # add Complex numbers
    def sumComplex_numbers(self, other):
        # obj1 = complex_class_factoring(3, -5)
        # obj2 = complex_class_factoring(2, 10)
        obj1 = self
        obj2 = other
        return (obj1 + obj2).fullnumber()


    #substract Complex numbers
    def subComplex_numbers(self, other):
        # obj1 = complex_class_factoring(2,10)
        # obj2 = complex_class_factoring(4,-10)
        obj1 = self
        obj2 = other
        return (obj1 - obj2).fullnumber()

    #modulus of Complex numbers
    def modulusComplex_numbers():
        obj1 = complex_class_factoring(5,4)
        return obj1.modulus()




