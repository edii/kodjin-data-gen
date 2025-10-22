import logging
import json
from uuid import uuid4
from jinja2 import Environment
from faker import Faker
from util.consts import Status
from datetime import datetime
from typing import List, Dict, Optional
from util.resources.Practitioner import Practitioner
from util.resources.Patient import Patient
from util.resources.Organization import Organization
from util.resources.Encounter import Encounter
from util.resources.Observation import Observation
from util.helper.helper import random_list


class Composition:
    TEMPLATE_NAME = "composition.json.jinja"

    practitioner: Practitioner = None

    def __init__(self, output_dir: str = "", log: logging.Logger = logging.getLogger("composition"),
                 jinja: Environment = Environment,
                 faker: Faker = Faker):
        self._log = log
        self._jinja = jinja
        self._faker = faker
        self._output_dir = output_dir
        self._params: List[Dict] = []

        # refs
        self._organization: Optional[Organization] = None
        self._patient: Optional[Patient] = None
        self._practitioner: Optional[Practitioner] = None
        self._encounter: Optional[Encounter] = None
        self._observation: Optional[Observation] = None

    def set_organization(self, organization: Optional[Organization]):
        self._organization = organization

    def set_patient(self, patient: Optional[Patient]):
        self._patient = patient

    def set_practitioner(self, practitioner: Optional[Practitioner]):
        self._practitioner = practitioner

    def set_encounter(self, encounter: Optional[Encounter]):
        self._encounter = encounter

    def set_observation(self, observation: Optional[Observation]):
        self._observation = observation

    def get_output_dir(self) -> str:
        return f"{self._output_dir}/{type(self).__name__}.ndjson"

    def validate(self):
        if (self._organization is None or
                (self._organization is not None and len(self._organization.get_params()) == 0)):
            raise Exception("Required ref for organization")

        if (self._patient is None or
                (self._patient is not None and len(self._patient.get_params()) == 0)):
            raise Exception("Required ref for patient")

        if (self._practitioner is None or
                (self._practitioner is not None and len(self._practitioner.get_params()) == 0)):
            raise Exception("Required ref for practitioner")

        if (self._encounter is None or
                (self._encounter is not None and len(self._encounter.get_params()) == 0)):
            raise Exception("Required ref for encounter")

        if (self._observation is None or
                (self._observation is not None and len(self._observation.get_params()) == 0)):
            raise Exception("Required ref for observation")

    def process(self, total: int = 0):
        self.validate()

        self._log.info(f"Prepare composition")

        for i in range(0, total):
            organization_param = random_list(self._organization.get_params())
            patient_param = random_list(self._patient.get_params())
            practitioner_param = random_list(self._practitioner.get_params())
            encounter_param = random_list(self._encounter.get_params())
            observation_param = random_list(self._observation.get_params())

            param = {
                "id": str(uuid4()),
                "status_text": Status.GENERATED,
                "status": Status.FINAL,
                "last_updated": datetime.now(),
                "ref_organization": f"Organization/{organization_param['id']}",
                "ref_patient": f"Patient/{patient_param['id']}",
                "ref_practitioner": f"Practitioner/{practitioner_param['id']}",
                "ref_encounter": f"Encounter/{encounter_param['id']}",
                "ref_observation": f"Encounter/{observation_param['id']}",
            }

            self._params.append(param)

    def get_params(self) -> List[Dict]:
        return self._params

    def create(self):
        self._log.info(f"Generating %s composition", len(self.get_params()))

        with open(self.get_output_dir(), "w") as output:
            for param in self.get_params():
                template = self._jinja.get_template(self.TEMPLATE_NAME)
                composition_data = template.render(param)

                output.write(json.dumps(json.loads(composition_data)))
                output.write("\n")
