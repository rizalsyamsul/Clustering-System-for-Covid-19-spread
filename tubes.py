# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:18:36 2020

@author: Sam
"""

import random
import matplotlib.pyplot as plt

def plot(x1,x2,x3,y1,y2,y3,inf,sembuh,day):
  x = (x1, x2, x3)
  y = (y1, y2, y3)
  colors = ("blue","red", "green")
  groups = ("Sehat","Terinfeksi", "Imun")
  markers = ("o","o", "+")
  sizes = (10,50,100)
  fig = plt.figure(figsize=(4,4))
  ax = fig.add_subplot(1, 1,1)
  plt.grid
  for x,y, color, group, markers, sizes in zip(x,y, colors, groups, markers, sizes):
    ax.scatter(x, y, c=color, edgecolors=color, s=sizes, label=group,marker=markers)
  if day == 1:
    plt.title('Hari ke-'+str(day)+'     Terinfeksi = '+str(inf))
  elif day>1:
    plt.title('Hari ke-'+str(day)+'     Terinfeksi = '+str(inf)+'     Sembuh = '+str(sembuh))

  plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
  plt.show()

def grafik(x, y):
    plt.plot(x, y,'b')  
    plt.xlabel('Days')  
    plt.ylabel('Number of Infected People')  
    plt.show()
  
# deklarasi
individu = 200   
r = 5/100         
p = 0.8          
waktupulih = 10
Nterinfeksi = int(individu * 5/100)
Nsehat = individu - Nterinfeksi
jumlahsakit = Nterinfeksi
imun_stat = [0 for i in range(individu)]
waktu_infeksi = [0 for i in range(individu)]

kesehatan= []
#terinfeksi
for i in range(Nterinfeksi):
  kesehatan.append(1)
#sehat
for i in range(Nsehat):
  kesehatan.append(0)
  
x_max=20
x_min=0

y_min= 0
y_max=20

x_range = x_max-x_min
y_range = y_max-y_min

x_sehat = [] 
y_sehat = [] 
i_sehat = [] 

x_infec = [] 
y_infec = [] 
i_infec = [] 

x_recover = [] 
y_recover = []
i_recover = [] 


#posisi awal
x = [[random.randint(0, 20) for i in range(individu)]]
y = [[random.randint(0, 20) for i in range(individu)]]
i=0
while i < individu:
  if (kesehatan[i] == 1): 
    x_infec.append(x[0][i])
    y_infec.append(y[0][i])
    i_infec.append(i)
  if (kesehatan[i] == 0):
    x_sehat.append(x[0][i])
    y_sehat.append(y[0][i])
    i_sehat.append(i)
  i+=1
plot(x_sehat,x_infec,x_recover,y_sehat,y_infec, y_recover, Nterinfeksi,0,1)

i = 0
while Nterinfeksi>0: 
    sembuh = 0 
    x.append([])
    y.append([])
    
    for j in range(individu): 
        x_now = x[i][j]
        y_now = y[i][j]

        rand = random.random()
        pb = random.random()
        if(pb > p): 
          x[i+1].append(x_now)
          y[i+1].append(y_now)
        else: 
          #kanan
          if rand <= 0.20:  
              if x_max <= x_now:
                  x[i+1].append(x_now-x_range)
                  y[i+1].append(y_now)
              else:
                  x[i+1].append(x_now+1)
                  y[i+1].append(y_now)
          #bawah       
          elif rand <= 0.40:
              if y_min >= y_now:
                  y[i+1].append(y_now+y_range)
                  x[i+1].append(x_now)
              else:
                  y[i+1].append(y_now-1)
                  x[i+1].append(x_now)
          elif rand <= 0.60:
              if x_min >= x_now:
                  x[i+1].append(x_now+x_range)
                  y[i+1].append(y_now)
              else:
                  x[i+1].append(x_now-1)
                  y[i+1].append(y_now)
          #atas
          else:
              if y_max <= y_now:
                  y[i+1].append(y_now-y_range)
                  x[i+1].append(x_now)
              else:
                  y[i+1].append(y_now+1)
                  x[i+1].append(x_now)
                 
        if (kesehatan[j] == 1):
            if (waktu_infeksi[j] <=waktupulih):
              waktu_infeksi[j] +=1
            elif (waktu_infeksi[j] > waktupulih): 
              sembuh +=1
              imun_stat[j] = 1
              kesehatan[j] = 0
              Nterinfeksi -= 1
              x_recover.append(x[i][j])
              y_recover.append(y[i][j])
              i_recover.append(j)
              temp = i_infec.index(j)
              del i_infec[temp]
              del x_infec[temp]
              del y_infec[temp]

        for k in i_recover: 
          if (k == j):
              temp = i_recover.index(k)
              x_recover[temp] = x[i][temp]
              y_recover[temp] = y[i][temp]

        for k in i_sehat: 
          if (k == j):
              temp = i_sehat.index(k)
              x_sehat[temp] = x[i][temp]
              y_sehat[temp] = y[i][temp]

        for k in i_infec: 
          if (k == j):
              temp = i_infec.index(k)
              x_infec[temp] = x[i][temp]
              y_infec[temp] = y[i][temp]
          if ((x[i][k] == x[i][j]) and (y[i][k] == y[i][j]) and (j!=k) and (i_infec[-1] < j)):
              x_infec.append(x[i][j])
              y_infec.append(y[i][j])
              i_infec.append(j)
              kesehatan[j] = 1
              Nterinfeksi+=1
              jumlahsakit += 1
              temp = i_sehat.index(j)
              del i_sehat[temp]
              del x_sehat[temp]
              del y_sehat[temp]

    i+=1
    hari = i
    #plot
    plot(x_sehat,x_infec,x_recover,y_sehat,y_infec, y_recover, 
           Nterinfeksi,len(i_recover),hari)
    


