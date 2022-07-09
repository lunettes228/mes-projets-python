def inverser_chaine(l):
    print(f"voici le mot en entier: {l}")
    l_reverse=""
    i=len(l)-1
    for n in l:
        l_reverse+=l[i]
        i-=1
            
    print(f"voici le mot inversé: {l_reverse}")