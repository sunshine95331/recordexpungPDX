from dataclasses import dataclass

from expungeservice.models.charge import Charge
from expungeservice.models.expungement_result import TypeEligibility, EligibilityStatus


@dataclass(frozen=True)
class CivilOffense(Charge):
    type_name: str = "Civil Offense"
    expungement_rules: str = (
        """Expungement, generally speaking, only applies to criminal offenses. Civil offenses and administrative procedures – even those subject to punishments including jail time – are not eligible for expungement. The distinction between criminal and civil charges is far from clear. See, e.g. Brown v. Multnomah County Dist. Court, 570 P. 2d 52 - Or: Supreme Court 1977 ('There is no easy test for when the imposition of a sanction is a "criminal prosecution" within the meaning of the constitutional guarantees.') However, at least the following are not eligible under the expungement statute:
 * Contempt of Court
 * Extradition/Fugitive Complaint
 * Parking tickets
 These charges are ineligible even if they are marked as Violations or some other level that would normally qualify them as eligible.
"""
    )
    blocks_other_charges: bool = False

    def _type_eligibility(self):
        return TypeEligibility(EligibilityStatus.INELIGIBLE, reason="Ineligible by omission from statute")
