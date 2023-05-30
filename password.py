import random

from typing import List

print('Welcome')
password_contents_symbols = ('!','@', '#', '$', '%', '^', '&', '*', '(', ')','.',',',';','`','+',';','[',']','{','}','<','>')
password_contents_numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
                             )
password_contents_letters = ('Q', 'W','E', 'b', 'y', 'M', 'I', 's', 'D', 'F', 'U', 'J', 'W', 'C', 'V',
                             'G', 'B', 'N', 'A', 'P', 'L', 'S', 'E', 'L', 'x', 'Z','z','k', 'v','l','i','o','g','L','B')



for i in range(10):

  password = ''
  letter = random.choice(password_contents_letters)
  symbol = random.choice(password_contents_symbols)
  numbers = random.choice(password_contents_numbers)
  password += letter+symbol+numbers
  passwordnew = ''.join(random.sample(password,len(password)))
  passwordlist = list(passwordnew)
  passwordlist.pop()

  print(''.join(passwordlist), end='')

