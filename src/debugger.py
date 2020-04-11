import pickle
import sys

def log(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text)+'\n\n')

data = DATA['TextSources'].TextSourceRoots.GetRefGuid()
#data = data.AreaPopulation.GetPopulationCount()
#data = in_data.AreaProductDelta.GetDelta()
#data = in_data.EconomyStatistic.GetProductionStatistic().GetProductGeneration(1)
#data = in_data.Economy.GetMetaStorage().GetAvailableAmount()
#data = dir(data)
log(data)