from cimpy.cimgen_v2_4_15.Base import Base


class ResistancePerLength(Base):
	'''
	Resistance (real part of impedance) per unit of length.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
	:denominatorUnit:  Default: None
	:denominatorMultiplier:  Default: None
		'''

	

	

	def __init__(self, value = 0.0, unit = None, multiplier = None, denominatorUnit = None, denominatorMultiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		self.denominatorUnit = denominatorUnit
		self.denominatorMultiplier = denominatorMultiplier
		
	def __str__(self):
		str = 'class=ResistancePerLength\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
