import os
import sys
import urllib.request
from dotenv import load_dotenv
import json

def serch(args):
    
    load_dotenv()

    serch_category = args[0]
    serch_text = args[1]
    
    
    MY_ID = os.getenv("MY_ID")
    MY_SECRET = os.getenv("MY_SECRET")
    
    client_id = MY_ID
    client_secret = MY_SECRET
    encText = urllib.parse.quote(serch_text)
    url = "https://openapi.naver.com/v1/search/" + serch_category + ".json?query=" + encText + '&display=10&start=1&sort=sim'    # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        result = response_body.decode('utf-8')
        data = json.loads(result)   # 리스트에서 딕셔너리로
        ldata = data['items']

        for n in ldata:
            print('\n')
            print(n['title'].replace('<b>', '').replace('</b>', ''))
            print(n['description'])
            print(n['link'])
        
    else:
        print("Error Code:" + rescode)


if __name__ == "__main__":
    st = sys.argv[1:]
    serch(st)