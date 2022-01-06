nr=int(input("Ievadi nedēļas dienas nummuru: "))
def diena(nr):
  ned=["pirmdiena","otrdiena","trešdiena","ceturtdiena","piektdiena","sestdiena","svētdiena"]
  return ned[nr-1]
print(diena(nr))
