from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
title = ''
content = ''
repeat = 0


@app.route("/", methods=["POST", "GET"])
def home():
    global title
    global content
    if request.method == 'POST':
        title = request.form["title"]
        content = request.form["content"]
#        return redirect(url_for('home'))
    return render_template("index.html", title=title, content=content, repeat=repeat)


if __name__ == "__main__":
    app.run(debug=True)
