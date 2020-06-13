from dataclasses import dataclass
from enum import Enum
from expungeservice.util import DateWithFuture as date


class DispositionStatus(str, Enum):
    CONVICTED = "Convicted"
    DISMISSED = "Dismissed"
    NO_COMPLAINT = "No Complaint"
    DIVERTED = "Diverted"
    UNKNOWN = "Unknown"
    UNRECOGNIZED = "Unrecognized"

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


@dataclass(frozen=True)
class Disposition:
    date: date
    ruling: str
    status: DispositionStatus
    amended: bool = False


class DispositionCreator:
    @staticmethod
    def empty():
        return Disposition(date.today(), "missing", DispositionStatus.UNKNOWN)

    @staticmethod
    def create(date: date, ruling: str, amended: bool = False) -> Disposition:
        status = DispositionCreator.__build_status(ruling)
        return Disposition(date, ruling, status, amended)

    @staticmethod
    def __build_status(ruling_string):
        ruling = ruling_string.lower()
        conviction_rulings = [
            "convicted",
            "conviction",
            "reduced",
            "finding - guilty",
            "finding - contempt",
            "conversion",
            "converted",
            "bail forfeiture",
            "extradited",
            "forfeiture allowed",
            "found in contempt",
        ]
        dismissal_rulings = [
            "acquitted",
            "acquittal",
            "dismissed",
            "discharged",
            "dismissal",
            "finding - not guilty",
            "accusatory instrument filed",
            "removed from charging instrument",
            "plea lesser charge",
        ]
        missing_rulings = ["missing", "conditional discharge", "deferred"]
        if any([rule in ruling for rule in conviction_rulings]):
            return DispositionStatus.CONVICTED
        elif any([rule in ruling for rule in dismissal_rulings]):
            return DispositionStatus.DISMISSED
        elif "diverted" in ruling:
            return DispositionStatus.DIVERTED
        elif "no complaint" in ruling:
            return DispositionStatus.NO_COMPLAINT
        elif any([rule == ruling for rule in missing_rulings]):
            return DispositionStatus.UNKNOWN
        else:
            return DispositionStatus.UNRECOGNIZED
