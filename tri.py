
def tri_par_insertion(l):
    n=len(l)
    print(f"unsorted liste: {l}".upper())
    for i in range(1,n):
        cle=l[i]
        j=i-1
        while j>=0 and l[j]>cle:
            l[j+1],l[j]=l[j],l[j+1]
            j-=1
    print(f"--sorted liste: {l}".upper())