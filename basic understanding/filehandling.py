# f= open("Hello.txt","w")
# f.write("hello, my name is manthan\n")
# f.write("and this is my first file handlaing programe")
# print(type(f))
# f.close()
try:
  f= open("basic understanding\\Hello.txt","r")  
  content=f.read(5)  # it read first 5 alphabet
  print(content)
  content=f.read(5)
  print(content)
  f.seek(5)   # to move curser at position 5
  content=f.read()  
  print(content)
except:
  print("file not find")
  f.close()
  
 