import random
import numpy as np

def Sample_Exponential_Distance():
	'''
	距離範圍:		0~無限大
	機率密度函數:	P(r) = 	1/(4*pi) * exp(-r)
	距離取樣:		r = -ln(R), where R = 0~1
	回傳一個距離r
	'''
	return -np.log(random.random())

def Sample_Uniform_Angle():
	'''
	角度範圍:		0~2*pi
	機率密度函數:	P(phi) = 1/(2*pi)
	角度取樣:		phi = 2*pi*R, where R = 0~1
	回傳一個方位角度phi
	'''
	return -2*np.pi*random.random()

def Sample_dxdy():
	'''
	回傳一組卡式座標，表示取樣點與參考點的相對位移
	'''
	r=Sample_Exponential_Distance()
	phi=Sample_Uniform_Angle()
	return r*np.cos(phi),r*np.sin(phi)

def Sample_Discrete_dxdy(): #用這個就好!!!
	'''
	回傳一組卡式座標，表示與取樣點「最接近」的網格中心座標與參考點的相對位移，如果結果為(0,0)則重新取樣
	'''
	while True:
		dx,dy=Sample_dxdy()
		intx = int(dx)
		if dx<0:
			intx=intx-1
		inty = int(dy)
		if dy<0:
			inty=inty-1
		GridCenter = [[intx,inty],[intx+1,inty],[intx,inty+1],[intx+1,inty+1]]
		DisList = [(GridCenter[i][0]-dx)**2+(GridCenter[i][1]-dy)**2 for i in range(len(GridCenter))]
		Minindex = DisList.index(min(DisList))
		if GridCenter[Minindex][0]!=0 or GridCenter[Minindex][1]!=0:
			return GridCenter[Minindex][0],GridCenter[Minindex][1]