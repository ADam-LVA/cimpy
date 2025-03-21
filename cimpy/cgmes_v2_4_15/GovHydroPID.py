from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroPID(TurbineGovernorDynamics):
    """
    PID governor and turbine.

    :aturb: Turbine numerator multiplier (Aturb) (note 3).  Typical Value -1. Default: 0.0
    :bturb: Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5. Default: 0.0
    :db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0
    :eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
    :gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
    :gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
    :inputSignal: Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true. Default: False
    :kd: Derivative gain (Kd).  Typical Value = 1.11. Default: 0.0
    :kg: Gate servo gain (Kg).  Typical Value = 2.5. Default: 0.0
    :ki: Integral gain (Ki).  Typical Value = 0.36. Default: 0.0
    :kp: Proportional gain (Kp).  Typical Value = 0.1. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
    :pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
    :pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0
    :pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0
    :r: Steady state droop (R).  Typical Value = 0.05. Default: 0.0
    :td: Input filter time constant (Td).  Typical Value = 0. Default: 0.0
    :tf: Washout time constant (Tf).  Typical Value = 0.1. Default: 0.0
    :tp: Gate servo time constant (Tp).  Typical Value = 0.35. Default: 0.0
    :tt: Power feedback time constant (Tt).  Typical Value = 0.02. Default: 0.0
    :tturb: Turbine time constant (Tturb) (note 3).  Typical Value = 0.8. Default: 0.0
    :velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14. Default: 0.0
    :velop: Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "aturb": [Profile.DY.value, ],
        "bturb": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "eps": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "gv6": [Profile.DY.value, ],
        "inputSignal": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pgv1": [Profile.DY.value, ],
        "pgv2": [Profile.DY.value, ],
        "pgv3": [Profile.DY.value, ],
        "pgv4": [Profile.DY.value, ],
        "pgv5": [Profile.DY.value, ],
        "pgv6": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tt": [Profile.DY.value, ],
        "tturb": [Profile.DY.value, ],
        "velcl": [Profile.DY.value, ],
        "velop": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, aturb = 0.0, bturb = 0.0, db1 = 0.0, db2 = 0.0, eps = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, gv6 = 0.0, inputSignal = False, kd = 0.0, kg = 0.0, ki = 0.0, kp = 0.0, mwbase = 0.0, pgv1 = 0.0, pgv2 = 0.0, pgv3 = 0.0, pgv4 = 0.0, pgv5 = 0.0, pgv6 = 0.0, pmax = 0.0, pmin = 0.0, r = 0.0, td = 0.0, tf = 0.0, tp = 0.0, tt = 0.0, tturb = 0.0, velcl = 0.0, velop = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.aturb = aturb
        self.bturb = bturb
        self.db1 = db1
        self.db2 = db2
        self.eps = eps
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.gv6 = gv6
        self.inputSignal = inputSignal
        self.kd = kd
        self.kg = kg
        self.ki = ki
        self.kp = kp
        self.mwbase = mwbase
        self.pgv1 = pgv1
        self.pgv2 = pgv2
        self.pgv3 = pgv3
        self.pgv4 = pgv4
        self.pgv5 = pgv5
        self.pgv6 = pgv6
        self.pmax = pmax
        self.pmin = pmin
        self.r = r
        self.td = td
        self.tf = tf
        self.tp = tp
        self.tt = tt
        self.tturb = tturb
        self.velcl = velcl
        self.velop = velop

    def __str__(self):
        str = "class=GovHydroPID\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
