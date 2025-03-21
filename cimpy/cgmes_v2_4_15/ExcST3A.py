from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcST3A(ExcitationSystemDynamics):
    """
    Modified IEEE ST3A static excitation system with added speed multiplier.

    :efdmax: Maximum AVR output (Efdmax).  Typical Value = 6.9. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 1.1. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0
    :ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 0.0
    :kj: AVR gain (Kj).  Typical Value = 200. Default: 0.0
    :km: Forward gain constant of the inner loop field regulator (Km).  Typical Value = 7.04. Default: 0.0
    :kp: Potential source gain (Kp) (>0).  Typical Value = 4.37. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
    :ks1: Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical Value = 0. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 6.67. Default: 0.0
    :tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0.0
    :thetap: Potential circuit phase angle (thetap).  Typical Value = 20. Default: 0.0
    :tm: Forward time constant of inner loop field regulator (Tm).  Typical Value = 1. Default: 0.0
    :vbmax: Maximum excitation voltage (Vbmax).  Typical Value = 8.63. Default: 0.0
    :vgmax: Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53. Default: 0.0
    :vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2. Default: 0.0
    :vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0
    :xl: Reactance associated with potential source (Xl).  Typical Value = 0.09. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdmax": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kj": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "ks1": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "thetap": [Profile.DY.value, ],
        "tm": [Profile.DY.value, ],
        "vbmax": [Profile.DY.value, ],
        "vgmax": [Profile.DY.value, ],
        "vimax": [Profile.DY.value, ],
        "vimin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xl": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdmax = 0.0, kc = 0.0, kg = 0.0, ki = 0.0, kj = 0.0, km = 0.0, kp = 0.0, ks = 0.0, ks1 = 0.0, tb = 0.0, tc = 0.0, thetap = 0.0, tm = 0.0, vbmax = 0.0, vgmax = 0.0, vimax = 0.0, vimin = 0.0, vrmax = 0.0, vrmin = 0.0, xl = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.kc = kc
        self.kg = kg
        self.ki = ki
        self.kj = kj
        self.km = km
        self.kp = kp
        self.ks = ks
        self.ks1 = ks1
        self.tb = tb
        self.tc = tc
        self.thetap = thetap
        self.tm = tm
        self.vbmax = vbmax
        self.vgmax = vgmax
        self.vimax = vimax
        self.vimin = vimin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xl = xl

    def __str__(self):
        str = "class=ExcST3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
