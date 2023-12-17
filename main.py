from flask import Flask, render_template
app = Flask(__file__)
@app.route("/over_ons")
def over_ons():
    return render_template("sport_main.html", root_name = "/over_ons")
@app.route("/waarom_is_sporten_belangrijk")
def about_us():
    return render_template("sport (1).html", root_name = "/waarom_is_sporten_belangrijk")
@app.route("/")
def home ():
    return render_template("home.html", root_name = "/")


if __name__ =="__main__":
    app.run(port= 5000, debug=True)
