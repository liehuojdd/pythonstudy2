def printme(str):
    print("here is ",str)
    return

def printinfo( arg1, *vartuple ):
   print ("arg is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

printme("abc")
printinfo( 10 )
printinfo( 70, 60, 50 )