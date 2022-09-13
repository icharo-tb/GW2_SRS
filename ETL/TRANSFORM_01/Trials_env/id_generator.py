import random

numbers = '1234567890'
letters = 'abcdefghijklmnopqrstuvwxyz'

chars = numbers + letters

id_lines = random.sample(chars,10)
print(''.join(id_lines))

#import the necessary modules !
import random
import string
print ( ' hello , Welcome to Password generator ! ' )
#input the length of password
length = int ( input ( ' \ nEnter the length of password : ' ) )
#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#combine the data
all = lower + upper + num + symbols
#use random
temp = random.sample ( all , length )
#create the password
password = " " .join ( temp )
#print the password
print ( password )