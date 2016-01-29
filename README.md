# Fractions
OOP skills shown through creating a Fraction class within Python

# Fractions
OOP example using Frcations
Project: Fractions

The goal of this project is to simpley allow the user to work with fractions within pythons
the code uses classes and the user can creat fraction as object of this class

Code was writen within python 3.5.0

when running the best method is to create your fraction by assigning them to a name such as fraction1

program was created based on instructions giving within the labsheet 8 on the 121COM module (included in respoistory)


contributor = Alexander Stacey

example of code
addition method:

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
        
        
        
  To get this to work within Python 3.5.0 shell all you need to do is this:
  
      fraction1 = Fraction(1,6) #creates a fraction and assigns it, in this example the fraction is 1/6
      fraction2 = Fraction(1,2)
  
      print(fraction1 + fraction2)
  
  
