import json
from dataclasses import dataclass


@dataclass
class AddUserRequest:
    json: dict


class AddUserController:
    def add(self, request: AddUserRequest) -> None:
        request = sorted(request.json)
        print(json.dumps(request))
