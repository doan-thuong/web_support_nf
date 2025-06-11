from flask import Flask
from flask_cors import CORS

from service import SheetService

app = Flask(__name__)

CORS(app, resources={r"/getdata": {"origins": "http://127.0.0.1:5500"}})

def api_get_id_bill(links):
    return ""

@app.route('/getdata')
def get_data():
    id_sheet = "15f_OxWHC_OLuDryjyDBmD3WDN01DDuDYi573UuG3RVQ"
    name_sheet = "Form Responses 1"
    list_col = [i for i in range(22)]
    
    data = SheetService.get_data_from_gg_sheet(id_sheet, name_sheet, list_col, "")
    
    return data