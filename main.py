from flask import Flask, render_template, url_for

import os

app = Flask(__name__, static_url_path='/static')
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/game/")
def game():
	return render_template("game.html")

@app.route("/research/")
def research():
    return render_template("research.html")

@app.route("/project/")
def project():
    return render_template("project.html")

@app.route("/teaching/")
def teaching():
    return render_template("teaching.html")

@app.route("/courseWeb/")
def courseWeb():
    return render_template("courseWeb.html")

@app.route("/coursePython1/")
def coursePython1():
    return render_template("coursePython1.html")

@app.route("/coursePython2/")
def coursePython2():
    return render_template("coursePython2.html")

@app.route("/courseCS/")
def courseCS():
    return render_template("courseCS.html")

@app.route("/presentation/")
def presentation():
    return render_template("presentation.html")

@app.route("/openCourse/")
def openCourse():
    return render_template("openCourse.html")

# ///////////////////////////////////////////////////////////////////////// overwrite
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
# /////////////////////////////////////////////////////////////////////////

if __name__ == '__main__':
	app.run(debug = True)

    