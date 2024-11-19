from typing import List
from my_project.auth.service import park_service
from my_project.auth.domain.orders.Park import Park
from my_project.auth.controller.general_controller import GeneralController

class ParkController(GeneralController):
    _service = park_service

    def create_park(self, park: Park) -> None:
        self._service.create(park)

    def update_park(self, park_id: int, park: Park) -> None:
        self._service.update(park_id, park)

    def delete_park(self, park_id: int) -> None:
        self._service.delete(park_id)

    def find_all(self) -> List[Park]:
        return self._service.get_all()

    def find_by_id(self, park_id: int) -> Park:
        return self._service.get_by_id(park_id)

    def find_by_name(self, name: str) -> List[Park]: # тут мало би бути get_by_name
        return self._service.get_by_name(name)

    def find_by_location(self, location: str) -> List[Park]:
        return self._service.get_by_location(location)