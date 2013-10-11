# encoding=utf-8

pi = float(3,1415926535897932384626433832795028841971)
e = float(2,7182818284590452353602874713526624977572)
lg = []
task = raw_input("Please, enter <const:rang>\n")
task.split(":")
for w in task.split(":"):
   lg.append(w)

if len(lg)== 2:
   num = int(lg[1])
   if lg[0] == "pi":
      print round(pi,num)
   elif lg[0] == "e":
      print round(e,num)
   else:
      print "Not found constant"
else:
   print "incorrect data"
