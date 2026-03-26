From flask import Flask, render_template

App = Flask(_name_)

@app.route("/")
Def home():
    Return render_template("index.html")


App.run()
