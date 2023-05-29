import requests
import json
import sqlite3

connection = sqlite3.connect('fun_facts.sqlite')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS fun_facts
              (id INTEGER PRIMARY KEY,
              fact TEXT,
              category TEXT )
              ''')
connection.commit()


def insert_facts(fact, category):
    cursor.execute('''INSERT INTO fun_facts (fact, category)
              VALUES (?, ?)''', (fact, category))
    connection.commit()

raw_fun_fact = requests.get("https://asli-fun-fact-api.herokuapp.com/")


if raw_fun_fact.status_code == 200:

    fun_fact = json.loads(raw_fun_fact.text)
    data = fun_fact['data']

    with open("fun_fact.json", "w") as f:
        json.dump(fun_fact, f)
    insert_facts(data['fact'], data['cat'])

    print("Fun fact: " + data['fact'])
