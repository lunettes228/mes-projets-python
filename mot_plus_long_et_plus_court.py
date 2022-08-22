# def reverse_string(x):
#     print(x[::-1])
    

# reverse_string("Comment tu va ?")

# x=["sam", "roger" , "ahlin", "solange","constance","ismael","jean","taofique"]
# print(f"le mot le plus long est: ",max(x,key=len))
# print(f"le mot le plus court est: ",min(x,key=len))

x=input("Ecrivez votre phrase: ")

def afficher_mot_min_et_mot_max(x):
    y=x.split()
    f=print("le mot le plus court est : ",min(y, key=len), "\nle mot le plus long est : ",max(y, key=len))
    return(f)
    

def afficher_mot_min_et_mot_max_par_ordre(x):
    y=x.split()
    f=[min(y, key=len),max(y, key=len)]
    f.sort()
    c=tuple(f)
    print(c)

afficher_mot_min_et_mot_max(x)

afficher_mot_min_et_mot_max_par_ordre(x)


