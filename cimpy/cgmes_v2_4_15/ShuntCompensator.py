from .RegulatingCondEq import RegulatingCondEq
from .CGMESProfile import Profile


class ShuntCompensator(RegulatingCondEq):
    """
    A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

    :SvShuntCompensatorSections: The state for the number of shunt compensator sections in service. Default: None
    :aVRDelay: Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR). Default: 0.0
    :grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded. Default: False
    :maximumSections: The maximum number of sections that may be switched in. Default: 0
    :nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the voltage at which the capacitor is connected to the network. Default: 0.0
    :normalSections: The normal number of sections switched in. Default: 0
    :sections: Shunt compensator sections in use. Starting value for steady state solution. Non integer values are allowed to support continuous variables. The reasons for continuous value are to support study cases where no discrete shunt compensators has yet been designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for a continuous solution as input. Default: 0.0
    :switchOnCount: The switch on count since the capacitor count was last reset or initialized. Default: 0
    :switchOnDate: The date and time when the capacitor bank was last switched on. Default: ''
    :voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "SvShuntCompensatorSections": [Profile.SV.value, ],
        "aVRDelay": [Profile.EQ.value, ],
        "grounded": [Profile.EQ.value, ],
        "maximumSections": [Profile.EQ.value, ],
        "nomU": [Profile.EQ.value, ],
        "normalSections": [Profile.EQ.value, ],
        "sections": [Profile.SSH.value, ],
        "switchOnCount": [Profile.EQ.value, ],
        "switchOnDate": [Profile.EQ.value, ],
        "voltageSensitivity": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class RegulatingCondEq:\n" + RegulatingCondEq.__doc__

    def __init__(self, SvShuntCompensatorSections = None, aVRDelay = 0.0, grounded = False, maximumSections = 0, nomU = 0.0, normalSections = 0, sections = 0.0, switchOnCount = 0, switchOnDate = '', voltageSensitivity = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SvShuntCompensatorSections = SvShuntCompensatorSections
        self.aVRDelay = aVRDelay
        self.grounded = grounded
        self.maximumSections = maximumSections
        self.nomU = nomU
        self.normalSections = normalSections
        self.sections = sections
        self.switchOnCount = switchOnCount
        self.switchOnDate = switchOnDate
        self.voltageSensitivity = voltageSensitivity

    def __str__(self):
        str = "class=ShuntCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
