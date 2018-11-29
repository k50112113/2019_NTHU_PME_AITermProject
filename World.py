import random
import Individual
import PlayGame
import SampleMethod
import copy
import heapq
import numpy as np

class World():
	def __init__(self, name, mapside, Avg, Std):
		self.Reset(name, mapside, Avg, Std)
	
	def Reset(self, name, mapside, Avg, Std):
		self.Name = name
		self.Size = mapside**2
		#self.ID_Map = [[x + x*y for x in range(mapside)] for y in range(mapside)]  # 看怎麼定義比較好，目前是用二維的，裡面放每個Individual的ID
		#self.Agent_List = [Individual.Individual(i, random.gauss(Avg, Std)) for i in range(self.Size)]  # 第n格表示ID為n的Individual
		self.Agent_List = [Individual.Individual([i//mapside, i%mapside], random.gauss(Avg, Std)) for i in range(self.Size)]
				
	def Interact(self,Interact_N):
		'''
		Interact_N = 要互動幾次
		
		互動方式：			PlayGame.Play_Prisoner_s_dilemma()
		互動對象取樣方式：	SampleMethod.Sample_Discrete_dxdy()
		
		for Interact_index in range(Interact_N):
			dx,dy=SampleMethod.Sample_Discrete_dxdy()
			...
			
		'''
		"""地圖的最左邊跟最右邊是算超近還是超遠啊?"""
			
	
	def Bear(self,Bear_N):
		'''
		Bear_N = 要生產多少人
		'''
		parents = self.selection()
		parents_address = [parent.ID for parent in parents]
		DNAs = self.crossover(parents)
		DNAs = self.mutation(DNAs)
		return DNAs, parents_address

	
	def Kill(self,Kill_N):
		'''
		Kill_N = 要淘汰多少人
		回傳Kill_N組座標，表示這些座標已經沒住人
		'''
		death = heapq.nsmallest(Kill_N, self.Agent_List, key = lambda x: x.wealth)
		address = [i.ID for i in death]
		return address


	def generation_change(self, Bear_N, Kill_N):
		DNAs, parents_address = self.Bear(Bear_N)
		empty_address = self.Kill(Kill_N)
		born_space = self.manhattan_squeeze(parents_address, empty_address)
		Avg, Std = self.Get_Wealth_Statistics()
		self.Agent_List.extend([Individual.Individual(born_space[i], DNAs[i], Avg, Std) for i in range(Bear_N)])
		"""
		*************未完成***********
		"""


	
	def Expense(self,Amount):
		'''
		Amount = 每個人要扣多少
		'''
		for x in range(self.Size):
			self.Agent_List[x].Wealth -= Amount

	
	def Get_Wealth_Statistics(self):
		'''
		回傳世界財富的平均及標準差
		'''
		wealth_list =[self.Agent_List[x].Wealth for x in range(self.Size)]
		Avg = np.mean(wealth_list)
		Std = np.std(wealth_list)
		
		return Avg,Std


	def selection(self):
		pass
	"""
	*****************未完成****************
	"""


	def crossover(self, parents):
		DNAs = []
		for i in range(len(parents)//2):
			father = copy.deepcopy(parents[2*i])
			mother = copy.deepcopy(parents[2*i + 1])
			child_a = []
			child_b = []
			for j in range(len(father.DNA)):
				bit = random.randint(0, 1)
				if bit == 0:
					child_a.append(father.DNA[j])
					child_b.append(mother.DNA[j])
				else:
					child_b.append(father.DNA[j])
					child_a.append(mother.DNA[j])
			DNAs.extend([child_a, child_b])
		return DNAs


	def mutation(self, DNAs):
		pass
	"""
	***************未完成*****************
	"""


	def manhattan_squeeze(self, parents_address, empty_address):
		pass

	"""
	***************未完成*****************
	"""


This_World = World("A Wrold",40)



