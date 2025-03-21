from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from .CGMESProfile import Profile


class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """
    The class represents IEEE PF Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.2.

    :ovex: Overexcitation Flag () true = overexcited false = underexcited. Default: False
    :tpfc: PF controller time delay ().  Typical Value = 5. Default: 0.0
    :vitmin: Minimum machine terminal current needed to enable pf/var controller (). Default: 0.0
    :vpf: Synchronous machine power factor (). Default: 0.0
    :vpfcbw: PF controller dead band ().  Typical Value = 0.05. Default: 0.0
    :vpfref: PF controller reference (). Default: 0.0
    :vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (). Default: 0.0
    :vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ovex": [Profile.DY.value, ],
        "tpfc": [Profile.DY.value, ],
        "vitmin": [Profile.DY.value, ],
        "vpf": [Profile.DY.value, ],
        "vpfcbw": [Profile.DY.value, ],
        "vpfref": [Profile.DY.value, ],
        "vvtmax": [Profile.DY.value, ],
        "vvtmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PFVArControllerType1Dynamics:\n" + PFVArControllerType1Dynamics.__doc__

    def __init__(self, ovex = False, tpfc = 0.0, vitmin = 0.0, vpf = 0.0, vpfcbw = 0.0, vpfref = 0.0, vvtmax = 0.0, vvtmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ovex = ovex
        self.tpfc = tpfc
        self.vitmin = vitmin
        self.vpf = vpf
        self.vpfcbw = vpfcbw
        self.vpfref = vpfref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin

    def __str__(self):
        str = "class=PFVArType1IEEEPFController\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
