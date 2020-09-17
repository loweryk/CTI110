Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Assignment on Basic Math
SyntaxError: invalid syntax
>>> Assignment On Basic Math
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> #Assignment on Basic Math
>>> # # A brief description of the project
>>> 
>>> #Project that user inputs 2 numbers and then sums and multiplies both numbers
>>> 
>>> #September 17, 2020
>>> #CTI-110 P1HW2 - Basic Math
>>> #Kasey Lowery
>>> 
>>> #Ask user to enter the first number, assign it a proper name
>>> num1 = int(input('Enter the first number: '))
Enter the first number: 
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    num1 = int(input('Enter the first number: '))
ValueError: invalid literal for int() with base 10: ''
>>> num1 = int(input('Enter the first number: '))
Enter the first number: 2
>>> #ask user to enter the second number, assign it a proper name
>>> num2 = int(input('Enter the second number: '))
Enter the second number: 2
>>> #Add the two numbers
>>> sum = (num1 + num2)
>>> #Multiply the two numbers
>>> results = (num1 * num2)
>>> 
>>> #Display the folling:
>>> print('First Number Entered: ',num1)
First Number Entered:  2
>>> print('Second Number Entered: ',num2)
Second Number Entered:  2
>>> #Display Sum and Results
>>> print('Sum of both numbers: ',sum)
Sum of both numbers:  4
>>> print('Results of Multiplying the two numbers: ',results)
Results of Multiplying the two numbers:  4
>>> 