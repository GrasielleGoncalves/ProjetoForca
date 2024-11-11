def main ():
    c= "b,c,d,f,gh,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
    v=[]
    cont=0 
    while cont < 10:
        v.append(str(input("digite uma string")))
        cont+=1
    
    const = 0
    consoante = 0
    while const < len(v):
        if v[const] in c:
            consoante += 1
        const += 1
        
    print(consoante)







if __name__ == "__main__":
    main()
