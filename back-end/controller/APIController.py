from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import math

from controller import SheetController
from service import StringService

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}}, supports_credentials=True)

def api_get_id_bill(links):
    return ""

ID_SHEET = "15f_OxWHC_OLuDryjyDBmD3WDN01DDuDYi573UuG3RVQ"
NAME_SHEET = "Form Responses 1"
LIST_COL = [i for i in range(22)]

@app.route('/getdata')
def get_data():
    try:
        date_min = StringService.convert_datetime_from_str(date_min) if(date_min := request.args.get("dateMin")) is not None else None
        date_max = StringService.convert_datetime_from_str(date_max) if(date_max := request.args.get("dateMax")) is not None else None
        
        case_min = int(case_min) if (case_min := request.args.get("caseMin")) is not None else None
        case_max = int(case_max) if (case_max := request.args.get("caseMax")) is not None else None
        
        status = request.args.get("status")
        
        is_cache = StringService.str_to_bool(request.args.get("cache"))
        is_refresh = StringService.str_to_bool(request.args.get("refresh"))

        data = SheetController.get_data_from_gg_sheet(
            ID_SHEET, 
            NAME_SHEET, 
            LIST_COL, 
            date_min, 
            date_max, 
            case_min, 
            case_max, 
            status, 
            is_cache, 
            is_refresh)

        return {
            "length": math.ceil(len(data) / 100),
            "data" : data
        }
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/firstGetData')
def first_get():
    page_data = SheetController.pagination_data(ID_SHEET, NAME_SHEET, LIST_COL)

    return {
        "data": page_data["data"],
        "length": math.ceil(int(page_data["length"]) /100)
    }

@app.route('/pageData')
def page_get():
    page = int(page) if (page := request.args.get("page")) is not None else None
    page_data = SheetController.pagination_data(ID_SHEET, NAME_SHEET, LIST_COL, page=page)

    return {
        "data": page_data["data"],
        "length": math.ceil(int(page_data["length"]) /100)
    }