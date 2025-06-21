from dataclasses import dataclass
from datetime import datetime


# dataclass đã tự tạo constructor
@dataclass
class User:
    case: int
    date: datetime
    uid: str
    device_id: str
    mail: str
    content: str
    link: list
    id_bill: list
    answer: str
    status: str