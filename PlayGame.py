'''
Agent_A,Agent_B 為 Individual
Gain,Trade,Loss 皆為正數

					Agent_A
				合作		背叛
		合作	A+,B+		A+,B-
				Gain		Trade
Agent_B
		背叛	A+,B-		A-,B-
				Trade		Loss

'''
def Play_Prisoner_s_dilemma(Agent_A,Agent_B,Gain,Trade,Loss):
	
	if Agent_A.Response() == True and Agent_B.Response() == True: #A,B 皆合作
		Agent_A.Wealth = Agent_A.Wealth + Gain
		Agent_B.Wealth = Agent_B.Wealth + Gain
		Agent_A.N_of_Crpt = Agent_A.N_of_Crpt + 1
		Agent_B.N_of_Crpt = Agent_B.N_of_Crpt + 1
		Agent_A.Last_Time_Received = True
		Agent_B.Last_Time_Received = True
	elif Agent_A.Response() == False and Agent_B.Response() == True:
		Agent_A.Wealth = Agent_A.Wealth + Trade
		Agent_B.Wealth = Agent_B.Wealth - Trade
		Agent_A.N_of_Crpt = Agent_A.N_of_Crpt + 1
		Agent_B.N_of_Btry = Agent_B.N_of_Btry + 1
		Agent_A.Last_Time_Received = True
		Agent_B.Last_Time_Received = False
	elif Agent_A.Response() == True and Agent_B.Response() == False:
		Agent_A.Wealth = Agent_A.Wealth - Trade
		Agent_B.Wealth = Agent_B.Wealth + Trade
		Agent_A.N_of_Btry = Agent_A.N_of_Btry + 1
		Agent_B.N_of_Crpt = Agent_B.N_of_Crpt + 1
		Agent_A.Last_Time_Received = False
		Agent_B.Last_Time_Received = True
	elif Agent_A.Response() == False and Agent_B.Response() == False:
		Agent_A.Wealth = Agent_A.Wealth - Loss
		Agent_B.Wealth = Agent_B.Wealth - Loss
		Agent_A.N_of_Btry = Agent_A.N_of_Btry + 1
		Agent_B.N_of_Btry = Agent_B.N_of_Btry + 1
		Agent_A.Last_Time_Received = False
		Agent_B.Last_Time_Received = False
	