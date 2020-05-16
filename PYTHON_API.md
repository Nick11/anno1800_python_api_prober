# About GUIDs
Find the GUIDs in the gamedata/Data0.rda asset.xml file. (See README)

# Existing modules
List of all available modules:

**Intersting ones**
- 'TextSources': <module 'TextSources' (built-in)>,
- 'scenes': <system.emptyObject object at 0x000002A1E53B6438>,
- 'system': <module 'system' (data/script/system/__init__.py)>,
- 'session': <Anno6.Session object at 0x000002A1E539E0D8>,
- 'gameevents': <Anno6.GameEvents object at 0x000002A1E539E0A0>,
- 'game': <Anno6.Game object at 0x000002A1E539E030>,

**UI**

- 'uiclasses': <module 'uiscenes' (built-in)>,
- 'ui': <Anno6.UI object at 0x000002A1E539E148>,

**Dev Tools and Game Management (boring)**
- 'debug': <Anno6.Debug object at 0x000002A1E539E378>,
- 'onlineManager': <anno7.COnlineManager object at 0x000002A1E539E650>,
- 'anno7': <module 'anno7' (built-in)>,
- 'utils': <Anno6.Utils object at 0x000002A1E539E308>,
- 'logger': <Anno6.Logger object at 0x000002A1E539E228>,
- 'console': <Anno6.Console object at 0x000002A1E0430E68>,
- 'net': <Anno6.Net object at 0x000002A1E539E1B8>,
- 'render': <Anno6.Render object at 0x000002A1E539E298>,

**No idea**

- 'rdgs::SessionTime': <class '__main__.rdgs::SessionTime'>,
- 'rdgs::ProductGUID': <class '__main__.rdgs::ProductGUID'>,
- 'rdgs::ProductAmount': <class '__main__.rdgs::ProductAmount'>,
- 'rdgs::CorporationTime': <class '__main__.rdgs::CorporationTime'>,
- 'rdgs::BuildingOrCraftableGUID': <class '__main__.rdgs::BuildingOrCraftableGUID'>,
- 'rdgs::CraftableGUID': <class '__main__.rdgs::CraftableGUID'>,
- 'rdmath': <module 'rdmath' (built-in)>,
- 'rdsdk::CRDString': <class '__main__.rdsdk::CRDString'>,

## gameevents

Events, would be nice, if we could get notified when they are fired...

[onAssetCreated', 'onAssetRemoved', 'onAssetWatcherDone', 'onCameraSequenceEnd', 'onCameraSequenceMetaEnd', 'onCameraSequenceMetaPause', 'onCameraSequenceMetaStart', 'onChangeSelection', 'onDataReload', 'onDataUnload', 'onGUIAction', 'onGUIDUnlocked', 'onGUITimer', 'onGameTimer', 'onObjectBuilt', 'onObjectDestroyed', 'onObjectGUIDChanged', 'onObjectSelected', 'onQuestObjectCollected', 'onQuestResolved', 'onQuestStarted', 'onRenderTimer', 'onSessionEnter', 'onSessionLeave', 'onSessionLoad', 'onSessionLoaded', 'onSessionUnloaded', 'onSystemLoaded']

## debug

Debugging tools I assume?

['changeOwnerOfSelected', 'failProtectionTrigger', 'forceAddOwnership', 'forceRemoveOwnership', 'showConditionTree', 'showConditionType', 'showVariableOptions', 'toggleOwnership']

## onlineManager

Connection and Session

['AutoConnect', 'DebugCopyHostDescriptorToClipboard', 'DebugCreateCustomSession', 'DebugKickPeer', 'EnableService', 'Get', 'GetStormManager', 'InviteFriend', 'JoinSession', 'LeaveSession', 'LoadMultiplayerSession', 'LoadSavegameAndLeaveSession', 'OpenHelpPage', 'SendTestBlob', 'ShowInviteOverlay', 'UploadFile']

## game

Camera, Time, Loading, UI and sound

['changeRotation', 'changeVariation', 'crash', 'destructObjectGroup', 'enableRenderCommands', 'enableResidentView', 'environmentSetRainDensity', 'environmentSetSnowDensity', 'environmentSetWindDir', 'executeDelayed', 'fastQuit', 'gainAchievement', 'gainRandomAchievement', 'getSessionTime', 'increaseTimeOfDay', 'initRandomSeed', 'isSessionLoadingDone', 'openDebugInfoPage', 'playCameraSequenceSound', 'playSound', 'printCallstack', 'reloadAssetInfos', 'reloadData', 'replaceMainModulePyBind11', 'resetGameCamera', 'restoreCameraView', 'restoreCameraViewAndRotate', 'restoreCameraViewAndRotateFromCurrentRotation', 'rotateCameraAroundLookAt', 'rotateCameraAroundLookAtWithDuration', 'rotateCameraAroundObject', 'rotateCameraAroundObjectWithDuration', 'setBenchTag', 'setMasterVolume', 'setMusicVolume', 'setNewSampling', 'setPostEffectEnabled', 'setSFXVolume', 'simulateWindowClose', 'soundEmitterPositionOffset', 'startBuild', 'startBuildCheat', 'startBuildModule', 'startBuildMove', 'startFAProfileStream', 'startLoopSequence', 'startMouseMode', 'stopFAProfileStream', 'stopSound', 'storeCameraView', 'takeScreenshot', 'testTimeQueue', 'toggleBlueprintMode', 'toggleFrameCaptureMode', 'toggleLensFlarePostEffect', 'toggleLightBoundToCamera', 'togglePortraitEditor', 'toggleTelemetry', 'toggleTextSourceResolving', 'toggleTickDayTime', 'toggleVersionLabel', 'toggleVideoPortraitEditor', 'useDebugGameSetup', 'waitForEvent', 'writeMemorySnapshot']

## anno7

Online and Voice-Chat related things? boring...

['COnlineManager', 'CStormManager', 'CVoiceChat']

## utils

[generatePopupHTML']

## TextSources

This is the cool stuff.
Get and Set the game-state values.


['CAICheatHandlerTextSource', 'CAIConstructionManagerTextSource', 'CAIGlobalCheatHandlerTextSource', 'CAIMetaShipHandlerTextSource', 'CAIUnitManagerTextSource', 'CAccountSettingsTextSource', 'CAchievementAssetTextSource', 'CAchievementManagerTextSource', 'CActiveTradeManagerTextSource', 'CActiveTradeOfferTextSource', 'CAnimalManagerTextSource', 'CAreaAttractivityManagerTextSource', 'CAreaEconomyTextSource', 'CAreaFestivalManagerTextSource', 'CAreaFetchManagerTextSource', 'CAreaHappinessManagerTextSource', 'CAreaLoaderTextSource', 'CAreaManagerTextSource', 'CAreaMoneyManagerTextSource', 'CAreaNeedUnlockManagerTextSource', 'CAreaObjectManagerTextSource', 'CAreaPopulationManagerTextSource', 'CAreaProductDeltaManagerTextSource', 'CAreaRailwayManagerTextSource', 'CAreaResidenceConsumptionManagerTextSource', 'CAreaVisitorsTextSource', 'CAssetTextSource', 'CBlueprintManagerTextSource', 'CBuildCostEntryTextSource', 'CBuildCostTextSource', 'CBuildModeManagerTextSource', 'CBuildModeObjectTextSource', 'CCheatManagerTextSource', 'CConditionGoodsInRangeBaseTextSource', 'CConditionGoodsInRangeTextSource', 'CConditionInStorageTextSource', 'CConditionItemActionCompletedTextSource', 'CConditionItemUsedTextSource', 'CConditionManagerTextSource', 'CConditionModuleBuildingEfficiencyTextSource', 'CConditionMoveVehicleTextSource', 'CConditionObjectSelectedTextSource', 'CConditionPhotographObjectTextSource', 'CConditionPlayerCounterTextSource', 'CConditionQuestBringVehicleToObjectTextSource', 'CConditionQuestDestroyTextSource', 'CConditionQuestEscortTextSource', 'CConditionQuestExpeditionTextSource', 'CConditionQuestFollowShipTextSource', 'CConditionQuestHitMovingTargetTextSource', 'CConditionQuestSmugglerTextSource', 'CConditionQuestSustainTextSource', 'CConditionQuestUseItemInAreaTextSource', 'CConditionShipsInRangeBaseTextSource', 'CConditionShipsInRangeTextSource', 'CConditionTextSource', 'CConditionTimerTextSource', 'CConstructionAreaTextSource', 'CCorporationDlcUpgradeManagerTextSource', 'CCorporationStatsTextSource', 'CDaytimeManagerTextSource', 'CDebugRenderManagerTextSource', 'CDesyncRecoverFlowTextSource', 'CDifficultyHelperTextSource', 'CDiscoveryManagerTextSource', 'CEconomyManagerTextSource', 'CEconomyStatisticManagerTextSource', 'CExpeditionTextSource', 'CFactoryAssetTextSource', 'CFetchSavegameFlowTextSource', 'CFullscreenMovieQueueManagerTextSource', 'CGUIManagerTextSource', 'CGameClockTextSource', 'CGameHelperClassesTextSource', 'CGameManagerTextSource', 'CGameObjectManagerTextSource', 'CGameObjectTextSource', 'CGameSetupManagerTextSource', 'CGameToolOneDataHelperTextSource', 'CGenericPopupManagerTextSource', 'CGlobalCheatsTextSource', 'CHappyDayEventManagerTextSource', 'CIncidentChanceSourceDescTextSource', 'CIncidentChancesTextSource', 'CIncidentManagerTextSource', 'CInfoTipContextValueTextSource', 'CInfoTipManagerTextSource', 'CInputManagerTextSource', 'CItemAssetTextSource', 'CItemSessionManagerTextSource', 'CLoadingPierManagerTextSource', 'CLocaHelperTextSource', 'CLogisticNodeTextSource', 'CMetaEconomyTextSource', 'CMetaGameLoaderTextSource', 'CMetaGameManagerTextSource', 'CMetaGameObjectManagerTextSource', 'CMetaGameObjectTextSource', 'CMetaIncidentManagerTextSource', 'CMetaMoneyManagerTextSource', 'CMetaPropertyBuildPermitsTextSource', 'CMetaPropertyBuySharesTextSource', 'CMetaPropertyConstructionAITextSource', 'CMetaPropertyDiplomacyTextSource', 'CMetaPropertyExpeditionUserTextSource', 'CMetaPropertyInfluenceTextSource', 'CMetaPropertyKontorOwnerTextSource', 'CMetaPropertyProfileCounterTextSource', 'CMetaPropertyProfileTextSource', 'CMilitaryManagerTextSource', 'CNewspaperArticleTextSource', 'CNewspaperContextTextSource', 'CNewspaperEffectDescTextSource', 'CNewspaperManagerTextSource', 'CNewspaperTextSource', 'CNotRenovatableContextTextSource', 'CNotUpgradableContextTextSource', 'CNotificationManagerTextSource', 'CNotificationTypeCharacterTextSource', 'COMOfferTextSource', 'COMTradeActiveTextSource', 'COMTradeBoughtTextSource', 'COnlineEventManagerTextSource', 'COnlineEventQuestHandlerTextSource', 'COnlineInventoryManagerTextSource', 'COnlineManagerTextSource', 'COnlineMarketManagerTextSource', 'COptionsManagerTextSource', 'COverlayDebugPalaceTextSource', 'CPalaceDecreeAssetTextSource', 'CParticipantManagerTextSource', 'CPassiveTradeControllerTextSource', 'CPassiveTradeOfferTextSource', 'CPathManagerTextSource', 'CPauseManagerTextSource', 'CPlatformDispatchManagerTextSource', 'CPopulationAssetTextSource', 'CPopulationStatisticsTextSource', 'CProductAmountTextSource', 'CProductAssetTextSource', 'CProductionStatisticsTextSource', 'CPropertyAttackableTextSource', 'CPropertyAttackerTextSource', 'CPropertyBuildingTextSource', 'CPropertyCollectableTextSource', 'CPropertyCommandQueueTextSource', 'CPropertyConstructionAITextSource', 'CPropertyCultureTextSource', 'CPropertyDelayedConstructionTextSource', 'CPropertyDistributionTextSource', 'CPropertyDyingTextSource', 'CPropertyElectricTextSource', 'CPropertyFactory7TextSource', 'CPropertyFreeAreaProductivityTextSource', 'CPropertyIncidentInfectableTextSource', 'CPropertyIncidentResolverTextSource', 'CPropertyInfluenceSourceTextSource', 'CPropertyItemContainerTextSource', 'CPropertyItemCrafterTextSource', 'CPropertyLifetimeTextSource', 'CPropertyMaintenanceTextSource', 'CPropertyMeshTextSource', 'CPropertyMetaPersistentTextSource', 'CPropertyModuleOwnerTextSource', 'CPropertyMonumentTextSource', 'CPropertyNameableTextSource', 'CPropertyPalaceMinistryTextSource', 'CPropertyPalaceTextSource', 'CPropertyPausableTextSource', 'CPropertyPirateTextSource', 'CPropertyRepairCraneTextSource', 'CPropertyResidence7TextSource', 'CPropertySelectionTextSource', 'CPropertySellableTextSource', 'CPropertyShipIncidentTextSource', 'CPropertyShipMaintenanceTextSource', 'CPropertyShipyardTextSource', 'CPropertyTradeRouteVehicleTextSource', 'CPropertyTraderTextSource', 'CPropertyVisitorHarborTextSource', 'CPropertyWalkingTextSource', 'CPropertyWarehouseTextSource', 'CQuestInstanceTextSource', 'CQuestManagerTextSource', 'CRecordingManagerTextSource', 'CRecordingPlayerTextSource', 'CRegrowManagerTextSource', 'CRenovatabilityCheckerTextSource', 'CRewardsManagerTextSource', 'CSelectionGroupControllerTextSource', 'CSelectionManagerTextSource', 'CSessionCameraManagerTextSource', 'CSessionCoastManagerTextSource', 'CSessionFeedbackManagerTextSource', 'CSessionFreeAreaProductivityManagerTextSource', 'CSessionParticipantManagerTextSource', 'CSessionRandomManagerTextSource', 'CSessionTradeRouteGoodInfoTextSource', 'CSessionTradeRouteStationInfoTextSource', 'CSessionTradeRouteTextSource', 'CSessionTransferManagerTextSource', 'CShipFleetTextSource', 'CSoundManagerTextSource', 'CStatisticsHistoryDataTextSource', 'CStreetOverlayManagerTextSource', 'CTargetManagerTextSource', 'CTextManagerTextSource', 'CTextSourceListValueTextSource', 'CTextSourceManagerTextSource', 'CTextSourceObjectWrapperTextSource', 'CTextSourceUtilityTextSource', 'CToolOneManagerTextSource', 'CToolOneTextHelperTextSource', 'CTradeOfferInfoTextSource', 'CTradeRouteManagerTextSource', 'CTransporterQueueTextSource', 'CUIBindingsTextSource', 'CUnlockManagerTextSource', 'CUpgradabilityCheckerTextSource', 'CVisitorManagerTextSource', 'CVoiceChatTextSource', 'CWeatherManagerTextSource', 'CWinLoseManagerTextSource', 'CWorkforceIslandTransferTextSource', 'CWorkforceMapTextSource', 'CWorkforceTransferManagerTextSource', 'CWorldMapSessionManagerTextSource', 'IConditionEventTextSource', 'IIncidentTextSource', 'ILogisticNodeTextSource', 'INotificationTextSource', 'IncidentResolverStateTextSource', 'TextSourceRoots', 'VirtualSpaceBuildCostTextSource', 'VirtualSpaceBuildingTextSource', 'VirtualSpaceDistributionTextSource', 'VirtualSpaceElectricityTextSource', 'VirtualSpaceExpeditionTextSource', 'VirtualSpaceFactoryTextSource', 'VirtualSpaceHeatProviderTextSource', 'VirtualSpaceHeatTextSource', 'VirtualSpaceMaintenanceTextSource', 'VirtualSpaceStaticDataTextSource', 'VirtualSpaceTradeTextSource', 'VirtualSpaceUniqueBuildingsTextSource', 'VirtualSpaceWarehouseTextSource']

### TextSourceRoots

Looks like the most promissing starting point.

- TextSourceRoots.EconomyStatistic.GetProductionStatistic().GetProductGeneration(productGUID: Int): Global production of resource with GUID productID

['AccountSettings', 'Achievements', 'ActiveTrade', 'AiConstruction', 'AiUnit', 'Animals', 'Area', 'AreaCoast', 'AreaFetch', 'AreaManager', 'AreaNeedUnlock', 'AreaPopulation', 'AreaProductDelta', 'AreaResidenceConsumption', 'Attractivity', 'Blueprint', 'BuildMode', 'BuildPermits', 'Cheat', 'Conditions', 'Daytime', 'DebugRender', 'DesyncRecover', 'DifficultyHelper', 'Discovery', 'DlcUpgrade', 'Economy', 'EconomyStatistic', 'Expedition', 'Feedback', 'FreeAreaProductivity', 'FullscreenMovieQueueManager', 'GUI', 'Game', 'GameClock', 'GameSetup', 'GetAccountSettings', 'GetAchievementAssetData', 'GetAchievements', 'GetActiveTrade', 'GetAiConstruction', 'GetAiUnit', 'GetAnd', 'GetAnimals', 'GetArea', 'GetAreaCoast', 'GetAreaFetch', 'GetAreaManager', 'GetAreaNeedUnlock', 'GetAreaPopulation', 'GetAreaProductDelta', 'GetAreaResidenceConsumption', 'GetAssetData', 'GetAssetForValue', 'GetAttractivity', 'GetBlueprint', 'GetBuildMode', 'GetBuildPermits', 'GetCheat', 'GetConditions', 'GetDaytime', 'GetDebugRender', 'GetDesyncRecover', 'GetDifficultyHelper', 'GetDiscovery', 'GetDlcUpgrade', 'GetEconomy', 'GetEconomyStatistic', 'GetExpedition', 'GetFactoryAssetData', 'GetFeedback', 'GetFestivalManager', 'GetFreeAreaProductivity', 'GetFullscreenMovieQueueManager', 'GetGUI', 'GetGame', 'GetGameClock', 'GetGameSetup', 'GetGreater', 'GetHappiness', 'GetHappyDayEventManager', 'GetIncidents', 'GetInfoTip', 'GetInputManager', 'GetInterface', 'GetItem', 'GetItemAssetData', 'GetLoadingPier', 'GetMetaGameManager', 'GetMetaIncidents', 'GetMetaInfluence', 'GetMetaObjects', 'GetMilitary', 'GetMoney', 'GetNewspaper', 'GetNot', 'GetNotifications', 'GetObjects', 'GetOnline', 'GetOnlineEvents', 'GetOnlineInventory', 'GetOnlineMarket', 'GetOptions', 'GetPalace', 'GetPalaceDecreeData', 'GetParticipants', 'GetPath', 'GetPause', 'GetPlatformDispatch', 'GetPopulationAssetData', 'GetPopup', 'GetProductAssetData', 'GetQuests', 'GetRailway', 'GetRandom', 'GetRecords', 'GetRefGuid', 'GetRefOid', 'GetRegrow', 'GetRewards', 'GetSavegameFetcher', 'GetSelection', 'GetSessionCamera', 'GetSessionParticipants', 'GetSessionTransfer', 'GetSound', 'GetStaticData', 'GetStreetOverlay', 'GetTarget', 'GetText', 'GetTextSourceManager', 'GetToolOneDataHelper', 'GetToolOneHelper', 'GetToolOneManager', 'GetTradeRoute', 'GetUnlock', 'GetVisitors', 'GetWeather', 'GetWinLose', 'GetWorkforceTransferManager', 'GetWorldMap', 'Happiness', 'HappyDayEventManager', 'Incidents', 'InfoTip', 'InputManager', 'Interface', 'Item', 'LoadingPier', 'MetaGameManager', 'MetaIncidents', 'MetaInfluence', 'MetaObjects', 'Military', 'Money', 'Newspaper', 'Notifications', 'Objects', 'Online', 'OnlineEvents', 'OnlineInventory', 'OnlineMarket', 'Options', 'Palace', 'Participants', 'Path', 'Pause', 'PlatformDispatch', 'Popup', 'Quests', 'Railway', 'Random', 'Records', 'RefGuid', 'RefOid', 'Regrow', 'Rewards', 'SavegameFetcher', 'Selection', 'SessionCamera', 'SessionParticipants', 'SessionTransfer', 'Sound', 'StaticData', 'StreetOverlay', 'Target', 'Text', 'TextSourceManager', 'ToggleDebugInfo', 'ToolOneDataHelper', 'ToolOneHelper', 'ToolOneManager', 'TradeRoute', 'Unlock', 'Visitors', 'Weather', 'WinLose', 'WorkforceTransferManager', 'WorldMap']

## session

Manipulation of the "world"?


['addReputation', 'aiDebugRenderContext', 'buildShipInBuilding', 'cameraFOV', 'cameraFarClip', 'changeTestNegotiation', 'createTestStreetGridTiles', 'daytime', 'deactivateSpecialCameraView', 'destroySelectionNextGametick', 'drawDebugLayer', 'drawPathplannerLayer', 'enableAllConstructionAreas', 'executeBuildModeEvent', 'executeBuildStreetEvent', 'executeTargetManagerEvent', 'executeWorldMapEvent', 'feedbackForceFieldRadiusHard', 'feedbackForceFieldRadiusSoft', 'feedbackForceFieldSpeed', 'feedbackSetDebugMode', 'feedbackSetDebugRenderMode', 'feedbackToggleDebugFlag', 'fireExplodingProjectile', 'fireProjectile', 'forceSequenceCamera', 'forceWeather', 'getNearestLabelAtCameraPos', 'getObject', 'getObjectByID', 'getObjectByLabel', 'getObjectGroupByName', 'getObjectGroupByObject', 'getSelectedFactory', 'getSessionGUID', 'hasNeverBeenEntered', 'hideDebugLayers', 'hideStreets', 'hideTestRandomArea', 'increaseDangerLayer', 'isNewSession', 'jumpToSelection', 'killGameObject', 'listenerPositionInterpolationValue', 'morale', 'openInfoTip', 'openSelectedObject', 'openSelectedObjectInToolOne', 'preloadObject', 'recordCameraSequence', 'selectNextObject', 'selection', 'setCameraToObjectPosAndRot', 'setCameraToPreset', 'setDefaultRotation', 'setSelectionRectMode', 'setStance', 'showAllCollectables', 'showStreet', 'showStreets', 'showTestRandomArea', 'spawnDebugGameObject', 'squadAddDestroyTask', 'squadAddRouteTask', 'startCameraShake', 'startDiplomacyMenu', 'startFeedbackSequence', 'startIslandSequence', 'startNegotiationMenu', 'startSequence', 'startTestNegotiation', 'stopSequence', 'switchCameraControl', 'toggleAIDebug', 'toggleCamSettings', 'toggleDrawDistanceToIslandLayer', 'togglePostcardView', 'unloadSession']


## scenes
These might be the different screens/Overlays

- scenes.SessionTradeRouteOverview.TradeRouteOverviewObject: array of all trade routes
- scenes.SessionTradeRoutes.Data.StationData: Array of routes stations.
- scenes.SessionTradeRouteOverview.TradeRouteOverviewObject.TransferData: Charter routes
- scenes.SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData: "Handelsrouten"

['Achievement', 'ActiveTrade', 'AdvanceDifficulties', 'AttractivenessPopup', 'BrowserDebug', 'CampaignNewspaper', 'CampaignNotifications', 'CharacterNotifications', 'ChatNotification', 'ChatWindow', 'ConfirmationMenu', 'ConstructionBar', 'CraftingPopup', 'CreateGame', 'Credits', 'CulturalBuildingPopup', 'DLCOverview', 'DLCPromotionPopup', 'DLCUpdate', 'Desync', 'Difficulties', 'DifficultyUpgrade', 'Diplomacy', 'Drag', 'EpilepsyWarning', 'ErrorMessage', 'ExpeditionEvent', 'ExpeditionOverview', 'FadeTransition', 'Feedback', 'GameBlur', 'GameModeSelection', 'GameOver', 'Hint', 'HostileTakeOver', 'IconInfolayer', 'InfluencePopup', 'Intro', 'IslandBar', 'Letterbox', 'Loader', 'Loading', 'MPGameModeSelection', 'MPLobbyCoop', 'MPNotification', 'MPQuickJoinLobby', 'MPQuickJoinWidget', 'MPQuickMatch', 'MPSessionBrowser', 'MPSessionCreate', 'MPWaitingForMatch', 'MainNotifications', 'MetaBackground', 'MilitaryResult', 'Minimap', 'NavigationMenu', 'NewSettingUpdate', 'Newspaper', 'NewspaperSpecialEdition', 'NonModalPopup', 'ObjectMenuBluePrint', 'ObjectMenuCityInstitution', 'ObjectMenuCoalOilHarbour', 'ObjectMenuCommuterHarbour', 'ObjectMenuCultureBuilding', 'ObjectMenuDepartment', 'ObjectMenuForeign', 'ObjectMenuGeneric', 'ObjectMenuGuildHouse', 'ObjectMenuHangar', 'ObjectMenuHarbour', 'ObjectMenuKontor', 'ObjectMenuMarketplace', 'ObjectMenuMausoleum', 'ObjectMenuMilitary', 'ObjectMenuModule', 'ObjectMenuMonument', 'ObjectMenuMonumentEvent', 'ObjectMenuOrnamental', 'ObjectMenuPalace', 'ObjectMenuProduction', 'ObjectMenuPublicService', 'ObjectMenuResidence', 'ObjectMenuShip', 'ObjectMenuShipYard', 'ObjectMenuSpecialist', 'ObjectMenuTrader', 'ObjectMenuTraderOldNate', 'ObjectMenuVisitorHarbor', 'ObjectMenuWarehouse', 'OnScreenHP', 'OnScreenIcon', 'OnScreenProgress', 'OnScreenText', 'Options', 'Palace', 'PauseExplanation', 'PauseMenu', 'PeakEasterEgg', 'PhoenixExport', 'PhotoMarker', 'PostcardExplanation', 'ProfileSelection', 'QuestBook', 'QuestTracker', 'QuickNavigationMap', 'ResourceBar', 'RightclickMenu', 'SaveDialog', 'ScreenCapture', 'Session', 'SessionTradeRouteOverview', 'SessionTradeRoutes', 'SessionTradeTransfer', 'SideNotificationArchives', 'SideNotifications', 'StartMenuVideo', 'StatisticScreen', 'StrategicMap', 'Subtitles', 'Survey', 'SystemBackground', 'SystemPopup', 'TextPopup', 'Title', 'Tooltip', 'TransferGoodsMenu', 'TreasureMap', 'UIPlayground', 'Unloading', 'UplayAction', 'VersionLabel', 'Video', 'VideoBackground', 'WorldMap']

### SessionTradeRouteOverview
Data for the trade route overviewscreen
[SceneTransition', 'TradeRouteOverviewObject']

#### TradeRouteOverviewObject
Data for trade(trade) and charter(transfere) routes

['CloseButtonReleased', 'CoopActiveMarkerData', 'CreateRouteDisabled', 'CreateRouteReleased', 'HasNoCharterRouteSearchResult', 'HasNoTradeRouteSearchResult', 'IsRemoveBtnVisible', 'RemoveSearchTermReleaseEvent', 'RouteData', 'SearchFilter', 'TradeRouteSelect', 'TransferData]

##### RouteData

Array, its elements contain:

['ActiveShips', 'DeleteRouteClicked', 'EditRouteClicked', 'GeneralErrorWarning', 'GoodIcons', 'HasStoppedTrading', 'MouseEntered', 'MouseLeft', 'NoShipsAssigned', 'NotificationAllShipsPaused', 'PausedShips', 'RouteID', 'RouteName', 'WarningNoGoods', 'WarningNoShips']


