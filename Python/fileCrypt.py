#!/usr/bin/python3
# -*- coding: utf-8 -*-

from key import *
from chiffre import *
from dechiffre import *

fileToCrypt = input('Write the file full name : ')
f = open(fileToCrypt, 'r')
fc = open(("C"+fileToCrypt), 'w')

for i in f:
  fc.write(chiffre(i, 134))
  
print('Your file has been crypted.')
