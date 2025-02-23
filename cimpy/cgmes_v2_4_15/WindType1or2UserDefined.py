from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics
from .CGMESProfile import Profile


class WindType1or2UserDefined(WindTurbineType1or2Dynamics):
    """
    Wind Type 1 or Type 2 function block whose dynamic behaviour is described by

    :ProprietaryParameterDynamics: Parameter of this proprietary user-defined model. Default: "list"
    :proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ProprietaryParameterDynamics": [Profile.DY.value, ],
        "proprietary": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindTurbineType1or2Dynamics:\n" + WindTurbineType1or2Dynamics.__doc__

    def __init__(self, ProprietaryParameterDynamics = "list", proprietary = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ProprietaryParameterDynamics = ProprietaryParameterDynamics
        self.proprietary = proprietary

    def __str__(self):
        str = "class=WindType1or2UserDefined\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
