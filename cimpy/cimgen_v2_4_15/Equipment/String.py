from cimpy.cimgen_v2_4_15.Base import Base


class String(Base):
	'''
	A string consisting of a sequence of characters. The character encoding is UTF-8. The string length is unspecified and unlimited.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=String\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
