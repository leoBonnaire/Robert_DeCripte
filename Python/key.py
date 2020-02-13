import time

def generateKey(tem=time.time()):               # Use the timestand as default key

  key0 = 1
  key1 = int(int(tem) / 100)
  key2 = int(key1 * key1 / 1337)
  digits = [int(i) for i in str(key2)]
  if len(digits) % 2 == 1: digits.append(7)
  for i in digits:
    if i != 0 and i != 1 :
      key0 *= i
  key0 *= key1
  return key0
