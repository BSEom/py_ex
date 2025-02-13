import requests as req
import sys


def show_stock(args):
    
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    web = req.get(url)
    html = web.text

    
    arg = args
    
    f1 = html.find(arg[0])
        
    f2 = html[f1:f1 + 100].find('<td class="number">')
        
    f3 = html[f1:f1 + 100][f2:60].find('</td>')
        
    f4 = html[f1:f1 + 100][f2:60][:f3].replace('<td class="number">', '')
        
        
    if f4 == '':
        print(f'\n 정확히 입력해 주세요. \n')
    else:
            print(f'\n{arg[0]}: {f4}원\n')


if __name__ == "__main__":
    args = sys.argv[1:]
    show_stock(args)











