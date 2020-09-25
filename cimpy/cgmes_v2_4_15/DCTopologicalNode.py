from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class DCTopologicalNode(IdentifiedObject):
	'''
	DC bus.

	:DCTopologicalIsland:  Default: 
	:DCTerminals: See association end Terminal.TopologicalNode. Default: 
	:DCEquipmentContainer:  Default: 
	:DCNodes: See association end ConnectivityNode.TopologicalNode. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, cgmesProfile.TP.value, ],
						'DCTopologicalIsland': [cgmesProfile.SV.value, ],
						'DCTerminals': [cgmesProfile.TP.value, ],
						'DCEquipmentContainer': [cgmesProfile.TP.value, ],
						'DCNodes': [cgmesProfile.TP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTopologicalIsland = , DCTerminals = , DCEquipmentContainer = , DCNodes = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTopologicalIsland = DCTopologicalIsland
		self.DCTerminals = DCTerminals
		self.DCEquipmentContainer = DCEquipmentContainer
		self.DCNodes = DCNodes
		
	def __str__(self):
		str = 'class=DCTopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
