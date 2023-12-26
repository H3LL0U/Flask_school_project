from flask import Flask, render_template , request
import sqlite3
app = Flask(__file__)

@app.route("/over_ons")
def over_ons():
    return render_template("sport_main.html", root_name = "/over_ons")

def add_to_the_database(table_name,**table_values):
    try:
        conn = sqlite3.connect("aangemelden.db")
        cur = conn.cursor()
        create_table = f"CREATE TABLE IF NOT EXISTS {table_name} {('id INTEGER PRIMARY KEY AUTOINCREMENT' , )+ tuple((element+ ' TEXT' for element in  tuple(table_values.keys())))};"
        cur.execute(create_table)
        insert_table = f"INSERT INTO {table_name} {tuple((element+ ' TEXT' for element in  tuple(table_values.keys())))}  VALUES {tuple(table_values.values())};"
        cur.execute(insert_table)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        conn.close()
        print(error)
    finally:
        print("Done!")
    
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
    app.run(port= 5000, debug=True)
