from .MechanicalLoadDynamics import MechanicalLoadDynamics
from .CGMESProfile import Profile


class MechLoad1(MechanicalLoadDynamics):
    """
    Mechanical load model type 1.

    :a: Speed squared coefficient (a). Default: 0.0
    :b: Speed coefficient (b). Default: 0.0
    :d: Speed to the exponent coefficient (d). Default: 0.0
    :e: Exponent (e). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a": [Profile.DY.value, ],
        "b": [Profile.DY.value, ],
        "d": [Profile.DY.value, ],
        "e": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class MechanicalLoadDynamics:\n" + MechanicalLoadDynamics.__doc__

    def __init__(self, a = 0.0, b = 0.0, d = 0.0, e = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a = a
        self.b = b
        self.d = d
        self.e = e

    def __str__(self):
        str = "class=MechLoad1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
