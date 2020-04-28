# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:18:36 2020

@author: Sam
"""

import numpy
import random
import matplotlib.pyplot as plt

def plot(x1,x2,x3,y1,y2,y3, n_i,n_r,sem, inf,day):
  x = (x1, x2, x3)
  y = (y1, y2, y3)
  colors = ("blue","red", "green")
  groups = ("sehat","terinfeksi", "sembuh")
  markers = ("o","o","x")
  sizes = (30,50,100)
  # Create plot
  fig = plt.figure(figsize=(6,6))
  ax = fig.add_subplot(1,1,1)
  plt.grid


  for x,y, color, group, markers, sizes in zip(x,y, colors, groups, markers, sizes):
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors=color, s=sizes, label=group,marker=markers )

  if day == 1:
    plt.title('Hari ke-'+str(day)+'     Terinfeksi = '+str(n_i-inf))
  elif day>1:
    plt.title('Hari ke-'+str(day)+'     Terinfeksi = '+str(n_i-inf)+'  (+'+str(inf)+')'+'     Sembuh = '+str(n_r)+'  (+'+str(sem)+')')
    
  plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
  plt.show()
  
  
#deklarasi
Nindividu = 200  #jumlah individu
r = 5/100       #ratio terinfeksi
p = 0.8         #probability individu bergerak
tpulih = 10    #waktu pemulihan

Nterinfeksi = int(Nindividu * r)
Nsehat = Nindividu - Nterinfeksi
imun = [0 for i in range(Nindividu)]
tinfeksi = [0 for i in range(Nindividu)]

kesehatan= []
for i in range(Nterinfeksi):
  kesehatan.append(1)
for i in range(Nsehat):
  kesehatan.append(0)

#ukuran ruang simulasi 20x20
#x_max=20
#x_min=0
#y_min= 0
#y_max=20
x_range = 20-0
y_range = 20-0

x_infec = []
y_infec = [] 
i_infec = []

x_sehat = [] 
y_sehat = [] 
i_sehat = []

x_recover = [] 
y_recover = [] 
i_recover = []

#inisialisasi posisi
x_pos = [[random.randint(0, 20) for i in range(Nindividu)]]
y_pos = [[random.randint(0, 20) for i in range(Nindividu)]]
i=0
while i < Nindividu:
  if (kesehatan[i] == 1): 
    x_infec.append(x_pos[0][i])
    y_infec.append(y_pos[0][i])
    i_infec.append(i)
  if (kesehatan[i] == 0): 
    #individu sehat
    x_sehat.append(x_pos[0][i])
    y_sehat.append(y_pos[0][i])
    i_sehat.append(i)
  i+=1

plot(x_sehat,x_infec,x_recover,y_sehat,y_infec,y_recover,Nterinfeksi,0,0,0,1)

j = 0
while Nterinfeksi > 0:
    infec = 0
    sembuh = 0
    x_pos.append([])
    y_pos.append([])
    
    for k in range(Nindividu) :
        


