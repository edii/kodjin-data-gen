from util.helper.helper import random_randrange


class Refs:
    def __init__(self,
                 organization_total: int = 0,
                 patient_total: int = 0,
                 practitioner_total: int = 0,
                 encounter_total: int = 0,
                 observation_total: int = 0):
        self._organization_total = organization_total
        self._patient_total = patient_total
        self._practitioner_total = practitioner_total
        self._encounter_total = encounter_total
        self._observation_total = observation_total

    def get_ref_organization(self) -> str:
        rand_id = random_randrange(0, self._organization_total)

        return f"Organization/{rand_id}"

    def is_organization_zero(self) -> bool:
        return self._organization_total == 0

    def get_ref_patient(self) -> str:
        rand_id = random_randrange(0, self._patient_total)

        return f"Patient/{rand_id}"

    def is_patient_zero(self) -> bool:
        return self._patient_total == 0

    def get_ref_practitioner(self) -> str:
        rand_id = random_randrange(0, self._practitioner_total)

        return f"Practitioner/{rand_id}"

    def is_practitioner_zero(self) -> bool:
        return self._practitioner_total == 0

    def get_ref_encounter(self) -> str:
        rand_id = random_randrange(0, self._encounter_total)

        return f"Encounter/{rand_id}"

    def is_encounter_zero(self) -> bool:
        return self._encounter_total == 0

    def get_ref_observation(self) -> str:
        rand_id = random_randrange(0, self._observation_total)

        return f"Observation/{rand_id}"

    def is_observation_zero(self) -> bool:
        return self._observation_total == 0
