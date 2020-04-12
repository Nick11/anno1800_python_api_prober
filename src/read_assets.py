class Assets:
	ALL_ASSETS_XPATH = './/Asset'
	GUID_XPATH = 'Values/Standard/GUID'
	NAME_XPATH = 'Values/Standard/Name'
	ENGLISH_TEXT_XPATH = 'Values/Text/LocaText/English/Text'
	TEMPLATE_SELECTOR_XPATH = '[Template=\'{}\']'
	GUID_SELECTOR_XPATH = '/Values/Standard/[GUID=\'{}\']/../..'

	def __init__(self, filename):
		import xml.etree.ElementTree as ET
		self.asset_tree = ET.parse(filename)
		self.asset_root = self.asset_tree.getroot()
		self.assets = {self.get_guid_from_node(x): x for x in self.get_nodes_xpath(self.asset_root, '', self.ALL_ASSETS_XPATH)}
		
		
	def get_guid_from_node(self, node):
		guid_node = self.get_node_xpath(node, self.GUID_XPATH)
		if guid_node is None:
			return None
		else:
			return guid_node.text
		
	def get_nodes_xpath(self, root_node, node_path, root_path = ".", selector_path = ""):
		path = root_path + selector_path
		if node_path != '':
			path += '/' + node_path
		return root_node.findall(path)
		
	def get_node_xpath(self, root_node, node_path, root_path = ".", selector_path = ""):
		nodes = self.get_nodes_xpath(root_node, node_path, root_path, selector_path)
		if len(nodes) == 1:
			return nodes[0]
		else:
			return None
		
	def get_asset_guids(self):
		return [x for x in self.assets.keys()]
		
	def get_asset_nodes_from_template(self, template):
		return [x for x in self.assets.values() if self.get_node_xpath(x, self.GUID_XPATH, self.TEMPLATE_SELECTOR_XPATH.format(template)) is not None]
	
	def get_product_guids(self):
		return [self.get_guid_from_node(x) for x in self.get_asset_nodes_from_template('Product')]
		
	def get_name(self, guid):
		return self.get_node_xpath(self.assets[guid], self.NAME_XPATH).text
		
	def get_english_text(self, guid):
		return self.get_node_xpath(self.assets[guid], self.ENGLISH_TEXT_XPATH).text
		
if __name__ == '__main__':
	assets = Assets('D:/programmieren/anno1800-rda/data0/data/config/export/main/asset/assets.xml')
	
	all_product_guids = assets.get_product_guids()
	
	with open('asset_list.py', 'w') as file:
		file.write('class Products:\n')
		for guid in all_product_guids:
			file.write("    {} = {}\n".format(assets.get_name(guid).upper().replace(' ', '_').replace('-', '_'), guid))
			
		file.write('\n')
		
		file.write("    PRODUCT_INFO = {\n")
		for guid in all_product_guids:
			file.write("        {} : {{ \"name\": \"{}\", \"english_text\" : \"{}\" }},\n".format(guid, assets.get_name(guid), assets.get_english_text(guid)))
		
		file.write("    }\n")
	