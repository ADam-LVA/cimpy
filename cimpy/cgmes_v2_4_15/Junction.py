from .Connector import Connector
from .CGMESProfile import Profile


class Junction(Connector):
    """
    A point where one or more conducting equipments are connected with zero resistance.

    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Connector:\n" + Connector.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=Junction\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
