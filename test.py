import os
import requests


def auth():
    url = "https://oauth.yandex.ru/authorize?response_type=token&client_id=f93c10ef8e2f42708d0f186eaf4997eb"
    payload = {}
    headers = {
        'Cookie': 'yandexuid=483361671653313224'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)


def create_upload_urls(upload_paths):
    upload_urls = []
    for path in upload_paths:
        url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={path}"
        payload = {}
        headers = {
            'Authorization': 'OAuth AQAAAAAO9KMZAAfsv2f3Hl_FUEp4oEJ3YcAFGJM'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        upload_urls.append(response.json())
    return upload_urls


def upload(upload_urls, paths):
    files = []
    for path in paths:
        with open(path, 'rb') as f:
            data = f.read()
            files.append(data)

    for index, url in enumerate(upload_urls):
        print(index)
        print(url)
        # print(files[index])
        payload = files[index]
        headers = {
            'Content-Type': 'application/octet-stream'
        }
        response = requests.request("PUT",
                                    url["href"],
                                    headers=headers,
                                    data=payload)
        print(response.text)


def main(files):
    drive_path = "/Microscope/"
    file_paths = files
    upload_paths = [drive_path + os.path.basename(path) for path in file_paths]
    print(upload_paths)

    urls = create_upload_urls(upload_paths)
    upload(urls, file_paths)


if __name__ == "__main__":
    file_paths = [
        "/home/sfelshtyn/Python/cloud-service/static/Screenshot from 2022-04-24 20-52-45.png",
        "/home/sfelshtyn/Python/cloud-service/static/data2005.csv",
        "/home/sfelshtyn/Python/cloud-service/static/AnimatedSticker.tgs"
    ]
    main(file_paths)
