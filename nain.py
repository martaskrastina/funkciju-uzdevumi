ter=input("Ievadi līguma teriņu: ")
iepr=float(input("Ievadi iepriekšējo skaitītāja rādījumu: "))
esosais=float(input("Ievadi esošo skaitītāja rādījumu: "))
gads1=0.20159
gads2=0.16961
gads3=0.16427
gads4=0.15964
def kilovati(iepr,esosais):
  kw=esosais-iepr
  return kw
def rekins(ter,kw):
  if ter==1:
    summa=kw*gads1
  elif ter==2:
    summa=kw*gads2
  elif ter==3:
    summa=kw*gads3
  else:
    summa=kw*gads4
  return summa

print("Patērēti",kilovati(iepr,esosais),"kW")
print("Maksājuma summa ir",round(rekins(ter,kilovati(iepr,esosais)),2),"eiro")