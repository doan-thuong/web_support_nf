import gspread

from google.oauth2 import service_account

from controller import APIController as api
from service import StringService as strService

from entity.User import User


LINK_HEAD = "E:/project/security/"

_cache_data_from_sheet = None

def get_sheet(id_sheet, name_tab_sheet):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = service_account.Credentials.from_service_account_file(LINK_HEAD + "config/key-gg-config.json", scopes=scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(id_sheet)

    return spreadsheet.worksheet(name_tab_sheet)

def handl_data_fom_sheet(list_data_from_row):
    # col 1 - case
    # col 11, 13, 15 - user's content
    # col 12, 14, 16 - link
    # col 17 - device id and uid
    # col 18 - user's mail
    # col 19 - answer's QA
    # col 21 - status of case from CS
    # col 26 - status of case from QA

    data_dict = {
        "case": [0],
        "get_id": [16],
        "content": [10, 12, 14],
        "link": [11, 13, 15],
        "mail": [17],
        "answer": [19],
        "status": [21]
    }

    case = list_data_from_row[data_dict["case"][0]]

    get_id = list_data_from_row[data_dict["get_id"][0]]
    uid = strService.handle_to_get_uid(get_id)
    device_id = strService.handle_to_get_device_id(get_id)

    content = "\n".join(str(list_data_from_row[i]) for i in data_dict["content"] if list_data_from_row[i])
    
    link_before_clean = "\n".join(str(list_data_from_row[i]).strip() for i in data_dict["link"] if list_data_from_row[i])
    link = strService.clean_link(link_before_clean)

    id_bill =  api.api_get_id_bill(link)

    mail = list_data_from_row[data_dict["mail"][0]]
    answer = list_data_from_row[data_dict["answer"][0]]
    status = list_data_from_row[data_dict ["status"][0]]

    return User(case, uid, device_id, mail, content, link, id_bill, answer, status)

def handle_get_data(sheet, cols_to_get, status = None):
    all_values = sheet.get_all_values()
    data_rows = all_values[1:]

    result = []
    for idx, row in enumerate(data_rows):
        row_number = idx + 2  # vì idx bắt đầu từ 0, dòng thực là từ 2
        row_data = {"row": row_number}

        if status is not None and row[21] not in status:
            continue

        for col_idx in cols_to_get:

            value = row[col_idx] if col_idx < len(row) else ""

            row_data[col_idx] = value.strip()

        result.append(row_data)

    return result

def get_data_from_gg_sheet(id_sheet, name_tab_sheet, list_col, status = None, is_cache = False):
    global _cache_data_from_sheet
    
    if is_cache and _cache_data_from_sheet is not None:
        print("get data cache")
        return _cache_data_from_sheet
    
    sheet = get_sheet(id_sheet, name_tab_sheet)
    data = handle_get_data(sheet, list_col, status)

    if len(data) == 0:
        print("Data null")
        return None

    data_after_handle = []

    for item in data:
        data_after_handle.append(handl_data_fom_sheet(item))

    _cache_data_from_sheet = data_after_handle

    return data_after_handle