import requests as req
import sys

url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text


args = sys.argv[1:]
f1 = html.find(args[0])

f2 = html[f1:f1 + 100].find('<td class="number">')

f3 = html[f1:f1 + 100][f2:60].find('</td>')

f4 = html[f1:f1 + 100][f2:60][:f3].replace('<td class="number">', '')

if f4 == '':
    print(f'\n 정확히 입력해 주세요. \n')
else:
    print(f'\n{args[0]}: {f4}원\n')

