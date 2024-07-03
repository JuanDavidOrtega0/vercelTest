from flask import Flask, render_template

app = Flask("my-first-website-in-python")

@app.route("/")
def home():
    return render_template("index.html", contenido = "Hola Mundo desde Python, Mi nombre es Juan David Ortega")

@app.route("/about")
def about():
    return "This is a about page"

@app.route("/<name>")
def return_dynamic_content(name):
    return render_template("name.html", contenido = name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')