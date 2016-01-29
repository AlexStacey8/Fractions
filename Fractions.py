#Labsheet 8
#Intermediate question 2
class Fraction:


    def __init__(self,n,d):
        if type(n) == int:
            self.numerator = n
        elif n < 0:
            self.numerator = -n
        else:
            raise TypeError("The Numerator must be an integer")
        
        if (type(d) == int) and (d > 0):
            self.denominator = d
        elif d == 0:
            raise ZeroDivisionError("You cannot have zero as a denominator")
        elif d < 0:
            self.denominator = -d
        else:
            raise TypeError("The deniminator must be an integer")

    #Class method to simplify fractions, it works by finding the highest common factor
    #hcf = Higest common factor, given 2 number (x and y)
        
    def hcf(x,y):
        if y == 0:
            return(x)
        else:
            return(Fraction.hcf(y,x%y))#using the modules to find the remiander when x is divide by y

    #string method that will retirn the frcation in it simplified form

    def __str__(self):
        if self.numerator>0 and self.denominator>0:
            a = Fraction.hcf(self.numerator,self.denominator) #using the hcf method and assigning the value to a variable 'a'
            return(str(int(self.numerator/a)) + "/" + str(int(self.denominator/a)))
        
    #method to see if two fractions are equal

    def __eq__(self,fraction):
    #this form of assignment will be used through the code as it makes the methods eaiser to code. n1 = numerator one and d1 = denominator 1 and so on.
        
        n1 = self.numerator 
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator
        
    #if stament to test, returns a boolean

        if (n1*d2) == (n2*d1):
            return(True)
        else:
            return(False)
        
    #method to see if a fraction is less than another

    def __lt__(self,fraction):
        
    #variable assignment
        
        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator

    #converting the fractions into deciamal numbers so pyhton can proform the less than operator on the floats

        decimal1 = float(n1/d1)
        decimal2 = float(n2/d2)

    #if statement test, returns as boolean

        if decimal1 < decimal2:
            return(True)
        else:
            return(False)

    #method to see if a fraction is greater than another, same as less than code but the if statment
    #test is different (testing if the first desicaml is grater than the secound)

    def __gt__(self,fraction):

        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator

        decimal1 = float(n1/d1)
        decimal2 = float(n2/d2)

        if decimal1 > decimal2:
            return(True)
        else:
            return(False)

    #method to add fractions 

    def __add__(self,fraction):

        #variable assignment
        
        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator

        #calculations required so that I can add the fractions

        answerNumerator = (n1*d2) + (n2*d1)
        answerDenominator = (d1*d2)

        #using hcf method so it will return the fraction in it's simplist form

        a = Fraction.hcf(answerNumerator,answerDenominator)

        return(str(int(answerNumerator/a)) + "/" + str(int(answerDenominator/a)))



    #method for subtracting fractions
    def __sub__(self,fraction):
        
        #variable assignment
               
        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator
        
        #calculations required so that I can subtract the fractions
               
        answerNumerator = (n1*d2) - (n2*d1)
        answerDenominator = (d1*d2)

        #using hcf method so it will return the fraction in it's simplist form

        a = Fraction.hcf(answerNumerator,answerDenominator)

        return(str(answerNumerator/a) + "/" + str(answerDenominator/a))

    #Method for multipling

    def __mul__(self,fraction):

        #variable assignment

        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator

        #calculations required so that I can multiply the fractions

        answerNumerator = (n1*n2)
        answerDenominator = (d1*d2)

        #using hcf method so it will return the fraction in it's simplist form

        a = Fraction.hcf(answerNumerator,answerDenominator)

        return(str(answerNumerator) + "/" + str(answerDenominator))

    #Method for dividing

    def __truediv__(self,fraction):

        n1 = self.numerator
        d1 = self.denominator
        n2 = fraction.numerator
        d2 = fraction.denominator

        #calculations required so that I can divide the fractions

        answerNumerator = (n1*d2)
        answerDenominator = (d1*n2)

        #using hcf method so it will return the fraction in it's simplist form

        a = Fraction.hcf(answerNumerator,answerDenominator)

        return(str(answerNumerator/a) + "/" + str(answerDenominator/a))


        
