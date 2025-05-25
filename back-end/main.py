import requests

url = 'https://your-service-name.onrender.com/ocr'
path_file = "" 
files = {'image': open(path_file, 'rb')}
res = requests.post(url, files=files)