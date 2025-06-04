from dataclasses import dataclass


# dataclass đã tự tạo constructor
@dataclass
class User:
    case: int
    uid: str
    device_id: str
    mail: str
    content: str
    link: list
    id_bill: list
    answer: str
    status: str