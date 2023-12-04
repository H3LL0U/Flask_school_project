from flask import Flask, render_template
app = Flask(__file__)
@app.route("/")
def home():
    return  "hi"



if __name__ =="__main__":
    app.run(port= 5000, debug=True)
