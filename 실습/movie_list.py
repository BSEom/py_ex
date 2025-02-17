import os
import sys
import requests as req
from dotenv import load_dotenv
import json

def serch_movie(args):
    
    load_dotenv()

    serch_date = args[0]

    
    MOVIE_KEY = os.getenv("MOVIE_KEY")
    key = MOVIE_KEY

    
    url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=" + key + "&targetDt=" + serch_date    # JSON 결과
    web = req.get(url)
    html = web.json()
    data = html['boxOfficeResult']['dailyBoxOfficeList']

    print('\n'+"="*30)
    
    for x in data:
        print(f'{x['rank']}위 - {x['movieNm']}')
        # print(x['movieNm'])

    print("="*30 + '\n')

if __name__ == "__main__":
    arg = sys.argv[1:]
    serch_movie(arg)