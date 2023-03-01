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

html = '''
<html>

    <head>

    <style>
        html {
            color: white;
            background-image: url("https://phonoteka.org/uploads/posts/2021-05/1620203343_9-phonoteka_org-p-fon-dlya-zuma-tyurma-11.png");
        }
        p{
            font-size: 2em;
        }

    </style>
    </head>
    <body>
      <form action = "http://localhost:5000/out" method = "post">
         <p>Введите имя преступника!:</p>
         <p><input type = "text" name = "item" /></p>
         <p><input type = "submit" value = "Найти гниду" /></p>
      </form>   
   </body>
</html>
'''

html1 = '''
<html>

    <head>

    <style>
        html {
            color: white;
            background-image: url("https://phonoteka.org/uploads/posts/2021-05/1620203343_9-phonoteka_org-p-fon-dlya-zuma-tyurma-11.png");
        }
        p{
            font-size: 2em;
        }

    </style>
    </head>
    <h1>Гнида Обнаружена</h1>
</html>
'''

from flask import Flask
from flask import redirect, url_for, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def lcpd():
    return html


@app.route("/out", methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        item = request.form['item']

        return html1 + f'''
        <br>Имя:      {g[item]['name']}</br> 
        <br>Возраст:  {g[item]['age']}  </br>
        <br>Город:    {g[item]['city']} </br>
        '''


app.run()




