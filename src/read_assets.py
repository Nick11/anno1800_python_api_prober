class Asset:
	ALL_ASSETS_XPATH = './/Asset'
	GUID_XPATH = 'Values/Standard/GUID'
	NAME_XPATH = 'Values/Standard/Name'
	PRODUCT_SELECTOR_XPATH = '[Template=\'{}\']'
	GUID_SELECTOR_XPATH = '/Values/Standard/[GUID=\'{}\']/../..'

	def __init__(self, filename):
		import xml.etree.ElementTree as ET
		self.asset_tree = ET.parse(filename)
		self.asset_root = self.asset_tree.getroot()
		
	def get_node_xpath(self, root_path, node_path, selector_path = ""):
		return self.asset_root.findall(root_path + selector_path + '/' + node_path)
		
	def get_asset_guids(self):
		return self.get_node_xpath(self.ALL_ASSETS_XPATH, self.GUID_XPATH)
		
	def get_asset_guids_from_template(self, template):
		return self.get_node_xpath(self.ALL_ASSETS_XPATH, self.GUID_XPATH, selector_path = self.PRODUCT_SELECTOR_XPATH.format(template))
	
	def get_product_guids(self):
		return self.get_asset_guids_from_template('Product')
		
	def get_name(self, guid):
		return self.get_node_xpath(self.ALL_ASSETS_XPATH, selector_path = self.GUID_SELECTOR_XPATH.format(guid), node_path = self.NAME_XPATH)