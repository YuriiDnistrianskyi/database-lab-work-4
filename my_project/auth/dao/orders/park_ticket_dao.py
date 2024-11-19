from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.park_show import ParkShow
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.park_ticket import ParkTicket


class ParkTicketDAO(GeneralDAO):
    _domain_type = ParkTicket

    def get_by_two_id(self, park_id: int, ticket_id: int) -> _domain_type:
        return self._session.query(self._domain_type).filter(
            self._domain_type.park_id == park_id,
            self._domain_type.ticket_id == ticket_id
        ).one()


    def uptade_by_two_id(self, park_id: int, ticket_id: int, in_obj: object) -> None:
        domain_obj = self._session.query(self._domain_type).filter(
            self._domain_type.park_id == park_id,
            self._domain_type.ticket_id == ticket_id
        ).one()
        mapper: Mapper = inspect(type(in_obj))  # Metadata
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()


    def delete_by_two_id(self, park_id: int, ticket_id: int) -> None:
        domain_obj = self._session.query(self._domain_type).filter(self._domain_type.park_id == park_id).filter(
            self._domain_type.ticket_id == ticket_id).one()
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
