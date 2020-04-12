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
	routeIDs = getTradeRouteIDs(DATA)
	routeID = routeIDs[0]
	routes = getTradeRoutes(DATA)
	route = routes[3]
	data = route.MouseLeft()
	
	data = DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0]
	data = DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[1]
	
	
	#openRoute(DATA)
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0]
	
	
	#data = DATA['scenes'].SessionTradeRoutes.Data.StationData[1].StationID
	
	
	
	#data = DATA['TextSources'].TextSourceRoots.GetTradeRoute().GetRoute(routeID).GetStation(0)
	#data = DATA['TextSources'].TextSourceRoots.TradeRoute.GetRoute(routeID)
	#data = DATA['scenes'].ObjectMenuShip.FleetObject.ActiveItemData
	#data = len(data)
	#data = vars(data)
	log(data)
	log(dir(data))
	log(len(data))
	log('\n')

def log(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text)+'\n\n')

def getTradeRoutes(modules):
	return scenes(modules).SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData
	
def getTradeRouteIDs(modules):
	routeData = getTradeRoutes(modules)
	return [route.RouteID for route in iter(routeData)]

def getAreasForRoute(modules, route):
	pass

def getAreaFromId(modules, areaID):
	return TextSourceRoots(modules).GetArea().GetAreaFromID(areaID)

def getStationsForTradeRoute(tradeRouteID):
	pass
	
def TextSourceRoots(modules):
	return modules['TextSources'].TextSourceRoots


def scenes(modules):
	return modules['scenes']
	
def iter(self):
	for i in range(len(self)):
		yield self[i]

# Notes
def openCharterRoute(modules):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.TransferData[1].RouteButtonClicked()
def openRoute(modules):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0].EditRouteClicked()
def getCargoForLAstSelectedShip():
	DATA['scenes'].ObjectMenuShip.ShipObject.CargoSlotData[0].ItemData.ButtonBehaviour.RefGUID
	
main()

