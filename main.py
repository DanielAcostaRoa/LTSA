import numpy as np
import LTSA 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.io

##Funcion donde leo la base de datos de las imagenes y aplico LTSA
##Regresa lista de conjuntos a examinar y el objeto de LTSA
def Imagenes():
    mat = scipy.io.loadmat('images.mat')
    X=mat['ff']
    X1=np.empty((560,600))
    for i in range(560):
        for j in range(600):
            X1[i][j]=X[i][j]
    Z, obj=LTSA.LTSA(X1,5,2)
    liz1=[]
    liz2=[]
    liz3=[]
    for i in range(Z[0].size):
        if Z[0][i]>0.03 and Z[1][i]<0:
            liz1.append(i)
        if Z[0][i]>0.001 and Z[0][i]<0.0044 and Z[1][i]>0.045 and Z[1][i]<0.07:
            liz2.append(i)
        if Z[0][i]>-0.0158 and Z[0][i]<0.02 and Z[1][i]>-0.04 and Z[1][i]<-0.021:
            liz3.append(i)
    liz1=np.array(liz1)
    liz2=np.array(liz2)
    liz3=np.array(liz3)
    color=np.zeros(Z[0].size)+1
    for i in range(liz1.size):
        color[liz1[i]]=15
    for i in range(liz2.size):
        color[liz2[i]]=30
    for i in range(liz3.size):
        color[liz3[i]]=10
    plt.scatter(Z[0],Z[1],c=color)
    return liz1,liz2,liz3, obj

#mapea el vector a usando la funcion fun y muestra la imagen 
def imp(a,fun):
    pp=fun(a)
    aa=np.empty((28,20))
    for i in range(28):
        for j in range(20):
            aa[i][j]=pp[i*20+j]
    plt.imshow(aa, cmap=plt.cm.gray)

#Imprime una imagen, recibe matriz donde cada columna es una imagen
#y el indice i que indica que imagen imprimir   
def imprimeImagen(X,i):
    a=X.T[i]
    aa=np.empty((28,20))
    for i in range(28):
        for j in range(20):
            aa[i][j]=a[i*20+j]
    plt.imshow(aa, cmap=plt.cm.gray)

#Construye grafica 1 
def Grafica1():
    tau=np.linspace(0, 4 * np.pi, 500)
    x1=tau*np.cos(tau) + 0.01*np.random.normal(2, 1, 500)
    x2=tau*np.sin(tau) + 0.01*np.random.normal(2, 1, 500)
    col=np.arange(1,500+1)
    #plt.scatter(x1,x2,c=col)
    X=np.empty((2,x1.size))
    for j in range(x1.size):
        X[0][j]=x1[j]
        X[1][j]=x2[j]
    Z,obj=LTSA.LTSA(X,4,1)
    zz=np.array(500*[0.0])
    for i in range(500):
        zz[i]=Z[0][i]
    plt.scatter(tau,zz,c=col)
    return Z

#Construye grafica 2
def Grafica2():
    n=200
    tau=np.linspace(-1, 1, n)
    x1=10*tau + .01*np.random.normal(2, 1, n)
    x2=10*tau**3+2*tau**2-10*tau + 0.01*np.random.normal(2, 1, n)
    col=np.arange(1,n+1)
    #plt.scatter(x1,x2,c=col)
    X=np.empty((2,x1.size))
    for j in range(x1.size):
        X[0][j]=x1[j]
        X[1][j]=x2[j]
    Z,obj=LTSA.LTSA(X,3,1)
    zz=np.array(n*[0.0])
    for i in range(n):
        zz[i]=Z[0][i]
    plt.scatter(tau,zz,c=col)
    return Z

#Construye grafica 3
def Grafica3():
    n=200
    figura_3d = plt.figure()
    ax = figura_3d.gca(projection = '3d')
    theta = np.linspace(0, 4 * np.pi, n)
    z1=3*np.cos(theta) + .05*np.random.normal(3, 1, n)
    z2=3*np.sin(theta) + .05*np.random.normal(3, 1, n)
    z3=3*theta + .05*np.random.normal(3, 1, n)
    col=np.arange(1,n+1)
    ax.scatter(z1,z2,z3,c=col)
    X=np.empty((3,z1.size))
    for j in range(z1.size):
        X[0][j]=z1[j]
        X[1][j]=z2[j]
        X[2][j]=z3[j]
    Z,obj=LTSA.LTSA(X,8,1)
    zz=np.array(n*[0.0])
    for i in range(n):
        zz[i]=Z[0][i]
    #plt.scatter(theta,zz,c=col)
    return Z
    