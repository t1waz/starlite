from starlite import DTOFactory
from tests import Person

PersonDTO = DTOFactory()("PersonDTO", Person)


def dto_test_handler(data: PersonDTO) -> PersonDTO:
    return data
