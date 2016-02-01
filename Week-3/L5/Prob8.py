def isIn(char, aStr):

   # Base Cases
   if aStr == '':
      return False

   if len(aStr) == 1:
      return (aStr == char)

  # Getting the nid value
   mid = len(aStr)/2
   midChar = aStr[mid]
   if (char == midChar):
      return True
   
  # Recuring Call .
   elif (char < midChar):
      return isIn(char, aStr[:mid])

   else:
      return isIn(char, aStr[mid+1:])
