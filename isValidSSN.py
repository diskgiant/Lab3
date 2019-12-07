#!/usr/bin/python3

def isValidSSN(ss):
  for e in [ ss[:3] , ss[4:6] , ss[7:] ]:
    print(e)
    if not e.isdigit():
      return False
  for e in [ ss[3], ss[6] ]:
    if e != '-':
      return False
  return True


