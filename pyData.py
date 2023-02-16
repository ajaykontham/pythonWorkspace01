
import urllib.request
import json

def main():
    # weburl = urllib.request.urlopen("http://google.com")
    # data = weburl.read()
    # print("Result code:", weburl.getcode())
    # print(data)

    weburl = urllib.request.urlopen("http://date.jsontest.com")
    if weburl.getcode() == 200:
        jsonData = json.loads(weburl.read())
        print(jsonData)
        if "date" in jsonData:
            print(jsonData["date"])


if __name__ == "__main__":
    main()