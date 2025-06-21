from service import SheetService as sService


_cache_data_from_sheet = None

def get_data_from_gg_sheet(id_sheet, name_tab_sheet, list_col, get_case_min = None, get_case_max = None, status = None, is_cache = False):
    global _cache_data_from_sheet
    
    if is_cache and _cache_data_from_sheet is not None:
        print("get data cache")
        return _cache_data_from_sheet
    
    sheet = sService.get_sheet(id_sheet, name_tab_sheet)
    data = sService.extract_data_rows(sheet, list_col, get_case_min, get_case_max, status=status)

    if len(data) == 0:
        print("Data null")
        return None

    data_after_handle = []

    for item in data:
        data_after_handle.append(sService.handl_data_fom_sheet(item))

    _cache_data_from_sheet = data_after_handle

    return data_after_handle