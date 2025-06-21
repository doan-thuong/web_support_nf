import gspread

from google.oauth2 import service_account

from controller import APIController as api
from service import StringService as strService

from entity.User import User


LINK_HEAD = "E:/project/security/"

def get_sheet(id_sheet, name_tab_sheet):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = service_account.Credentials.from_service_account_file(LINK_HEAD + "config/key-gg-config.json", scopes=scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(id_sheet)

    return spreadsheet.worksheet(name_tab_sheet)

def get_all_data(sheet):
    all_values = sheet.get_all_values()
    data_rows = all_values[1:]

    return data_rows

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

def extract_data_rows(sheet, cols_to_get, get_case_min=None, get_case_max=None, status=None):
    data_rows = get_all_data(sheet)
    result = []

    for idx, row in enumerate(data_rows):
        row_number = idx + 2  # vì Google Sheet index bắt đầu từ 1, bỏ header

        # --- Filter theo case ---
        try:
            case = int(row[0])
        except (ValueError, IndexError, TypeError):
            case = None

        if case is not None:
            # Nếu min và max đều có và min > max thì đảo chiều điều kiện
            if get_case_min is not None and get_case_max is not None and get_case_min > get_case_max:
                if case > get_case_min or case < get_case_max:
                    continue
            else:
                if get_case_min is not None and case < get_case_min:
                    continue
                if get_case_max is not None and case > get_case_max:
                    break

        # --- Filter theo status ---
        if status is not None:
            try:
                if row[21] not in status:
                    continue
            except IndexError:
                continue

        # --- Lấy dữ liệu theo cột chỉ định ---
        row_data = {"row": row_number}
        for col_idx in cols_to_get:
            value = row[col_idx] if col_idx < len(row) else ""
            row_data[col_idx] = value.strip()
        
        result.append(row_data)

    return result