from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovGAST1(TurbineGovernorDynamics):
    """
    Modified single shaft gas turbine.

    :a: Turbine power time constant numerator scale factor (a).  Typical Value = 0.8. Default: 0.0
    :b: Turbine power time constant denominator scale factor (b).  Typical Value = 1. Default: 0.0
    :db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0
    :eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :fidle: Fuel flow at zero power output (Fidle).  Typical Value = 0.18. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
    :gv2: Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
    :gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
    :ka: Governor gain (Ka).  Typical Value = 0. Default: 0.0
    :kt: Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0
    :lmax: Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust gas temperature.  Typical Value = 1. Default: 0.0
    :loadinc: Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05. Default: 0.0
    :ltrate: Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
    :pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
    :r: Permanent droop (R).  Typical Value = 0.04. Default: 0.0
    :rmax: Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1. Default: 0.0
    :t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0.0
    :t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0.0
    :t3: Turbine exhaust temperature time constant (T3).  T3 represents delay in the exhaust temperature and load limiting system. Typical Value = 3. Default: 0.0
    :t4: Governor lead time constant (T4).  Typical Value = 0. Default: 0.0
    :t5: Governor lag time constant (T5).  Typical Value = 0. Default: 0.0
    :tltr: Valve position averaging time constant (Tltr).  Typical Value = 10. Default: 0.0
    :vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0
    :vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a": [Profile.DY.value, ],
        "b": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "eps": [Profile.DY.value, ],
        "fidle": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "gv6": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kt": [Profile.DY.value, ],
        "lmax": [Profile.DY.value, ],
        "loadinc": [Profile.DY.value, ],
        "ltrate": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pgv1": [Profile.DY.value, ],
        "pgv2": [Profile.DY.value, ],
        "pgv3": [Profile.DY.value, ],
        "pgv4": [Profile.DY.value, ],
        "pgv5": [Profile.DY.value, ],
        "pgv6": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "rmax": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "tltr": [Profile.DY.value, ],
        "vmax": [Profile.DY.value, ],
        "vmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, a = 0.0, b = 0.0, db1 = 0.0, db2 = 0.0, eps = 0.0, fidle = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, gv6 = 0.0, ka = 0.0, kt = 0.0, lmax = 0.0, loadinc = 0.0, ltrate = 0.0, mwbase = 0.0, pgv1 = 0.0, pgv2 = 0.0, pgv3 = 0.0, pgv4 = 0.0, pgv5 = 0.0, pgv6 = 0.0, r = 0.0, rmax = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, tltr = 0.0, vmax = 0.0, vmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a = a
        self.b = b
        self.db1 = db1
        self.db2 = db2
        self.eps = eps
        self.fidle = fidle
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.gv6 = gv6
        self.ka = ka
        self.kt = kt
        self.lmax = lmax
        self.loadinc = loadinc
        self.ltrate = ltrate
        self.mwbase = mwbase
        self.pgv1 = pgv1
        self.pgv2 = pgv2
        self.pgv3 = pgv3
        self.pgv4 = pgv4
        self.pgv5 = pgv5
        self.pgv6 = pgv6
        self.r = r
        self.rmax = rmax
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.tltr = tltr
        self.vmax = vmax
        self.vmin = vmin

    def __str__(self):
        str = "class=GovGAST1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
