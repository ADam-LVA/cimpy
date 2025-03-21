from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssIEEE4B(PowerSystemStabilizerDynamics):
    """
    The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.

    :bwh1: Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 0.0
    :bwh2: Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 0.0
    :bwl1: Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 0.0
    :bwl2: Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 0.0
    :kh: High band gain (K).  Typical Value = 120. Default: 0.0
    :kh1: High band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :kh11: High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :kh17: High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :kh2: High band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :ki: Intermediate band gain (K).  Typical Value = 30. Default: 0.0
    :ki1: Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :ki11: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :ki17: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :ki2: Intermediate band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :kl: Low band gain (K).  Typical Value = 7.5. Default: 0.0
    :kl1: Low band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :kl11: Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :kl17: Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 0.0
    :kl2: Low band differential filter gain (K).  Typical Value = 66. Default: 0.0
    :omeganh1: Notch filter 1 (high-frequency band): filter frequency (omega). Default: 0.0
    :omeganh2: Notch filter 2 (high-frequency band): filter frequency (omega). Default: 0.0
    :omeganl1: Notch filter 1 (low-frequency band): filter frequency (omega). Default: 0.0
    :omeganl2: Notch filter 2 (low-frequency band): filter frequency (omega). Default: 0.0
    :th1: High band time constant (T).  Typical Value = 0.01513. Default: 0.0
    :th10: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th11: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th12: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th2: High band time constant (T).  Typical Value = 0.01816. Default: 0.0
    :th3: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th4: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th5: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th6: High band time constant (T).  Typical Value = 0. Default: 0.0
    :th7: High band time constant (T).  Typical Value = 0.01816. Default: 0.0
    :th8: High band time constant (T).  Typical Value = 0.02179. Default: 0.0
    :th9: High band time constant (T).  Typical Value = 0. Default: 0.0
    :ti1: Intermediate band time constant (T).  Typical Value = 0.173. Default: 0.0
    :ti10: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti11: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti12: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti2: Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0.0
    :ti3: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti4: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti5: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti6: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :ti7: Intermediate band time constant (T).  Typical Value = 0.2075. Default: 0.0
    :ti8: Intermediate band time constant (T).  Typical Value = 0.2491. Default: 0.0
    :ti9: Intermediate band time constant (T).  Typical Value = 0. Default: 0.0
    :tl1: Low band time constant (T).  Typical Value = 1.73. Default: 0.0
    :tl10: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl11: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl12: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl2: Low band time constant (T).  Typical Value = 2.075. Default: 0.0
    :tl3: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl4: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl5: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl6: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :tl7: Low band time constant (T).  Typical Value = 2.075. Default: 0.0
    :tl8: Low band time constant (T).  Typical Value = 2.491. Default: 0.0
    :tl9: Low band time constant (T).  Typical Value = 0. Default: 0.0
    :vhmax: High band output maximum limit (V).  Typical Value = 0.6. Default: 0.0
    :vhmin: High band output minimum limit (V).  Typical Value = -0.6. Default: 0.0
    :vimax: Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 0.0
    :vimin: Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 0.0
    :vlmax: Low band output maximum limit (V).  Typical Value = 0.075. Default: 0.0
    :vlmin: Low band output minimum limit (V).  Typical Value = -0.075. Default: 0.0
    :vstmax: PSS output maximum limit (V).  Typical Value = 0.15. Default: 0.0
    :vstmin: PSS output minimum limit (V).  Typical Value = -0.15. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "bwh1": [Profile.DY.value, ],
        "bwh2": [Profile.DY.value, ],
        "bwl1": [Profile.DY.value, ],
        "bwl2": [Profile.DY.value, ],
        "kh": [Profile.DY.value, ],
        "kh1": [Profile.DY.value, ],
        "kh11": [Profile.DY.value, ],
        "kh17": [Profile.DY.value, ],
        "kh2": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "ki1": [Profile.DY.value, ],
        "ki11": [Profile.DY.value, ],
        "ki17": [Profile.DY.value, ],
        "ki2": [Profile.DY.value, ],
        "kl": [Profile.DY.value, ],
        "kl1": [Profile.DY.value, ],
        "kl11": [Profile.DY.value, ],
        "kl17": [Profile.DY.value, ],
        "kl2": [Profile.DY.value, ],
        "omeganh1": [Profile.DY.value, ],
        "omeganh2": [Profile.DY.value, ],
        "omeganl1": [Profile.DY.value, ],
        "omeganl2": [Profile.DY.value, ],
        "th1": [Profile.DY.value, ],
        "th10": [Profile.DY.value, ],
        "th11": [Profile.DY.value, ],
        "th12": [Profile.DY.value, ],
        "th2": [Profile.DY.value, ],
        "th3": [Profile.DY.value, ],
        "th4": [Profile.DY.value, ],
        "th5": [Profile.DY.value, ],
        "th6": [Profile.DY.value, ],
        "th7": [Profile.DY.value, ],
        "th8": [Profile.DY.value, ],
        "th9": [Profile.DY.value, ],
        "ti1": [Profile.DY.value, ],
        "ti10": [Profile.DY.value, ],
        "ti11": [Profile.DY.value, ],
        "ti12": [Profile.DY.value, ],
        "ti2": [Profile.DY.value, ],
        "ti3": [Profile.DY.value, ],
        "ti4": [Profile.DY.value, ],
        "ti5": [Profile.DY.value, ],
        "ti6": [Profile.DY.value, ],
        "ti7": [Profile.DY.value, ],
        "ti8": [Profile.DY.value, ],
        "ti9": [Profile.DY.value, ],
        "tl1": [Profile.DY.value, ],
        "tl10": [Profile.DY.value, ],
        "tl11": [Profile.DY.value, ],
        "tl12": [Profile.DY.value, ],
        "tl2": [Profile.DY.value, ],
        "tl3": [Profile.DY.value, ],
        "tl4": [Profile.DY.value, ],
        "tl5": [Profile.DY.value, ],
        "tl6": [Profile.DY.value, ],
        "tl7": [Profile.DY.value, ],
        "tl8": [Profile.DY.value, ],
        "tl9": [Profile.DY.value, ],
        "vhmax": [Profile.DY.value, ],
        "vhmin": [Profile.DY.value, ],
        "vimax": [Profile.DY.value, ],
        "vimin": [Profile.DY.value, ],
        "vlmax": [Profile.DY.value, ],
        "vlmin": [Profile.DY.value, ],
        "vstmax": [Profile.DY.value, ],
        "vstmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, bwh1 = 0.0, bwh2 = 0.0, bwl1 = 0.0, bwl2 = 0.0, kh = 0.0, kh1 = 0.0, kh11 = 0.0, kh17 = 0.0, kh2 = 0.0, ki = 0.0, ki1 = 0.0, ki11 = 0.0, ki17 = 0.0, ki2 = 0.0, kl = 0.0, kl1 = 0.0, kl11 = 0.0, kl17 = 0.0, kl2 = 0.0, omeganh1 = 0.0, omeganh2 = 0.0, omeganl1 = 0.0, omeganl2 = 0.0, th1 = 0.0, th10 = 0.0, th11 = 0.0, th12 = 0.0, th2 = 0.0, th3 = 0.0, th4 = 0.0, th5 = 0.0, th6 = 0.0, th7 = 0.0, th8 = 0.0, th9 = 0.0, ti1 = 0.0, ti10 = 0.0, ti11 = 0.0, ti12 = 0.0, ti2 = 0.0, ti3 = 0.0, ti4 = 0.0, ti5 = 0.0, ti6 = 0.0, ti7 = 0.0, ti8 = 0.0, ti9 = 0.0, tl1 = 0.0, tl10 = 0.0, tl11 = 0.0, tl12 = 0.0, tl2 = 0.0, tl3 = 0.0, tl4 = 0.0, tl5 = 0.0, tl6 = 0.0, tl7 = 0.0, tl8 = 0.0, tl9 = 0.0, vhmax = 0.0, vhmin = 0.0, vimax = 0.0, vimin = 0.0, vlmax = 0.0, vlmin = 0.0, vstmax = 0.0, vstmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.bwh1 = bwh1
        self.bwh2 = bwh2
        self.bwl1 = bwl1
        self.bwl2 = bwl2
        self.kh = kh
        self.kh1 = kh1
        self.kh11 = kh11
        self.kh17 = kh17
        self.kh2 = kh2
        self.ki = ki
        self.ki1 = ki1
        self.ki11 = ki11
        self.ki17 = ki17
        self.ki2 = ki2
        self.kl = kl
        self.kl1 = kl1
        self.kl11 = kl11
        self.kl17 = kl17
        self.kl2 = kl2
        self.omeganh1 = omeganh1
        self.omeganh2 = omeganh2
        self.omeganl1 = omeganl1
        self.omeganl2 = omeganl2
        self.th1 = th1
        self.th10 = th10
        self.th11 = th11
        self.th12 = th12
        self.th2 = th2
        self.th3 = th3
        self.th4 = th4
        self.th5 = th5
        self.th6 = th6
        self.th7 = th7
        self.th8 = th8
        self.th9 = th9
        self.ti1 = ti1
        self.ti10 = ti10
        self.ti11 = ti11
        self.ti12 = ti12
        self.ti2 = ti2
        self.ti3 = ti3
        self.ti4 = ti4
        self.ti5 = ti5
        self.ti6 = ti6
        self.ti7 = ti7
        self.ti8 = ti8
        self.ti9 = ti9
        self.tl1 = tl1
        self.tl10 = tl10
        self.tl11 = tl11
        self.tl12 = tl12
        self.tl2 = tl2
        self.tl3 = tl3
        self.tl4 = tl4
        self.tl5 = tl5
        self.tl6 = tl6
        self.tl7 = tl7
        self.tl8 = tl8
        self.tl9 = tl9
        self.vhmax = vhmax
        self.vhmin = vhmin
        self.vimax = vimax
        self.vimin = vimin
        self.vlmax = vlmax
        self.vlmin = vlmin
        self.vstmax = vstmax
        self.vstmin = vstmin

    def __str__(self):
        str = "class=PssIEEE4B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
