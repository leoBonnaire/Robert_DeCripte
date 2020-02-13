#!/usr/bin/python3
# -*- coding: utf-8 -*-

from key import *
from chiffre import *
from dechiffre import *

fileToCrypt = input('Write the file full name : ')
f = open(fileToCrypt, 'r')
  
for i in f:
  print(dechiffre(i, 134))
