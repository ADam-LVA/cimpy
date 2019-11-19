from cimpy.cimgen_v2_4_15.Equipment.Switch import Switch


class GroundDisconnector(Switch):
	'''
	A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from ground.

		'''

	

	__doc__ += '\n Documentation of parent class Switch: \n' + Switch.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=GroundDisconnector\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
