#!/usr/bin/env python
# coding: utf-8

# In[8]:


llista=[["gener","febrer","març"],["abril","maig","juny"],["juliol","agost","setembre"],["octubre","novembre","desembre"]]
print(llista[0][1])
print(llista[0])
print(llista[2][2],llista[3][0])


# In[31]:


llista2=[89,87,3,4,45,99,6,3]
print(len(llista2))
x=0
y=0
z=0
for i in llista2:
    if i==3:
        x+=1
    if i==4:
        y+=1
    if i>z:
        z=i
print("El número 3 apareix",x,"vegades")
print("El número 3 i 4 apareix",x+y,"vegades")
print("El número més gran és:",z)

###Ordenaré la llista per obtenir els 3 més petits
llista2.sort()
print("Els 3 números més petits són:", llista2[0:3])



# In[36]:


Compra={"Pomes":{"Qty":5,"€":0.42},"Peres":{"Qty":3,"€":0.66}}
Compra.update({"platans":{"Qty":5,"€":0.96}})
print("El preu total de les peres és:",Compra["Peres"]['Qty']*Compra["Peres"]['€'])
print("El nombre total de fruites és de:",len(Compra))
fruita_cara=0
nom_fruita=""
for i in Compra:
    if(Compra[i]["Qty"]*Compra[i]["€"]>fruita_cara):
        fruita_cara=Compra[i]["Qty"]*Compra[i]["€"]
        nom_fruita=i
print("La fruita més cara són", nom_fruita, "i el seu preu és de:", fruita_cara, "€")


# In[38]:


def notes(nota):
    if(nota<5):
        return 'suspès'
    elif(nota<7):
        return 'aprovat'
    elif(nota<9):
        return 'notable'
    else:
        return 'excel·lent'
print(notes(3))
print(notes(6))
print(notes(8))
print(notes(9))    


# In[39]:


def numeros(num1,num2):
    if(num1>num2):
        print("El primer número és més gran que el segon")
    elif(num1<num2):
        print("El segon número és més gran que el primer")
    else:
        print("Els dos números són iguals")
x1=int(input("Introdueixi el primer número:"))
x2=int(input("Introdueixi el segon número:"))
numeros(x1,x2)


# In[ ]:


def repetirNom(y,nom):
    if(y==0):
        print("Error")
    else:
        print(y*(nom+" "))
x=int(input("Introdueixi un número:"))
n=input("Introdueixi un nom:")
repetirNom(x,n)


# In[15]:


def simetria(llista):
    cont=0
    sim=True
    x=len(llista)-1
    if((x+1)%2==0):
        while(cont<x):
            if(llista[cont]!=llista[x]):
                sim=False
                break
            cont+=1
            x-=1
        if(sim):
            print("llista simètrica de",len(llista),"elements")
        else:
            print("llista NO simètrica")
    else:
        print("llista NO simètrica")
llista=[1,2,3,3,2,1]
simetria(llista)


# In[18]:


def coincidencies(llista):
    cont=0
    llista_coincid=[]
    for i in llista:
        if(i==cont):
            llista_coincid.append(i)
        cont+=1
    return llista_coincid
llista=[2,3,4,5,4,5,7,7]
print("els números que coincideixen amb la seva posició són:",coincidencies(llista))


# In[ ]:




