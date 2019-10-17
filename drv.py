import requests
from tqdm import tqdm

#get fallback url
def get_link(url):
    json_url = url[0:-1] + ".json"
    resp = requests.get(json_url, headers = {"user-agent": "Mozilla/5.0"})
    fallback = resp.json()[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
    return fallback

#download and save in memory
def download_video(url):
    fallback = get_link(url)
    resp = requests.get(fallback, stream = True)
    file_size = int(resp.headers["Content-length"])
    local_filename = "C:/Users/Robson Jesus/Downloads/" + url.split('/')[-2] + ".mp4"
    bar = tqdm(total=file_size, unit='iB', unit_scale=True)
    with open(local_filename, "wb") as _file:
        for data in resp.iter_content(1024):
            _file.write(data)
            bar.update(len(data))
    bar.close()

def main():
    url = input("url: ")
    download_video(url)

if __name__ == "__main__":
    main()