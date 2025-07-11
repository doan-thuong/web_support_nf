from service import SheetService as sService


_cache_data_from_sheet = None
_data_not_refresh = None

def get_all_data(sheet):
    all_values = sheet.get_all_values()

    # --- trừ dòng đầu tiên
    data_rows = all_values[1:]

    return data_rows

# --- lấy dòng cụ thể. bắt đầu từ 1, không phải là 0 ---
def get_specific_row(sheet, row_need_to_get):
    data = sheet.row_values(row_need_to_get)

    return data

def pagination_data(id_sheet, name_tab_sheet, list_col, page=None):
    global _data_not_refresh
    
    sheet = sService.get_sheet(id_sheet, name_tab_sheet)
    data_rows = get_all_data(sheet)
    _data_not_refresh = data_rows

    data = sService.extract_data_rows(data_rows, list_col, page=page)

    data_after_handle = []

    for item in data:
        data_after_handle.append(sService.handl_data_fom_sheet(item))

    return {
        "data": data_after_handle,
        "length": len(data_rows)
    }

def get_data_from_gg_sheet(id_sheet, name_tab_sheet, list_col,get_date_min = None, get_date_max = None, get_case_min = None, get_case_max = None, status = None, is_cache = False, is_refresh = False):
    global _cache_data_from_sheet
    global _data_not_refresh

    sheet = sService.get_sheet(id_sheet, name_tab_sheet)

    if not is_refresh and _data_not_refresh is not None:
        print("get data not refresh")
        data_rows = _data_not_refresh
    else:
        print("get data refresh")
        data_rows = get_all_data(sheet)
        _data_not_refresh = data_rows
    
    if is_cache and _cache_data_from_sheet is not None:
        print("get data cache")
        return _cache_data_from_sheet
    
    data = sService.extract_data_rows(
        data_rows=data_rows, 
        cols_to_get=list_col, 
        get_date_min=get_date_min, 
        get_date_max=get_date_max, 
        get_case_min=get_case_min, 
        get_case_max=get_case_max, 
        status=status)

    if len(data) == 0:
        print("Data null")
        return None

    data_after_handle = []

    for item in data:
        data_after_handle.append(sService.handl_data_fom_sheet(item))

    _cache_data_from_sheet = data_after_handle

    return data_after_handle