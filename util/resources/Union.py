import json
import logging
from typing import List, Optional, Dict


class Union:
    def __init__(self, name: str, resources: Optional[List] = None,
                 output_dir: str = "",
                 log: logging.Logger = logging.getLogger("encounter")):
        self._name = name
        self._resources = resources
        self._log = log
        self._total = 0
        self._output_dir = output_dir

    def get_output_dir(self) -> str:
        return f"{self._output_dir}/{self._name}.ndjson"

    def get_resource_name(self, obj) -> str:
        return f"{type(obj).__name__}"

    def process(self, total: int = 0):
        self._log.info(f"Prepare {self._name}")

        if self._resources is None:
            raise Exception("resources not be empty")

        self._total = total
        for resource in self._resources:
            resource.process(total)

    def render_data(self, resource, params: List[Dict], current_index: int) -> Dict:
        for i, param in enumerate(params):
            if i == current_index:
                new_param = param | resource.union_refs(union_id=str(i+1))

                return json.loads(resource.render_data(new_param))

        return {}

    def create(self):
        self._log.info(f"Generating %s {self._name}", self._total)

        with open(self.get_output_dir(), "w") as output:
            for i in range(0, self._total):
                union_dict: List[Dict] = []

                for resource in self._resources:
                    union_dict.append(self.render_data(resource=resource, params=resource.get_params(), current_index=i))

                output.write(json.dumps(union_dict))
                output.write("\n")
