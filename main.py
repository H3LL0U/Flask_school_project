from flask import Flask, render_template
app = Flask(__file__)
@app.route("/")
def home():
    return render_template("sport_main.html", root_name = "/")
@app.route("/over_ons")
def about_us():
    return render_template("sport (1).html", root_name = "/over_ons")



if __name__ =="__main__":
    app.run(port= 5000, debug=True)
