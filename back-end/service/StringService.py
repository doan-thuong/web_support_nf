from urllib.parse import urlparse, parse_qs
import re
from dateutil import parser


LIST_TEXT_SKIP = ['Device', 'device',
                'deviceid', 'deviceId',
                'DeviceId', 'DeviceID',
                'Id', 'ID',
                'Uid', 'UID',
                "uID", 'uid',
                'UId']

SPECIAL_CHAR = "@()."

def has_dash(str_check):
    return "-" in str_check

def has_no_uppercase(str_check):
    return not any(text.isupper() for text in str_check)

def has_no_lowercase(str_check):
    return not any(text.islower() for text in str_check)

def handle_to_get_device_id(str_old: str):
    if not str_old: return None

    result = []
    list_str = re.split('[:;, \n]', str_old.strip())
    

    for str in list_str:
        if not str.strip() or len(str) < 10: continue

        if str in LIST_TEXT_SKIP: continue

        if any(char in str for char in SPECIAL_CHAR): continue

        if not has_dash(str) and has_no_uppercase(str):

            result.append(str)
        elif  has_dash(str) and has_no_lowercase(str):

            result.append(str)

    return result

def handle_to_get_uid(str_old: str):
    if not str_old: return None

    result = []
    list_str = re.split('[:;, \n]', str_old.strip())

    for str in list_str:
        if not str.strip() or len(str) < 10: continue

        if str in LIST_TEXT_SKIP: continue

        if any(char in str for char in SPECIAL_CHAR): continue

        if not has_dash(str) and not has_no_lowercase(str) and not has_no_uppercase(str):

            result.append(str)

    return result

def clean_link(link_old: str):
    return re.split('[;,\n]', link_old.strip())

def str_to_bool(value):
    return str(value).lower() in ("true", "1")

def extract_drive_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Với link dạng: https://drive.google.com/open?id=...
    if 'id' in query_params:
        return query_params['id'][0]

    # Với link dạng: https://drive.google.com/file/d/FILE_ID/view
    path_parts = parsed_url.path.split('/')
    if 'file' in path_parts and 'd' in path_parts:
        try:
            idx = path_parts.index('d')
            return path_parts[idx + 1]
        except IndexError:
            pass

    return None

def convert_datetime_from_str(str_dt: str):
    if not str_dt.strip():
        return None

    try:
        return parser.parse(str_dt)
    except (ValueError, TypeError):
        return None