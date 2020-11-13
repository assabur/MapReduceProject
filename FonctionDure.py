# fonction qui recherche toutes les durees dappel dun num de tel dans le fichier call
# return un tableau contenant les differentes durees dans un tableau
def userDuree(tel):
    fichier = open("calls.txt", "r")
    tableau =[]
    for tuple in fichier:
      Line = tuple.strip()
      Line = tuple.split(",")
      for values in Line :
          if tel in values:
            tableau.append(Line[2].strip())
    #print(len(tableau))
    return tableau


