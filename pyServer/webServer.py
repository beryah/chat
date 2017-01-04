from flask import Flask, render_template, request
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='$$',
        block_end_string='$$',
        variable_start_string='$',
        variable_end_string='$',
        comment_start_string='$#',
        comment_end_string='#$',
    ))

app = CustomFlask(__name__)
app.secret_key = '\xe5xt\xc2e\x97\xdb[\xda\x1f\x9a\x96cV|\xe5E\xc1\xbc\x1c\x05\xa9\x8f2'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
