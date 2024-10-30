from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class Location(IdentifiedObject):
    """
    The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.

    :CoordinateSystem: Coordinate system used to describe position points of this location. Default: None
    :PositionPoints: Sequence of position points describing this location, expressed in coordinate system `Location.CoordinateSystem`. Default: "list"
    :PowerSystemResources: All power system resources at this location. Default: None
    """

    possibleProfileList = {
        "class": [Profile.GL.value, ],
        "CoordinateSystem": [Profile.GL.value, ],
        "PositionPoints": [Profile.GL.value, ],
        "PowerSystemResources": [Profile.GL.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.GL.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, CoordinateSystem = None, PositionPoints = "list", PowerSystemResources = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.CoordinateSystem = CoordinateSystem
        self.PositionPoints = PositionPoints
        self.PowerSystemResources = PowerSystemResources

    def __str__(self):
        str = "class=Location\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
