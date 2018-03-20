import numpy as np
import matplotlib.pyplot as plt


def normal_dist(x,mean,sigma):
	x=[]
	x.append(np.random.normal(loc=mean,scale=sigma,x))
	return x 
