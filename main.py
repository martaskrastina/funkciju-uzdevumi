import math
skaitlis=float(input("Ievadi skaitli: "))
def decimaldala(skaitlis):
  s=int(skaitlis)
  rez=abs(skaitlis-s)
  return rez
def kvadrats(skaitlis):
  kv=math.pow(skaitlis,2)
  return kv
def sakne(skaitlis):
  if skaitlis>=0:
    sakne=math.sqrt(skaitlis)
  else:
    sakne="nav iespējama"
  return sakne
def zime(skaitlis):
  if skaitlis<0:
    zim="-"
  elif skaitlis==0:
    zim=0
  else:
    zim="+"
  return zim



print("Skaitļa decimāldaļa ir",decimaldala(skaitlis))
print("Skaitļa kvadrāts ir",kvadrats(skaitlis))
print("Skaitļa kvadrātsakne ir",sakne(skaitlis))
print("Skaitļa zīme ir",zime(skaitlis))