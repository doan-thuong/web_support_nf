import requests
import service.StringService as strService
from service import SheetService
from service import DBService
from controller.APIController import app

from entity.User import User

# url = 'https://your-service-name.onrender.com/ocr'
# path_file = "" 
# files = {'image': open(path_file, 'rb')}
# res = requests.post(url, files=files)

# id_sheet = "1WtpFPPX6frk29T2225dhgEtxj5qotQv1hPPOixqZIOM"
# tab_name = "active"
# list_col = [i for i in range(22)]
# status = "Done"

# data_from_sheet = SheetService.get_data_from_gg_sheet(id_sheet, tab_name, list_col, status)

# for row in data_from_sheet:
#     user = SheetService.handl_data_fom_sheet(row)
#     print(user)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)