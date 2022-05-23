from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/authorize")
def authorize_yandex_drive(client_id="f93c10ef8e2f42708d0f186eaf4997eb"):
    # AQAAAAAO9KMZAAfsv2f3Hl_FUEp4oEJ3YcAFGJM
    url = f"https://oauth.yandex.ru/authorize?response_type=token&client_id={client_id}"
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return "None"


@app.route("/create", methods=['POST'])
def create(path, session="AQAAAAAO9KMZAAfsv2f3Hl_FUEp4oEJ3YcAFGJM"):
    url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={path}"
    payload = {}
    headers = {
        'Authorization': f'OAuth {session}'
    }
    upload_url = requests.request("GET", url, headers=headers, data=payload)
    return upload_url


@app.route("/upload")
def upload(upload_url, file):
    payload = "<file contents here>"
    headers = {
        'Content-Type': 'image/png'
    }
    response = requests.request("PUT", upload_url, headers=headers)
    print(response.text)


if __name__ == '__main__':
    app.run()
