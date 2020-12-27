import json
from itertools import product
from typing import Iterable, Dict, Optional, List, Any

ex = {
    "атмосфера": ["кислородосодержащая", "отсутствует"],
    "размер": ["карлик", "великан"],
    "температура": ["низкая", "средняя", "выскоая"],
    "посещалась ранее": ["да", "нет"]
}


class TooMuchParametersException(Exception):
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


def calculate(js):
    answer = [dict(zip(js.keys(), item)) for item in product(*js.values())]
    count = len(answer)
    print(count)
    if count > 100:
        raise TooMuchParametersException("Tdasads")
    return answer


print(calculate(ex))
