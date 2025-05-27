def has_dash(str_check):
    return "-" in str_check

def has_no_uppercase(str_check):
    return not any(text.isupper() for text in str_check)

def has_no_lowercase(str_check):
    return not any(text.islower() for text in str_check)

def handle_to_get_device_id_android(str_old):
    if not str_old: return None

    list_str = str_old.split(" ")
    for str in list_str:
        if not str.strip(): continue

        if not has_dash(str) and has_no_uppercase(str):

            return str

    return None
    
def handle_to_get_device_id_ios(str_old):
    if not str_old: return None

    list_str = str_old.split(" ")
    for str in list_str:
        if not str.strip(): continue

        if has_dash(str) and has_no_lowercase(str):

            return str

    return None

def handle_to_get_uid(str_old):
    if not str_old: return None

    list_str = str_old.split(" ")
    for str in list_str:
        if not str.strip(): continue

        if not has_dash(str) and not has_no_lowercase(str) and not has_no_uppercase(str):

            return str

    return None