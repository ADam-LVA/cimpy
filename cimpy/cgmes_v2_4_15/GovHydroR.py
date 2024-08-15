from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroR(TurbineGovernorDynamics):
    """
    Fourth order lead-lag governor and hydro turbine.

    :at: Turbine gain (At).  Typical Value = 1.2. Default: 0.0
    :db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0
    :dturb: Turbine damping factor (Dturb).  Typical Value = 0.2. Default: 0.0
    :eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :gmax: Maximum governor output (Gmax).  Typical Value = 1.05. Default: 0.0
    :gmin: Minimum governor output (Gmin).  Typical Value = -0.05. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
    :gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
    :gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
    :h0: Turbine nominal head (H0).  Typical Value = 1. Default: 0.0
    :inputSignal: Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true. Default: False
    :kg: Gate servo gain (Kg).  Typical Value = 2. Default: 0.0
    :ki: Integral gain (Ki).  Typical Value = 0.5. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
    :pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
    :pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0
    :pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0
    :qnl: No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08. Default: 0.0
    :r: Steady-state droop (R).  Typical Value = 0.05. Default: 0.0
    :t1: Lead time constant 1 (T1).  Typical Value = 1.5. Default: 0.0
    :t2: Lag time constant 1 (T2).  Typical Value = 0.1. Default: 0.0
    :t3: Lead time constant 2 (T3).  Typical Value = 1.5. Default: 0.0
    :t4: Lag time constant 2 (T4).  Typical Value = 0.1. Default: 0.0
    :t5: Lead time constant 3 (T5).  Typical Value = 0. Default: 0.0
    :t6: Lag time constant 3 (T6).  Typical Value = 0.05. Default: 0.0
    :t7: Lead time constant 4 (T7).  Typical Value = 0. Default: 0.0
    :t8: Lag time constant 4 (T8).  Typical Value = 0.05. Default: 0.0
    :td: Input filter time constant (Td).  Typical Value = 0.05. Default: 0.0
    :tp: Gate servo time constant (Tp).  Typical Value = 0.05. Default: 0.0
    :tt: Power feedback time constant (Tt).  Typical Value = 0. Default: 0.0
    :tw: Water inertia time constant (Tw).  Typical Value = 1. Default: 0.0
    :velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2. Default: 0.0
    :velop: Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "at": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "dturb": [Profile.DY.value, ],
        "eps": [Profile.DY.value, ],
        "gmax": [Profile.DY.value, ],
        "gmin": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "gv6": [Profile.DY.value, ],
        "h0": [Profile.DY.value, ],
        "inputSignal": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pgv1": [Profile.DY.value, ],
        "pgv2": [Profile.DY.value, ],
        "pgv3": [Profile.DY.value, ],
        "pgv4": [Profile.DY.value, ],
        "pgv5": [Profile.DY.value, ],
        "pgv6": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "qnl": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "t7": [Profile.DY.value, ],
        "t8": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tt": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
        "velcl": [Profile.DY.value, ],
        "velop": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, at = 0.0, db1 = 0.0, db2 = 0.0, dturb = 0.0, eps = 0.0, gmax = 0.0, gmin = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, gv6 = 0.0, h0 = 0.0, inputSignal = False, kg = 0.0, ki = 0.0, mwbase = 0.0, pgv1 = 0.0, pgv2 = 0.0, pgv3 = 0.0, pgv4 = 0.0, pgv5 = 0.0, pgv6 = 0.0, pmax = 0.0, pmin = 0.0, qnl = 0.0, r = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, td = 0.0, tp = 0.0, tt = 0.0, tw = 0.0, velcl = 0.0, velop = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.at = at
        self.db1 = db1
        self.db2 = db2
        self.dturb = dturb
        self.eps = eps
        self.gmax = gmax
        self.gmin = gmin
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.gv6 = gv6
        self.h0 = h0
        self.inputSignal = inputSignal
        self.kg = kg
        self.ki = ki
        self.mwbase = mwbase
        self.pgv1 = pgv1
        self.pgv2 = pgv2
        self.pgv3 = pgv3
        self.pgv4 = pgv4
        self.pgv5 = pgv5
        self.pgv6 = pgv6
        self.pmax = pmax
        self.pmin = pmin
        self.qnl = qnl
        self.r = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.td = td
        self.tp = tp
        self.tt = tt
        self.tw = tw
        self.velcl = velcl
        self.velop = velop

    def __str__(self):
        str = "class=GovHydroR\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
