from flask import Flask, render_template , request
import sqlite3
app = Flask(__name__)

@app.route("/over_ons")
def over_ons():
    return render_template("sport_main.html", root_name = "/over_ons")


def add_to_the_database(table_name, **table_values):
    try:
        conn = sqlite3.connect("aangemelden.db")
        cur = conn.cursor()

       
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, "
        create_table_query += ", ".join([f"{key} TEXT" for key in table_values.keys()])
        create_table_query += ");"
        cur.execute(create_table_query)

        
        insert_query = f"INSERT INTO {table_name} ({', '.join(table_values.keys())}) VALUES ({', '.join(['?' for _ in table_values.values()])});"
        cur.execute(insert_query, list(table_values.values()))

        conn.commit()
        print("Done!")
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
@app.route("/waarom_is_sporten_belangrijk", methods = ["POST", "GET"])
def waarom_is_sporten_belangrijk():
    if request.method == "POST":
        add_to_the_database("aangemelden", naam = request.form["naam"] , email = request.form["email"] , tel = request.form["tel"])
    
    return render_template("sport (1).html", root_name = "/waarom_is_sporten_belangrijk")

@app.route("/", methods = ["POST","GET"])
def home ():
    if request.method == "POST":
        add_to_the_database("aangemelden", naam = request.form["naam"] , email = request.form["email"] , tel = request.form["tel"])
    return render_template("home.html", root_name = "/")


if __name__ =="__main__":
    app.run(host="0.0.0.0",port= 5000)
