from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssSK(PowerSystemStabilizerDynamics):
    """
    PSS Slovakian type - three inputs.

    :k1: Gain P (K1).  Typical Value = -0.3. Default: 0.0
    :k2: Gain fe (K2).  Typical Value = -0.15. Default: 0.0
    :k3: Gain If (K3).  Typical Value = 10. Default: 0.0
    :t1: Denominator time constant (T1).  Typical Value = 0.3. Default: 0.0
    :t2: Filter time constant (T2).  Typical Value = 0.35. Default: 0.0
    :t3: Denominator time constant (T3).  Typical Value = 0.22. Default: 0.0
    :t4: Filter time constant (T4).  Typical Value = 0.02. Default: 0.0
    :t5: Denominator time constant (T5).  Typical Value = 0.02. Default: 0.0
    :t6: Filter time constant (T6).  Typical Value = 0.02. Default: 0.0
    :vsmax: Stabilizer output max limit (Vsmax).  Typical Value = 0.4. Default: 0.0
    :vsmin: Stabilizer output min limit (Vsmin).  Typical Value = -0.4. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k2": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "vsmax": [Profile.DY.value, ],
        "vsmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, k1 = 0.0, k2 = 0.0, k3 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, vsmax = 0.0, vsmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.vsmax = vsmax
        self.vsmin = vsmin

    def __str__(self):
        str = "class=PssSK\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
