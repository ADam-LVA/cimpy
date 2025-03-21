from .GeneratingUnit import GeneratingUnit
from .CGMESProfile import Profile


class NuclearGeneratingUnit(GeneratingUnit):
    """
    A nuclear generating unit.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class GeneratingUnit:\n" + GeneratingUnit.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=NuclearGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
