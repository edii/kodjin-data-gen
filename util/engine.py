import logging
from jinja2 import Environment
from faker import Faker
from typing import Dict
from util.resources.Organization import Organization
from util.resources.Practitioner import Practitioner
from util.resources.Patient import Patient
from util.resources.Encounter import Encounter
from util.resources.Condition import Condition
from util.resources.Observation import Observation
from util.resources.Composition import Composition


class Engine:

    def __init__(self, cfg: Dict,
                 names: Dict,
                 ages: Dict,
                 terminology: Dict,
                 output_dir: str = "",
                 log: logging.Logger = logging.getLogger("engine"),
                 jinja: Environment = Environment,
                 faker: Faker = Faker):
        self._cfg = cfg
        # self._names = names
        self._log = log
        self._organization = Organization(output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._practitioner = Practitioner(
            names=names, ages=ages, terminology=terminology, output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._patient = Patient(
            names=names, ages=ages, terminology=terminology,output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._encounter = Encounter(output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._condition = Condition(output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._observation = Observation(output_dir=output_dir, log=log, jinja=jinja, faker=faker)
        self._composition = Composition(output_dir=output_dir, log=log, jinja=jinja, faker=faker)

    def run(self):
        # processing all resources
        self._organization.process(self._cfg["organization_total"])
        self._practitioner.process(self._cfg["practitioner_total"])
        self._patient.process(self._cfg["patient_total"])

        self._encounter.set_organization(self._organization)
        self._encounter.set_patient(self._patient)
        self._encounter.set_practitioner(self._practitioner)
        self._encounter.process(self._cfg["encounter_total"])

        self._condition.set_organization(self._organization)
        self._condition.set_patient(self._patient)
        self._condition.set_practitioner(self._practitioner)
        self._condition.set_encounter(self._encounter)
        self._condition.process(self._cfg["condition_total"])

        self._observation.set_organization(self._organization)
        self._observation.set_patient(self._patient)
        self._observation.set_practitioner(self._practitioner)
        self._observation.set_encounter(self._encounter)
        self._observation.process(self._cfg["observation_total"])

        self._composition.set_organization(self._organization)
        self._composition.set_patient(self._patient)
        self._composition.set_practitioner(self._practitioner)
        self._composition.set_encounter(self._encounter)
        self._composition.set_observation(self._observation)
        self._composition.process(self._cfg["composition_total"])

        # create resources
        # Organization
        self._organization.create()

        # Practitioner
        self._practitioner.create()

        # Patient
        self._patient.create()

        # Encounter
        self._encounter.create()

        # Condition
        self._condition.create()

        # Observation
        self._observation.create()

        # Composition
        self._composition.create()
