from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

from controller import SheetController
from service import StringService

app = Flask(__name__)

CORS(app, resources={r"/getdata": {"origins": "http://127.0.0.1:5500"}})

def api_get_id_bill(links):
    return ""

@app.route('/getdata')
def get_data():
    id_sheet = "15f_OxWHC_OLuDryjyDBmD3WDN01DDuDYi573UuG3RVQ"
    name_sheet = "Form Responses 1"
    list_col = [i for i in range(22)]
    
    try:
        case_min = int(case_min) if (case_min := request.args.get("caseMin")) is not None else None
        case_max = int(case_max) if (case_max := request.args.get("caseMax")) is not None else None
        status = request.args.get("status")
        is_cache = StringService.str_to_bool(request.args.get("cache"))

        data = SheetController.get_data_from_gg_sheet(id_sheet, name_sheet, list_col, case_min, case_max, status, is_cache)

        return data
    except Exception as e:
        return jsonify({"error": str(e)}), 400