from .Equipment import Equipment
from .CGMESProfile import Profile


class GeneratingUnit(Equipment):
    """
    A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.

    :ControlAreaGeneratingUnit: ControlArea specifications for this generating unit. Default: "list"
    :GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: "list"
    :RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: "list"
    :genControlSource: The source of controls for a generating unit. Default: None
    :governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. Default: 0.0
    :initialP: Default initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration. Default: 0.0
    :longPF: Generating unit long term economic participation factor. Default: 0.0
    :maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit. Default: 0.0
    :maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. Default: 0.0
    :minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. Default: 0.0
    :nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive value equal or less than RotatingMachine.ratedS. Default: 0.0
    :normalPF: Generating unit economic participation factor. Default: 0.0
    :ratedGrossMaxP: The unit`s gross rated maximum capacity (book value). Default: 0.0
    :ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid. Default: 0.0
    :ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity. Default: 0.0
    :shortPF: Generating unit short term economic participation factor. Default: 0.0
    :startupCost: The initial startup cost incurred for each start of the GeneratingUnit. Default: 0.0
    :totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy. Default: 0.0
    :variableCost: The variable cost component of production per unit of ActivePower. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "ControlAreaGeneratingUnit": [Profile.EQ.value, ],
        "GrossToNetActivePowerCurves": [Profile.EQ.value, ],
        "RotatingMachine": [Profile.EQ.value, ],
        "genControlSource": [Profile.EQ.value, ],
        "governorSCD": [Profile.EQ.value, ],
        "initialP": [Profile.EQ.value, ],
        "longPF": [Profile.EQ.value, ],
        "maxOperatingP": [Profile.EQ.value, ],
        "maximumAllowableSpinningReserve": [Profile.EQ.value, ],
        "minOperatingP": [Profile.EQ.value, ],
        "nominalP": [Profile.EQ.value, ],
        "normalPF": [Profile.SSH.value, ],
        "ratedGrossMaxP": [Profile.EQ.value, ],
        "ratedGrossMinP": [Profile.EQ.value, ],
        "ratedNetMaxP": [Profile.EQ.value, ],
        "shortPF": [Profile.EQ.value, ],
        "startupCost": [Profile.EQ.value, ],
        "totalEfficiency": [Profile.EQ.value, ],
        "variableCost": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Equipment:\n" + Equipment.__doc__

    def __init__(self, ControlAreaGeneratingUnit = "list", GrossToNetActivePowerCurves = "list", RotatingMachine = "list", genControlSource = None, governorSCD = 0.0, initialP = 0.0, longPF = 0.0, maxOperatingP = 0.0, maximumAllowableSpinningReserve = 0.0, minOperatingP = 0.0, nominalP = 0.0, normalPF = 0.0, ratedGrossMaxP = 0.0, ratedGrossMinP = 0.0, ratedNetMaxP = 0.0, shortPF = 0.0, startupCost = 0.0, totalEfficiency = 0.0, variableCost = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit
        self.GrossToNetActivePowerCurves = GrossToNetActivePowerCurves
        self.RotatingMachine = RotatingMachine
        self.genControlSource = genControlSource
        self.governorSCD = governorSCD
        self.initialP = initialP
        self.longPF = longPF
        self.maxOperatingP = maxOperatingP
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve
        self.minOperatingP = minOperatingP
        self.nominalP = nominalP
        self.normalPF = normalPF
        self.ratedGrossMaxP = ratedGrossMaxP
        self.ratedGrossMinP = ratedGrossMinP
        self.ratedNetMaxP = ratedNetMaxP
        self.shortPF = shortPF
        self.startupCost = startupCost
        self.totalEfficiency = totalEfficiency
        self.variableCost = variableCost

    def __str__(self):
        str = "class=GeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
