from cimpy.cimgen_v2_4_15.Base import Base


class Source(Base):
	'''
	Source gives information related to the origin of a value.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Source\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
