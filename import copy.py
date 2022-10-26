import copy
import time
from tkinter import * #pour creer une interface
import random
#rapport :Une interface graphique est un outil permettant d’interagir..

##Ceci est une version du programme avec une interface graphique.Toutefois, l'éxécution sera un peu plus lente.
def etatinitial():
    mat=[[2,8,3],[1,6,4],[7,0,5]]
    #hony amlna test nchofo ken case mta3 interface heya bideha lcase mta3 matrice
    if (L1['text']!=mat[0][0] or L2['text']!=mat[0][1] or L3['text']!=mat[0][2] or L4['text']!=mat[1][0] or L5['text']!=mat[1][1] or L6['text']!=mat[1][2] or L7['text']!=mat[2][0] or L8['text']!=mat[2][1] or L9['text']!=mat[2][2]):
        mat[0][0]=int(L1['text'])
        mat[0][1]=int(L2['text'])
        mat[0][2]=int(L3['text'])
        mat[1][0]=int(L4['text'])
        mat[1][1]=int(L5['text'])
        mat[1][2]=int(L6['text'])
        mat[2][0]=int(L7['text'])
        mat[2][1]=int(L8['text'])
        mat[2][2]=int(L9['text'])
    return mat
def retourinitial():##Changer les valeurs ici afin de commencer à partir d'un état initial choisi par l'utilisateur.
    #hony ili yal3eb 9a3ed ya3by fil case mta3 interface
    L1['text']='2' #Ktebna fi west button "2"
    L2['text']='8'
    L3['text']='3'
    L4['text']='1'
    L5['text']='6'
    L6['text']='4'
    L7['text']='7'
    L8['text']='0'
    L9['text']='5'
def affichermat(m):
    print("+-+-+-+-+-+-+")
    for i in range(3):
        p=""
        for j in range(3):
            v=str(m[i][j])
            print("| "+v+" ",end='')
        print("|")
        print("+-+-+-+-+-+-+");
    print("\n")
    print("\n")
    print("-----------------------")
    print("-----------------------")
    print("\n")
    print("\n")
def afficher(t):#ba3ed matl3na position mta3 case vide namlo copier lil matrice
    (x,y)=position_case_vide(t)
    L1['text']=copy.deepcopy(t[0][0])
    L2['text']=copy.deepcopy(t[0][1])
    L3['text']=copy.deepcopy(t[0][2])
    L4['text']=copy.deepcopy(t[1][0])
    L5['text']=copy.deepcopy(t[1][1])
    L6['text']=copy.deepcopy(t[1][2])
    L7['text']=copy.deepcopy(t[2][0])
    L8['text']=copy.deepcopy(t[2][1])
    L9['text']=copy.deepcopy(t[2][2])
    L1.update()
    L2.update()
    L3.update()
    L4.update()
    L5.update()*
    L6.update()
    L7.update()
    L8.update()
    L9.update()
    time.sleep(1)  

def position_case_vide(mat):
    y=0
    x=0
    c=0
    l=0
    for x in range (3):
        for y in range (3):
            if (mat[x][y]==0):
                l=x
                c=y
    return l,c
def etatfinal(mat):
    if(mat==[[1,2,3],[8,0,4],[7,6,5]]):
        return True    
def transitions(mat):
    if (mat[2][0]==0):
        return (1,0),(2,1)
    elif (mat[0][0]==0):
        return (1,0),(0,1)
    elif (mat[2][2]==0):
        return (2,1),(1,2)
    elif (mat[0][2]==0):
        return (0,1),(1,2)
    elif (mat[1][1]==0):
        return (0,1),(1,0),(1,2),(2,1)
    elif (mat[1][2]==0):
        return (0,2),(1,1),(2,2)
    elif (mat[0][1]==0):
        return (0,0),(0,2),(1,1)
    elif (mat[2][1]==0):
        return (1,1),(2,0),(2,2)
    elif (mat[1][0]==0):
        return (1,1),(0,0),(2,0)
def permuter( mat,c1,c2):#ndkhlou position t 0 c1,c2
    for i in range(3):
        for j in range(3):
            if mat[i][j]==c1:
                x1=i
                x2=j
            if mat[i][j]==c2:
                x3=i
                x4=j
    mat[x1][x2],mat[x3][x4]=mat[x3][x4],mat[x1][x2]
    return mat    
    #afficher text 3 fois . puis .. puis ...
def calcul2(L11):  
     L11['text']="Calcul de l'etat final."
     L11.update()
def calcul3(L11):
     L11['text']="Calcul de l'etat final.."
     L11.update()
def calcul4(L11):
     L11['text']="Calcul de l'etat final..."
     L11.update()
#calcul heuristique     
def comparer(mat2):
    mat1=[[1,2,3],[8,0,4],[7,6,5]]
    h=0
    for i in range (3):
        for j in range (3):
            if (mat1[i][j]!=0):
                if (mat1[i][j]!=mat2[i][j]):
                    h=h+1
    return h

def Aetoile():
    B1['state']="disabled" #DISABLE = n’est pas cliquable
    B2['state']="disabled" #state =état ta boutton teik
    v=etatinitial() #matrice initial
    OPEN=[v] #on a ajouté matricie v initial dans l'ensemble ouvert
    print("Etat Initial")
    affichermat(v)
    CLOSED=[[[0,0,0],[0,0,0],[0,0,0]]] #etat final vide
    t=etatinitial() 
    m=etatinitial()
    PROFONDEUR =[] #longeur d'arbre , niveau = cout (g(x))
    f=[]# h+g= h+cout
    PROFONDEUR.append(0) #on est à niveau 0 profondeur=
    h=comparer(OPEN[0])
    f.append(h+PROFONDEUR[0])
    pos=0
    L11=Label(main,text="Calcul de l'etat final",fg="blue",font=('Arial',40, 'bold'))
    L11.place(x=800,y=200)
    L12=Label(main,text="Etats Explorés",fg="red",font=('Arial',40, 'bold'))
    L12.place(x=930,y=350)
    L13=Label(main,text="0",fg="red",font=('Arial',40, 'bold'))
    L13.place(x=1080,y=410)
    compteEtat=0
    while (not(etatfinal(OPEN[pos])) and len(OPEN)!=0):
        x,y=position_case_vide(t)
        if (((x==0) and (y==0)) or ((x==0) and (y==2)) or ((x==2) and (y==0)) or ((x==2) and (y==2))):
            (x1,y1),(x2,y2)=transitions(t)
            m=permuter(m,m[x1][y1],m[x][y])
            if(m not in CLOSED):
               t=permuter(t,t[x1][y1],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               t=permuter(t,t[x1][y1],t[x][y])
               m=permuter(m,m[x1][y1],m[x][y])
               m=permuter(m,m[x2][y2],m[x][y])
            else:
               m=permuter(m,m[x1][y1],m[x][y])
               m=permuter(m,m[x][y],m[x2][y2])
            if(m not in CLOSED):
               t=permuter(t,t[x2][y2],t[x][y])
               z=copy.deepcopy(t)
               h=copy.deepcopy(comparer(z))
               OPEN.append(z)
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
        elif ((x==1) and (y==1)): 
            (x1,y1),(x2,y2),(x3,y3),(x4,y4)=transitions(t)
            m=permuter(m,m[x1][y1],m[x][y])
            if(m not in CLOSED):
               t=permuter(t,t[x1][y1],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               t=permuter(t,t[x1][y1],t[x][y])
               m=permuter(m,m[x1][y1],m[x][y])
               m=permuter(m,m[x2][y2],m[x][y])
            else:
               m=permuter(m,m[x1][y1],m[x][y])
               m=permuter(m,m[x][y],m[x2][y2])
            if(m not in CLOSED):
               t=permuter(t,t[x2][y2],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               m=permuter(m,m[x2][y2],m[x][y])
               t=permuter(t,t[x2][y2],t[x][y])
               m=permuter(m,m[x3][y3],m[x][y])
            else:
               m=permuter(m,m[x][y],m[x2][y2])
               m=permuter(m,m[x3][y3],m[x][y])
            if(m not in CLOSED):
               t=permuter(t,t[x3][y3],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               m=permuter(m,m[x3][y3],m[x][y])
               t=permuter(t,t[x3][y3],t[x][y])
               m=permuter(m,m[x4][y4],m[x][y])
            else:
               m=permuter(m,m[x][y],m[x3][y3])
               m=permuter(m,m[x4][y4],m[x][y])
            if(m not in CLOSED):
               permuter(t,t[x4][y4],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
        elif (((x==1) and (y==0)) or  ((x==0) and (y==1)) or ((x==1) and (y==2)) or ((x==2) and (y==1))):
            (x1,y1),(x3,y3),(x2,y2),=transitions(t)
            m=permuter(m,m[x1][y1],m[x][y])
            if(m not in CLOSED):
               t=permuter(t,t[x1][y1],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               m=permuter(m,m[x1][y1],m[x][y])
               t=permuter(t,t[x1][y1],t[x][y])
               m=permuter(m,m[x2][y2],m[x][y])
            else:
               m=permuter(m,m[x1][y1],m[x][y])
               m=permuter(m,m[x2][y2],m[x][y])
            if(m not in CLOSED):
               t=permuter(t,t[x2][y2],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
               m=permuter(m,m[x2][y2],m[x][y])
               t=permuter(t,t[x2][y2],t[x][y])
               m=permuter(m,m[x3][y3],m[x][y])
            else:
               m=permuter(m,m[x2][y2],m[x][y])
               m=permuter(m,m[x3][y3],m[x][y])
            if(m not in CLOSED):
               permuter(t,t[x3][y3],t[x][y])
               z=copy.deepcopy(t)
               OPEN.append(z)
               h=copy.deepcopy(comparer(z))
               PROFONDEUR.append(PROFONDEUR[pos]+1)
               
               f.append(PROFONDEUR[len(PROFONDEUR)-1]+h)
        r=copy.deepcopy(OPEN.pop(pos))
        f.pop(pos)
        PROFONDEUR.pop(pos)
        CLOSED.append(r)
        calcul2(L11) # baed kol matrice ymlha  yayt cal 2 3 4
        time.sleep(2)#le temps bint msg 1 w 2  w3 
        calcul3(L11)
        time.sleep(2)
        calcul4(L11)
        time.sleep(2)
        L11['text']="Calcul de l'etat final"# rajaaneha maghr noktatt mch maaa kol matrice yawd milou . .. ...
        L11.update()# 
        mini=min(f)
        pos=f.index(mini)
        compteEtat=compteEtat+1
        L13['text']=compteEtat # l13 label affiiche numero compte etat
        L13.update() #maa kol taghyiir mtaa text ybadlha 
        affichermat(OPEN[pos])
        afficher(OPEN[pos])
        print("Etats Explorés:",compteEtat)
        t=copy.deepcopy(OPEN[pos])
        m=copy.deepcopy(OPEN[pos])
        if (etatfinal(OPEN[pos])):
            L11['text']="Etat Final Atteint"  
            L11.config(fg="green")#config pour modifier"config" ,la couleur du text en utilisant "fg"
            L11.update()
    time.sleep(5)
    L11.destroy()# effacer tout ili ala imiiin
    L12.destroy()
    L13.destroy()
    B1['state']="normal" #NORMAL - Le bouton peut être cliqué par l’utilisateur
    B2['state']="normal"

start_time = time.time()
#crée notre fenetre
main=Tk()
#taille de notre fenetre 
main.geometry("1500x1500")
#titre de fenetre
main.title("Jeu De Taquin")
#LABEL-houni rsamna carroo w lawneh 9 marat
L1=Label(main,text="2",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2) 
L1.place(x=20,y=20)#PLACE - blaset button
L2=Label(main,text="8",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L2.place(x=258,y=20)
L3=Label(main,text="3",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L3.place(x=496,y=20)
L4=Label(main,text="1",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L4.place(x=20,y=246)
L5=Label(main,text="6",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L5.place(x=258,y=246)
L6=Label(main,text="4",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L6.place(x=496,y=246)
L7=Label(main,text="7",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L7.place(x=20,y=472)
L8=Label(main,text="0",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L8.place(x=258,y=472)
L9=Label(main,text="5",bg="purple",fg="yellow",font=('Arial', 70, 'bold'),width=4,height=2)
L9.place(x=496,y=472)
#command thsnii l fonction ta best A ili hya A étoile 
B1=Button(main,text="A*  ",command=Aetoile,fg="white",bg="black",font="bold" )
B1.place(x=380,y=700)
B2=Button(main,text="Retour à l'état initial",bg="black",fg="white",font="bold" ,command=retourinitial)
B2.place(x=650,y=750)
main.mainloop()#pour afficher notre fenetre
print("--- %s seconds ---" % (time.time() - start_time))