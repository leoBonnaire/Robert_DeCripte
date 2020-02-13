# -*- coding: utf-8 -*-

def dechiffre(chiffred, key):

  chiffred = chiffred.replace('*','')
  chiffred = chiffred.replace('X','')
  chiffred = chiffred.replace('#','')
  tabChiffre = [chiffred[i:i+5] for i in range(0, len(chiffred), 5)]  # Separate the text in an array
  tabKey = list(str(key))                                             # Same for the key
  tabChiffre = [int(i) for i in tabChiffre]                           # Convert to int
  tabKey = [int(i) for i in tabKey]
  size = int(tabChiffre[0] / 10)                                      # We take the size of the text
  tabChiffre.pop(0)                                                   # Then we delete the first index

  j = 0

  for i in tabChiffre:                                                # Delete the two last number of each instance
    tabChiffre[j] = int(tabChiffre[j] / 100)
    j += 1

  while len(tabKey) > len(tabChiffre): tabChiffre.append(0)           # Adjust the size of the text
  
  i = 0
  k = 1
  
  while len(tabKey) < len(tabChiffre):                                # Adjust the key to be the right size
    if i > len(tabKey): 
      i = 0
      k += 1
    value = int(tabKey[i] / k)
    tabKey.append(value)
    i += 1
  
  j = 0
  
  for i in tabKey:                                                    # Subtract the number of the key
    tabChiffre[j] -= 3*i
    j += 1
   
  while len(tabChiffre) > size:                                       # While the size is not corresponding, reduct the text
    j = 0
    for i in tabChiffre:
      if i <= 0: tabChiffre.pop(j)
      j += 1
  
  j = 0  

  for i in tabChiffre:                                                # Change the value by the letter
  
    if i == 32: tabChiffre[j] = ' '
    elif i == 33: tabChiffre[j] = '!'
    elif i == 34: tabChiffre[j] = '"'
    elif i == 35: tabChiffre[j] = '#'
    elif i == 36: tabChiffre[j] = '$'
    elif i == 37: tabChiffre[j] = '%'
    elif i == 38: tabChiffre[j] = '&'
    elif i == 39: tabChiffre[j] = '\''
    elif i == 40: tabChiffre[j] = '('
    elif i == 41: tabChiffre[j] = ')'
    elif i == 42: tabChiffre[j] = '*'
    elif i == 43: tabChiffre[j] = '+'
    elif i == 44: tabChiffre[j] = ','
    elif i == 45: tabChiffre[j] = '-'
    elif i == 46: tabChiffre[j] = '.'
    elif i == 47: tabChiffre[j] = '/'
  
    elif i == 48: tabChiffre[j] = '0'
    elif i == 49: tabChiffre[j] = '1'
    elif i == 50: tabChiffre[j] = '2'
    elif i == 51: tabChiffre[j] = '3'
    elif i == 52: tabChiffre[j] = '4'
    elif i == 53: tabChiffre[j] = '5'
    elif i == 54: tabChiffre[j] = '6'
    elif i == 55: tabChiffre[j] = '7'
    elif i == 56: tabChiffre[j] = '8'
    elif i == 57: tabChiffre[j] = '9'
    
    elif i == 58: tabChiffre[j] = ':'
    elif i == 59: tabChiffre[j] = ';'
    elif i == 60: tabChiffre[j] = '<'
    elif i == 61: tabChiffre[j] = '='
    elif i == 62: tabChiffre[j] = '>'
    elif i == 63: tabChiffre[j] = '?'
    elif i == 64: tabChiffre[j] = '@'

    elif i == 65: tabChiffre[j] = 'A'
    elif i == 66: tabChiffre[j] = 'B'
    elif i == 67: tabChiffre[j] = 'C'
    elif i == 68: tabChiffre[j] = 'D'
    elif i == 69: tabChiffre[j] = 'E'
    elif i == 70: tabChiffre[j] = 'F'
    elif i == 71: tabChiffre[j] = 'G'
    elif i == 72: tabChiffre[j] = 'H'
    elif i == 73: tabChiffre[j] = 'I'
    elif i == 74: tabChiffre[j] = 'J'
    elif i == 75: tabChiffre[j] = 'K'
    elif i == 76: tabChiffre[j] = 'L'
    elif i == 77: tabChiffre[j] = 'M'
    elif i == 78: tabChiffre[j] = 'N'
    elif i == 79: tabChiffre[j] = 'O'
    elif i == 80: tabChiffre[j] = 'P'
    elif i == 81: tabChiffre[j] = 'Q'
    elif i == 82: tabChiffre[j] = 'R'
    elif i == 83: tabChiffre[j] = 'S'
    elif i == 84: tabChiffre[j] = 'T'
    elif i == 85: tabChiffre[j] = 'U'
    elif i == 86: tabChiffre[j] = 'V'
    elif i == 87: tabChiffre[j] = 'W'
    elif i == 88: tabChiffre[j] = 'X'
    elif i == 89: tabChiffre[j] = 'Y'
    elif i == 90: tabChiffre[j] = 'Z'
    
    elif i == 97: tabChiffre[j] = 'a'
    elif i == 98: tabChiffre[j] = 'b'
    elif i == 99: tabChiffre[j] = 'c'
    elif i == 100: tabChiffre[j] = 'd'
    elif i == 101: tabChiffre[j] = 'e'
    elif i == 102: tabChiffre[j] = 'f'
    elif i == 103: tabChiffre[j] = 'g'
    elif i == 104: tabChiffre[j] = 'h'
    elif i == 105: tabChiffre[j] = 'i'
    elif i == 106: tabChiffre[j] = 'j'
    elif i == 107: tabChiffre[j] = 'k'
    elif i == 108: tabChiffre[j] = 'l'
    elif i == 109: tabChiffre[j] = 'm'
    elif i == 110: tabChiffre[j] = 'n'
    elif i == 111: tabChiffre[j] = 'o'
    elif i == 112: tabChiffre[j] = 'p'
    elif i == 113: tabChiffre[j] = 'q'
    elif i == 114: tabChiffre[j] = 'r'
    elif i == 115: tabChiffre[j] = 's'
    elif i == 116: tabChiffre[j] = 't'
    elif i == 117: tabChiffre[j] = 'u'
    elif i == 118: tabChiffre[j] = 'v'
    elif i == 119: tabChiffre[j] = 'w'
    elif i == 120: tabChiffre[j] = 'x'
    elif i == 121: tabChiffre[j] = 'y'
    elif i == 122: tabChiffre[j] = 'z'
    
    elif i == 128: tabChiffre[j] = 'é'
    elif i == 129: tabChiffre[j] = 'è'
    elif i == 130: tabChiffre[j] = 'à'
    elif i == 131: tabChiffre[j] = 'ù'

    elif i == 132: tabChiffre[j] = '\n'

    else: tabChiffre[j] = '?'
    
    j += 1
  
  final = ''

  for i in tabChiffre:                                                # Put the array into a string
    final += i
  
  return final
  
def translate(text):
  text = text.replace('#', '')
  text = text.replace('*', '')
  tabText = [text[i:i+2] for i in range(0, len(text), 2)]
  j = 0
  final = ''
  for i in tabText:
    i = int(i)
    if i == 35: tabText[j] = '#'
    elif i == 42: tabText[j] = '*'
    elif i == 48: tabText[j] = '0'
    elif i == 49: tabText[j] = '1'
    elif i == 50: tabText[j] = '2'
    elif i == 51: tabText[j] = '3'
    elif i == 52: tabText[j] = '4'
    elif i == 53: tabText[j] = '5'
    elif i == 54: tabText[j] = '6'
    elif i == 55: tabText[j] = '7'
    elif i == 56: tabText[j] = '8'
    elif i == 57: tabText[j] = '9'
    elif i == 88: tabText[j] = 'X'
    else: tabText[j] = '?'
    final += tabText[j]
    j += 1
  return final
