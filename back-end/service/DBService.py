import os
import json
from typing import List
from dataclasses import asdict

from entity.User import User


LINK_DB = "E:/Document/project/web_support_nf/back-end/db/database.json"

def read_db() -> List[User]:
    if not os.path.exists(LINK_DB):
        return []

    with open(LINK_DB, "r", encoding="utf-8") as f:
        try:
            raw_data = json.load(f)
            return [User(**item) for item in raw_data]
        except json.JSONDecodeError:
            return []
        
def write_db(data: List[User]):
        with open(LINK_DB, "w", encoding="utf-8") as f:
            json.dump([asdict(user) for user in data], f, indent=4, ensure_ascii=False)

def write_append_db(data :User):
    file_data = []

    if os.path.exists(LINK_DB):
        with open(LINK_DB, "r", encoding="utf-8") as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                print("File JSON bị lỗi, sẽ ghi đè lại từ đầu.")

    file_data.append(asdict(data))

    with open(LINK_DB, "w", encoding="utf-8") as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)
        
def remove_data_in_db(case_to_delete):
    users = read_db()

    users = [user for user in users if user.case != case_to_delete]

    write_db(users)