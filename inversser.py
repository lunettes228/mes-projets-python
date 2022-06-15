# def reverse_string(x):
#     print(x[::-1])
    

# reverse_string("Comment tu va ?")

# x=["sam", "roger" , "ahlin", "solange","constance","ismael","jean","taofique"]
# print(f"le mot le plus long est: ",max(x,key=len))
# print(f"le mot le plus court est: ",min(x,key=len))

x="Aujourd'hui il ne fait pas beau mais bon j'ai envie d'un bon c"

def afficher_mot_min_et_mot_max(x):
    y=x.split()
    print("le mot le plus court est : ",min(y, key=len))
    print("le mot le plus long est : ",max(y, key=len))
    
afficher_mot_min_et_mot_max(x)
