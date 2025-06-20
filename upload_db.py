# このスクリプトをcronで任意タイミングで実行設定する
import requests

url = 'https://plant-dashboard.fly.dev/upload'
# files = {'dbfile': open('/home/aiot/raspberrypi_green/sensor_data.db', 'rb')}
files = {'dbfile': open('C:/Users/ai/Projects/plant-dashboard/sensor_data.db', 'rb')}

response = requests.post(url, files=files)

print("アップロード結果:", response.text)
