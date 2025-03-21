from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcST6B(ExcitationSystemDynamics):
    """
    Modified IEEE ST6B static excitation system with PID controller and optional inner feedbacks loop.

    :ilr: Exciter output current limit reference (Ilr).  Typical Value = 4.164. Default: 0.0
    :k1: Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical Value = true. Default: False
    :kcl: Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577. Default: 0.0
    :kff: Pre-control gain constant of the inner loop field regulator (Kff).  Typical Value = 1. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 0.0
    :kia: Voltage regulator integral gain (Kia).  Typical Value = 45.094. Default: 0.0
    :klr: Exciter output current limit adjustment (Kcl).  Typical Value = 17.33. Default: 0.0
    :km: Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1. Default: 0.0
    :kpa: Voltage regulator proportional gain (Kpa).  Typical Value = 18.038. Default: 0.0
    :kvd: Voltage regulator derivative gain (Kvd).  Typical Value = 0. Default: 0.0
    :oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: None
    :tg: Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02. Default: 0.0
    :ts: Rectifier firing time constant (Ts).  Typical Value = 0. Default: 0.0
    :tvd: Voltage regulator derivative gain (Tvd).  Typical Value = 0. Default: 0.0
    :vamax: Maximum voltage regulator output (Vamax).  Typical Value = 4.81. Default: 0.0
    :vamin: Minimum voltage regulator output (Vamin).  Typical Value = -3.85. Default: 0.0
    :vilim: Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical Value = true. Default: False
    :vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0
    :vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0
    :vmult: Selector (Vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator output by terminal voltage.  Typical Value = true. Default: False
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 4.81. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -3.85. Default: 0.0
    :xc: Excitation source reactance (Xc).  Typical Value = 0.05. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ilr": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "kcl": [Profile.DY.value, ],
        "kff": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "kia": [Profile.DY.value, ],
        "klr": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "kpa": [Profile.DY.value, ],
        "kvd": [Profile.DY.value, ],
        "oelin": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "ts": [Profile.DY.value, ],
        "tvd": [Profile.DY.value, ],
        "vamax": [Profile.DY.value, ],
        "vamin": [Profile.DY.value, ],
        "vilim": [Profile.DY.value, ],
        "vimax": [Profile.DY.value, ],
        "vimin": [Profile.DY.value, ],
        "vmult": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xc": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ilr = 0.0, k1 = False, kcl = 0.0, kff = 0.0, kg = 0.0, kia = 0.0, klr = 0.0, km = 0.0, kpa = 0.0, kvd = 0.0, oelin = None, tg = 0.0, ts = 0.0, tvd = 0.0, vamax = 0.0, vamin = 0.0, vilim = False, vimax = 0.0, vimin = 0.0, vmult = False, vrmax = 0.0, vrmin = 0.0, xc = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ilr = ilr
        self.k1 = k1
        self.kcl = kcl
        self.kff = kff
        self.kg = kg
        self.kia = kia
        self.klr = klr
        self.km = km
        self.kpa = kpa
        self.kvd = kvd
        self.oelin = oelin
        self.tg = tg
        self.ts = ts
        self.tvd = tvd
        self.vamax = vamax
        self.vamin = vamin
        self.vilim = vilim
        self.vimax = vimax
        self.vimin = vimin
        self.vmult = vmult
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xc = xc

    def __str__(self):
        str = "class=ExcST6B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
