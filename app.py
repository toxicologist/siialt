from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html', bgimage=True, show_title_icon=True)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
