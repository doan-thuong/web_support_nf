import gspread

from google.oauth2 import service_account

from controller import APIController as api
from service import StringService as strService
from service import GeneralService as gService

from entity.User import User


LINK_HEAD = "E:/project/security/"

def get_sheet(id_sheet, name_tab_sheet) -> gspread.worksheet.Worksheet:
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
        "date": [1],
        "get_id": [16],
        "content": [10, 12, 14],
        "link": [11, 13, 15],
        "mail": [17],
        "answer": [19],
        "status": [21]
    }

    case = list_data_from_row[data_dict["case"][0]]

    date = strService.convert_datetime_from_str(list_data_from_row[data_dict["date"][0]])

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

    return User(case, date, uid, device_id, mail, content, link, id_bill, answer, status)

def extract_data_rows(data_rows,
                    cols_to_get,
                    get_date_min=None,
                    get_date_max=None,
                    get_case_min=None,
                    get_case_max=None,
                    page=None,
                    status=None):
    
    result = []

    # --- Filter theo PAGE
    size_in_page = 100
    
    if page:
        try:
            page_number = int(page) - 1
        except (TypeError, ValueError):
            page_number = None

        min_case_in_page = page_number*size_in_page
        max_case_in_page = min_case_in_page + size_in_page - 1
        print(f"{min_case_in_page} and {max_case_in_page}")

    count = 0

    for idx, row in enumerate(data_rows):
        row_number = idx + 2
        if count >= size_in_page: break

        # --- Filter theo CASE ---
        try:
            case = int(row[0])
        except (ValueError, IndexError, TypeError):
            case = None
        if get_case_min or get_case_max:
            if not gService.is_value_in_range(case, get_case_min, get_case_max, auto_swap=True):
                continue

        # --- Filter theo PAGE
        if page and case:
            if case > max_case_in_page: break
            if not gService.is_value_in_range(case, min_case_in_page, max_case_in_page): continue

        # --- Filter theo DATE ---
        if get_date_min or get_date_max:
            try:
                date_str = row[1]
                date_obj = strService.convert_datetime_from_str(date_str)
            except (IndexError, ValueError, TypeError):
                continue

            if not gService.is_value_in_range(date_obj, get_date_min, get_date_max, auto_swap=True):
                continue

        # --- Filter theo STATUS ---
        if status is not None:
            try:
                if row[21] not in status:
                    continue
            except IndexError:
                continue

        row_data = {"row": row_number}
        for col_idx in cols_to_get:
            value = row[col_idx] if col_idx < len(row) else ""
            row_data[col_idx] = value.strip()

        result.append(row_data)
        count += 1

    return result

def edit_cell(sheet:gspread.worksheet.Worksheet, cell , data, is_append:bool = False):
    if is_append:
        current_value = sheet.acell(cell). value or ""
        new_value = f"{current_value}\n{data}"
    else:
        new_value = data

    sheet.update(cell, new_value)