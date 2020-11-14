# fonction qui recherche toutes les durees dappel dun num de tel dans le fichier call
# return un tableau contenant les differentes durees dans un tableau
def userDuree(tel):
    fichier = open("calls.txt", "r")
    tableau =[]
    TotalDure = 0
    for tuple in fichier:
      Line = tuple.strip()
      Line = tuple.split(",")
      for values in Line :
          if tel in values:
            dure = int(Line[2].strip())
            tableau.append(dure)
            TotalDure+= dure
    #print(len(tableau))
    return round(TotalDure/len(tableau),2)


