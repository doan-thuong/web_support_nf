from dataclasses import dataclass


@dataclass
class User:
    case: int
    uid: str
    device_id: str
    content: str
    link: str
    id_bill: str
    answer: str
    status: str