import numpy as np
from sklearn.neighbors import NearestNeighbors

#Clase Variedad
#Al terminar de ejecutar la funcion LTSA, la funcion crea un objeto
#Variedad que almacena los puntos en la alta dimencion y en la baja
#Asi como crea la funcion aprendida
#Parametros de inicializacion matriz de datos X, proyecciones T, d (dimension menor)
#k, numero de vecinos a conciderar
#Matriz T_i y Q_i y lista de k vecinos de X
class Variedad:
    def __init__(self,X,T,d,k, Th, Q, ind):
        self.X=X
        self.T=T
        self.d=d
        self.k=k
        self.Th=Th
        self.Q=Q
        self.ind=ind
    def funVariedad(self,tau): #La funcion evalua un punto en la baja dimension a la alta
        tAux=np.empty((self.T.shape[0],self.T.shape[1]+1))
        for i in range(self.T.shape[0]):
            tAux[i][0]=tau[i]
        for i in range(self.T.shape[1]):
            for j in range(self.T.shape[0]):
                tAux[j][i+1]=self.T[j][i]
        nbrs = NearestNeighbors(n_neighbors=self.k+1, algorithm='ball_tree').fit(tAux.T)
        dist, ind1 = nbrs.kneighbors(tAux.T)
        ii=ind1[0][1] ##El mas cercano a tau
        #Promediamos tau_i
        taup=np.zeros(tau.size)
        for i in range(self.k+1):
            if ind1[ii][i]!=0:
                for j in range(tau.size):
                    taup[j]+=tAux[j][ind1[ii][i]]
        taup=taup/self.k
        ii-=1
        xp=np.zeros(self.X.shape[0])
        for i in range(self.k):
            for j in range(self.X.shape[0]):
                xp[j]+=self.X[j][self.ind[ii][i]]
        xp=xp/self.k
        T1=np.empty((self.d,self.k))
        for i in range(self.k):
            T1[0][i]=self.T[0][ind1[ii+1][i]]
            T1[1][i]=self.T[1][ind1[ii+1][i]]
        T=np.dot(T1,np.identity(self.k)-np.ones(self.k)/self.k)
        L1=np.dot(T,np.linalg.pinv(self.Th[ii]))
        return xp + np.dot(self.Q[ii],np.dot(np.linalg.pinv(L1),tau-taup ) )

#ALGORITMO LTSA descrito en reporte, recibe matriz de datos X,
#numero de vecinos a considerar k y dimension baja
def LTSA(X,k,d):
    M=int(X.shape[0])
    N = int(X.shape[1])
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(X.T)
    dist, ind = nbrs.kneighbors(X.T)
    B=np.zeros((N,N)) + 0.1*np.identity(N)
    TH=[]
    Q=[]
    for i in range(N):
        Xi=matrizKNN(X,ind,i,k,M,N)
        Xc=np.dot(Xi,(np.identity(k)-(np.zeros((k,k))+1)/k ))
        U, D, V = np.linalg.svd(Xc)
        Qi=computeQ(U,d,M)
        Th=np.dot(Qi.T,Xc)
        TH.append(Th)
        Q.append(Qi)
        Wi=np.dot( (np.identity(k)- ((np.zeros((k,k))+1)/k)) ,(np.identity(k)-np.dot(np.linalg.pinv(Th),Th)))
        for j in range(k):
            for l in range(k):
                B[ind[i][j]][ind[i][l]]= B[ind[i][j]][ind[i][l]] + Wi[j][l]
        #Calcula Xi los vecinos mas cercanos
        #Calcula la matriz Xi
    w,v=np.linalg.eig(B)
    T=np.empty((N,d))
    for i in range(N):
        for j in range(d):
            T[i][j]=v[i][N-d+j-1]
    T1=np.empty((d,N))
    for i in range(N):
        for j in range(d):
            T1[j][i]=T.T[j][N-1-i]
    a=Variedad(X,T.T,d,k,TH,Q,ind)
    return T.T, a

#Funcion que usa LTSA para crear matriz de k-nn
def matrizKNN(X,ind,i,k,M,N):
    Xi=np.empty((M,k))
    for j in range(k):
        for l in range(M):
            Xi[l][j]=X[l][ind[i][j]]
    return Xi
#Funcion que usa LTSA para crear matriz Q
def computeQ(U,d,M):
    Q=np.empty((M,d))
    for i in range(d):
        for j in range(M):
            Q[j][i]=U[j][i]
    return Q