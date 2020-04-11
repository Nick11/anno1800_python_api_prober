import pickle
import sys

def log(text):
	mod_dir = 'C:/code/anno1800_modding/python/'
	with open(mod_dir+'debug.log', 'a') as log_file:
		log_file.write(str(text)+'\n\n')

data = DATA
#data = data.AreaPopulation.GetPopulationCount()
#data = in_data.AreaProductDelta.GetDelta()
#data = in_data.EconomyStatistic.GetProductionStatistic().GetProductGeneration(1)
#data = in_data.Economy.GetMetaStorage().GetAvailableAmount()
data = dir(data)
log(data)