import gspread

from oauth2client.service_account import ServiceAccountCredentials


LINK_HEAD = "E:/project/security/"

def get_sheet(id_sheet, name_tab_sheet):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(LINK_HEAD + "config/key-gg-config.json", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(id_sheet)

    return spreadsheet.worksheet(name_tab_sheet)

def handle_get_data(sheet, cols_to_get, status = None):
    all_values = sheet.get_all_values()
    data_rows = all_values[1:]

    result = []
    for idx, row in enumerate(data_rows):
        row_number = idx + 2  # vì idx bắt đầu từ 0, dòng thực là từ 2
        row_data = {"row": row_number}

        empty = True

        for col_idx in cols_to_get:
            if status is not None and status != row[20]:
                continue

            value = row[col_idx] if col_idx < len(row) else ""

            if value.strip() == "":
                empty = False

            row_data[col_idx] = value.strip()

        if not empty:
            result.append(row_data)

    return result

def get_data_from_gg_sheet(id_sheet, name_tab_sheet, list_col, status = None):
  sheet = get_sheet(id_sheet, name_tab_sheet)
  data = handle_get_data(sheet, list_col, status)

  if len(data) == 0:
    print("Data null")
    return None
  
  return data