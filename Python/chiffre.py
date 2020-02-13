# -*- coding: utf-8 -*-

from random import *

def chiffre(texte, key):

  tabKey = [int(i) for i in str(key)]                                   # Transform the key and the text in array
  tabTexte = [str(i) for i in texte]
  
  j = 0
  
  for i in tabTexte:                                                    # Replace each letter by a number
  
    if i == ' ': tabTexte[j] = 32
    elif i == '!': tabTexte[j] = 33
    elif i == '"': tabTexte[j] = 34
    elif i == '#': tabTexte[j] = 35
    elif i == '$': tabTexte[j] = 36
    elif i == '%': tabTexte[j] = 37
    elif i == '&': tabTexte[j] = 38
    elif i == '\'': tabTexte[j] = 39
    elif i == '(': tabTexte[j] = 40
    elif i == ')': tabTexte[j] = 41
    elif i == '*': tabTexte[j] = 42
    elif i == '+': tabTexte[j] = 43
    elif i == ',': tabTexte[j] = 44
    elif i == '-': tabTexte[j] = 45
    elif i == '.': tabTexte[j] = 46
    elif i == '/': tabTexte[j] = 47

    elif i == '0': tabTexte[j] = 48
    elif i == '1': tabTexte[j] = 49
    elif i == '2': tabTexte[j] = 50
    elif i == '3': tabTexte[j] = 51
    elif i == '4': tabTexte[j] = 52
    elif i == '5': tabTexte[j] = 53
    elif i == '6': tabTexte[j] = 54
    elif i == '7': tabTexte[j] = 55
    elif i == '8': tabTexte[j] = 56
    elif i == '9': tabTexte[j] = 57
    
    elif i == ':': tabTexte[j] = 58
    elif i == ';': tabTexte[j] = 59
    elif i == '<': tabTexte[j] = 60
    elif i == '=': tabTexte[j] = 61
    elif i == '>': tabTexte[j] = 62
    elif i == '?': tabTexte[j] = 63
    elif i == '@': tabTexte[j] = 64
  
    elif i == 'A': tabTexte[j] = 65
    elif i == 'B': tabTexte[j] = 66
    elif i == 'C': tabTexte[j] = 67
    elif i == 'D': tabTexte[j] = 68
    elif i == 'E': tabTexte[j] = 69
    elif i == 'F': tabTexte[j] = 70
    elif i == 'G': tabTexte[j] = 71
    elif i == 'H': tabTexte[j] = 72
    elif i == 'I': tabTexte[j] = 73
    elif i == 'J': tabTexte[j] = 74
    elif i == 'K': tabTexte[j] = 75
    elif i == 'L': tabTexte[j] = 76
    elif i == 'M': tabTexte[j] = 77
    elif i == 'N': tabTexte[j] = 78
    elif i == 'O': tabTexte[j] = 79
    elif i == 'P': tabTexte[j] = 80
    elif i == 'Q': tabTexte[j] = 81
    elif i == 'R': tabTexte[j] = 82
    elif i == 'S': tabTexte[j] = 83
    elif i == 'T': tabTexte[j] = 84
    elif i == 'U': tabTexte[j] = 85
    elif i == 'V': tabTexte[j] = 86
    elif i == 'W': tabTexte[j] = 87
    elif i == 'X': tabTexte[j] = 88
    elif i == 'Y': tabTexte[j] = 89
    elif i == 'Z': tabTexte[j] = 90
    
    elif i == 'a': tabTexte[j] = 97
    elif i == 'b': tabTexte[j] = 98
    elif i == 'c': tabTexte[j] = 99
    elif i == 'd': tabTexte[j] = 100
    elif i == 'e': tabTexte[j] = 101
    elif i == 'f': tabTexte[j] = 102
    elif i == 'g': tabTexte[j] = 103
    elif i == 'h': tabTexte[j] = 104
    elif i == 'i': tabTexte[j] = 105
    elif i == 'j': tabTexte[j] = 106
    elif i == 'k': tabTexte[j] = 107
    elif i == 'l': tabTexte[j] = 108
    elif i == 'm': tabTexte[j] = 109
    elif i == 'n': tabTexte[j] = 110
    elif i == 'o': tabTexte[j] = 111
    elif i == 'p': tabTexte[j] = 112
    elif i == 'q': tabTexte[j] = 113
    elif i == 'r': tabTexte[j] = 114
    elif i == 's': tabTexte[j] = 115
    elif i == 't': tabTexte[j] = 116
    elif i == 'u': tabTexte[j] = 117
    elif i == 'v': tabTexte[j] = 118
    elif i == 'w': tabTexte[j] = 119
    elif i == 'x': tabTexte[j] = 120
    elif i == 'y': tabTexte[j] = 121
    elif i == 'z': tabTexte[j] = 122
    
    elif i == 'é': tabTexte[j] = 128
    elif i == 'è': tabTexte[j] = 129
    elif i == 'à': tabTexte[j] = 130
    elif i == 'ù': tabTexte[j] = 131

    elif i == '\n': tabTexte[j] = 132

    else: tabTexte[j] = 255
    
    j += 1
    
  i = 0
  k = 1
  
  while len(tabKey) < len(tabTexte):                                     # Adjust the size of the key to have the same length
    if i > len(tabKey): 
      i = 0
      k += 1
    value = int(tabKey[i] / k)
    tabKey.append(value)
    i += 1
    
  while len(tabKey) > len(tabTexte): tabTexte.append(0)                  # Adjust the size of the text to have the same length
    
  j = 0
  i = 0
  final = ''
  
  for i in tabKey:
    if tabTexte[j] == 0: break
    tabTexte[j] += 3*i                                                  # Add the key and the numbers of the text
    tabTexte[j] = str(tabTexte[j])
    while len(tabTexte[j]) < 3: tabTexte[j] = '0' + tabTexte[j]         # Make each number made of 3 by adding 0
    final += tabTexte[j] +'X'+ str(randint(0,9)) + str(randint(0,7))    # Add 2 random numbers after this and make a string
    j += 1
  
  size = str(len(texte))
  while len(size) < 4: size = '0' + size                                 # Adjust the size to be made of 5 numbers
  size += str(randint(0,9))

  final = '#' + size + final + '*'                                       # Add the size to the text
  return final                                                           # Then return
