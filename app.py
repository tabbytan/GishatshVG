from flask import Flask , render_template, request
from bs4 import BeautifulSoup
import urllib.request, urllib.parse

app =  Flask(__name__ , template_folder='webpages')

@app.route('/')
def test():
    return "Hello, World!" 

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    val = urllib.parse.quote(query.encode('utf-8'))
    print(val)
    yyturl = (f'https://www.cardrush-vanguard.jp/product-list?keyword={val}&Submit=%E6%A4%9C%E7%B4%A2')
    print(yyturl)
    response = urllib.request.urlopen(yyturl).read()
    soup = BeautifulSoup(response, 'html.parser')
    list = soup.find_all('div', class_='item_data')

    for item in list:
        print(item.a.p.find('span', class_='goods_name'))
        print(item.a.find('span', class_='figure'))
    
    return "Check Console"

if __name__ == '__main__': 
    app.run(debug=True)