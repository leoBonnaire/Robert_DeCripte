#!/usr/bin/python3
# -*- coding: utf-8 -*-

from key import *
from chiffre import *
from dechiffre import *

while 1:
  texte = input('Texte à chiffrer : ')
  if texte == 'quit': break
  key = generateKey(987654321)                  # Create the key
  texteChiffre = chiffre(texte, key)            # Crypte the message
  print('Texte chiffé : ' + str(texteChiffre))
  texteDechiffre = dechiffre(texteChiffre, key) # Decrypte the message
  print('Texte déchiffré : '+str(texteDechiffre))
