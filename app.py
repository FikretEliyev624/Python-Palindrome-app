#Program-1

str = 'JaVaJa'  
strstr = str.casefold()  

rev = reversed(str)  
  
if list(str) == list(rev):  
   print("PALINDROME !")  
else:  
   print("NOT PALINDROME !")  

#Program-2

string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")  