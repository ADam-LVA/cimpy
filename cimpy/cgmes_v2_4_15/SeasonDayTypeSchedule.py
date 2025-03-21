from .RegularIntervalSchedule import RegularIntervalSchedule
from .CGMESProfile import Profile


class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """
    A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

    :DayType: Schedules that use this DayType. Default: None
    :Season: Schedules that use this Season. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "DayType": [Profile.EQ.value, ],
        "Season": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class RegularIntervalSchedule:\n" + RegularIntervalSchedule.__doc__

    def __init__(self, DayType = None, Season = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DayType = DayType
        self.Season = Season

    def __str__(self):
        str = "class=SeasonDayTypeSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
