global Animals
Animals = []

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
 ArrayLength = len(Animals)
 for x in range(ArrayLength - 1):
     for y in range(ArrayLength - x - 1):
          if Animals[y][0] < Animals[y+1][0]:
              Temp = Animals[y]
              Animals[y] = Animals[y + 1]
              Animals[y + 1] = Temp

SortDescending()
for i in Animals:
    print(i)
