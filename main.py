from flask import Flask, render_template, url_for

import os

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/gallery/")
def gallery():
	return render_template("gallery.html")

@app.route("/music/")
def music():
    return render_template("music.html")

@app.route("/game/")
def game():
	return render_template("game.html")

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