import sys, inspect
import os
sys.path.append(SRC_PATH)
from api_wrapper import api_wrapper as api
from asset_list import Products

def main():
	wood_id = 120008
	
	popIDs = {
                'farmers': 15000000,
                'workers': 15000001,
                'artisans': 15000002,
                'engineers': 15000003,
                'investors': 15000004
                }

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
	#routeIDs = getTradeRouteIDs(DATA)
	#routeID = routeIDs[0]
	#routes = getTradeRoutes(DATA)
	#route = routes[0]
	
	#data = DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0]
	#data = DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[1]
	
	
	
	#data = DATA['scenes'].SessionTradeRoutes.SceneTransition.Hide()
	#data = DATA['scenes'].SessionTradeRouteOverview.SceneTransition.Hide()
	#for i in range(2,20):
		#openRoute(DATA,i)
		#data = DATA['scenes'].SessionTradeRoutes.Data.StationData
		#log(len(data))
	#DATA['scenes'].SessionTradeRoutes.Data.CancelButtonReleased()
	#DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.CloseButtonReleased()
	
	#data = DATA['scenes'].SessionTradeRoutes.Data.StationData[1].StationID
	#data = scenes(DATA).SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[4]
	#data = DATA['scenes'].SessionTradeRoutes.Data.StationData
	
	#data = DATA['gameevents'].onChangeSelection
	
	#data = DATA['scenes'].ObjectMenuShip.FleetObject.ActiveItemData
	#data = DATA['TextSources'].TextSourceRoots.TradeRoute.GetRoute(routeID)
	
	#stationID = DATA['scenes'].SessionTradeRoutes.Data.StationData[0].StationID
	#for prod in Products.PRODUCT_INFO.keys():
	#for prod in range(10):
	#	data = DATA['TextSources'].TextSourceRoots.GetTradeRoute().GetRoute(routeID).GetStation(stationID).GetGood(prod).Guid
		#if data:
			#pass
			#log(data)
			#log(data)
	#station_name = DATA['scenes'].SessionTradeRoutes.Data.StationData[1].StationName
	
	#DATA['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[0].EditRouteClicked()
	#markers = iter(scenes(DATA).StrategicMap.Data.IslandMarker)
	#for marker in markers:
		#log(dir(marker))
		#log(marker.RefGUID)
		#pass
	#data = DATA['TextSources'].TextSourceRoots.GetArea().GetAreaFromID(9026).GetEconomy().GetPopulationCount()
	#data = scenes(DATA).StrategicMap.Data.RouteLines[0].Start
	
	#data = DATA['TextSources'].TextSourceRoots.GetArea().GetCurrent().GetEconomy().CityStatus
	
	#data = DATA['scenes'].StatisticScreen.WarehouseData.WarehouseTradeWrapper[0].TradeHeaderBtnObject.RouteName
	
	#data = DATA['logger'].setLevel(3)
	#openConsole(DATA)
	#getListofHistoricPop(DATA,popIDs)
	data = DATA['game'].crash(True)
	#data = len(data)
	#data = vars(data)
	log(data)
	log(dir(data))
	log(len(data))
	log('\n')


def log(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text)+'\n\n')

def getListofHistoricPop(modules, popIDs):
        for poptype, popID in popIDs.items():
                popvalues = []
                popvalues.append(getHistoricPop(modules, 0, popID))
                i=1
                while getHistoricPop(modules, i, popID) > 0:
                        popvalues.append(getHistoricPop(modules, i, popID))
                        i=i+1
                log(poptype+'\n'+''.join(str(popvalues))+'\n'+'---')
		
def getHistoricPop(modules, snapshotIndex, popID):
        return modules['TextSources'].TextSourceRoots.EconomyStatistic.History.GetPopulationAmount(snapshotIndex,popID)

def openConsole(modules):
	modules['console'].toggleVisibility()
	
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


def listener():
	scenes(DATA).SessionTradeRouteOverview.TradeRouteOverviewObject.RouteDat    
# Notes
def openCharterRoute(modules):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.TransferData[1].RouteButtonClicked()
def openRoute(modules, index):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[index].EditRouteClicked()
def getCargoForLAstSelectedShip():
	DATA['scenes'].ObjectMenuShip.ShipObject.CargoSlotData[0].ItemData.ButtonBehaviour.RefGUID
def openCreateRouteMenu():
	scenes(DATA).SessionTradeRouteOverview.TradeRouteOverviewObject.TradeRouteSelect
def islandCoordinates():
	scenes(DATA).StrategicMap.Data.IslandMarker[0].Position.x
main()

