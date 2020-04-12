import sys, binascii
import os
sys.path.append(SRC_PATH)
from api_wrapper import api_wrapper as api

def main():
	wood_id = 120008

	#data = DATA

	#data = DATA['TextSources'].TextSourceRoots.EconomyStatistic.GetProductionStatistic().GetProductGeneration(wood_id)
	#data = data['TextSources'].TextSourceRoots.GetTradeRoute().GetRoute(10)
	#trade_route = DATA['TextSources'].TextSourceRoots.GetTradeRoute()
	#for route_index in [10,11,14]:
		#for station_index in range(2,3):
			#data = trade_route.GetRoute(i).GetNoGoodsActive()
		#belongs_to_me = trade_route.GetRoute(route_index).GetStation(3).#GetStationBelongsToCurrentParticipant()
		#if belongs_to_me:
			#log(route_index)
	#data = in_data.AreaProductDelta.GetDelta()
	#data = in_data.EconomyStatistic.GetProductionStatistic().GetProductGeneration(1)
	#data = in_data.Economy.GetMetaStorage().GetAvailableAmount()


	#data = DATA['TextSources'].TextSourceRoots.GetTradeRoute().GetRoute(10)
	#data = DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0].RouteID
	#data = DATA['scenes'].SessionTradeRoutes.Data.StationData[0].StationName
	#data = DATA['rdsdk::CRDString']('TEST')
	data = api.getTradeRoutes(DATA)
	#data = dir(data)
	#data = len(data)
	#data = vars(data)
	log(data)

def log(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text)+'\n\n')


main()

