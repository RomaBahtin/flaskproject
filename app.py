import json
data = '''
{"Роман Бахтин": {
    "name": "БАХТА",
    "age": 17,
    "city": "Лесное"
    },



"Егор Смоликов": {
    "name": "СМОЛА",
    "age": 17,
    "city": "Нелидово"
    }
}
'''
data1 = json.loads(data)

with open("hhh.json", "w", encoding="UTF-8") as f:
    json.dump(data1, f)
with open("hhh.json", "r", encoding="UTF-8") as f:
    g = json.load(f)


from flask import Flask, render_template
from flask import redirect, url_for, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def lcpd():
    return render_template("main.html")


@app.route("/out", methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        item = request.form['item']
        # тут нужно проверить, есть ли наше имя в списке
        if item in g:
            return render_template('main1.html') + f'''
            <br>Имя:      {g[item]['name']}</br> 
            <br>Возраст:  {g[item]['age']}  </br>
            <br>Город:    {g[item]['city']} </br>
            '''
        else:
            return render_template('main.html')


if __name__ == '__main__':
    app.run(debug = True)




