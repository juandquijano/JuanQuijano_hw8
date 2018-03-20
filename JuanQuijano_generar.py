import numpy as np
import matplotlib.pyplot as plt

##funcion que retorna N numeros aleatorios con la distribucion P dada
def sample_1(N):  
		a = [-10.0,-5.0,3.0,9.0]
		x=np.random.choice(a=a,size= N, p=[0.1, 0.4, 0.2, 0.3])
		return x 

##funcion que retorna N numeros aleatorios con la distribucion exponencial		
def sample_2(N):
		y = np.random.exponential(0.5, N)
		return y

##funcion que obtiene los promedios, primero lo almacena en una variable x
## y despues llena una lista y de tamano N con esos promedios
def get_mean(sampling_fun,N,M):
	x=0
	y=[]	
	for i in range(M):
		x=np.mean(sampling_fun(N))
		y.append(x)
	return y

###para los valores propuestos se crean 3 recorridos los cuales crean los txt
for value in (10.0,100.0,1000,0):
	x=get_mean(sample_1,value,1000)
	y=get_mean(sample_2,value,1000)
	if (value==10.0):
		np.savetxt("sample1_10.txt",x)
		np.savetxt("sample2_10.txt",y)
	elif (value==100.0):
		np.savetxt("sample1_100.txt",x)
		np.savetxt("sample2_100.txt",y)
	else:
		np.savetxt("sample1_1000.txt",x)
		np.savetxt("sample2_1000.txt",y)

	
