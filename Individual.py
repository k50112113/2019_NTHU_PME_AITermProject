import random
import numpy as np
from functools import total_ordering
@total_ordering
class Individual():
	def __init__(self, id, wealth, DNA=None):
		self.Reset(id, wealth, DNA)

	def Reset(self, id, wealth, DNA):
		self.ID = id
		if DNA:
			self.DNA = DNA
		else:
			preDNA = [0]
			DNA = []
			preDNA.extend([random.random() for i in range(5)])
			preDNA.append(1)
			preDNA.sort()
			for i in range(6):
				DNA[i] = preDNA[i+1]-preDNA[i]
			DNA.append(random.random())
			self.DNA = DNA

		'''
		DNA[0] = 合作
		DNA[1] = 背叛
		DNA[2] = 上一個人對我做什麼，我就對下一個人做什麼
		DNA[3] = 前面大部分的人對我做什麼，我就對下一個人做什麼
		DNA[4] = 隨機合作或背叛
		DNA[5] = 先合作，如果上一個人跟我合作，那我對下一個人做上一回合做的事，反之，對下一個人做上一回合相反的事
		
		DNA[6] = 犯錯
		'''
		self.Wealth = wealth
		self.N_of_Crpt = 0 #別人對自己合作次數
		self.N_of_Btry = 0 #別人對自己背叛次數
		self.Last_Time_Received = True #前一次別人跟他合作或背叛，預設合作
		self.Last_Time_Did = True
		
	def Response(self):
		'''
		根據DNA回傳合作或背叛
		return True 表示合作
		return False 表示背叛
		'''
		error = random.choices([True, False], weights=[1- self.DNA[6], self.DNA[6]]) #依照DNA[6]的機率決定是否犯錯
		strategy = random.choices([i for i in range(6)], weights=self.DNA[:6])  #依照DNA[:6] 決定response strategy
		if strategy == 0:
			return (True and error)
		elif strategy == 1:
			return (False and error)
		elif strategy == 2:
			return (self.Last_Time_Received and error)
		elif strategy == 3:
			if self.N_of_Crpt >= self.N_of_Btry:
				return True and error
			else:
				return False and error
		elif strategy == 4:
			return random.choice([True, False])
		else:
			return self.Last_Time_Did and self.Last_Time_Received and error


	def Print_Status(self):
		'''
		印出自身狀態
		'''
		print("\n%25s%5d"%("ID:",self.ID))
		print("-"*79)
		print("%25s%5d"%("Wealth:",self.Wealth))
		print("%25s%5d"%("Received Cooperation:",self.N_of_Crpt))
		print("%25s%5d"%("Received Betray:",self.N_of_Btry))
		print("%25s%5d"%("Last Time Received:",self.Last_Time_Received))
		print("-"*79)

	def __eq__(self, other):
		if self.wealth == other.wealth:
			return True
		else:
			return False

	def __gt__(self, other):
		if self.wealth > other.wealth:
			return True
		else:
			return False


