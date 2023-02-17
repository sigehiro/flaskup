# 必要なモジュールのインポート
from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

app = Flask(__name__)

class InputForm(Form):
    InputFormTest = StringField('文字を入力してください', [validators.InputRequired()])

    submit = SubmitField('送信')

@app.route('/', methods =['GET', 'POST'])
def input():
    form = InputForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', forms=form)
        else:
            outputname_ = request.form['InputFormTest']
            return render_template('result.html', outputname= outputname_)
    elif request.method == 'GET':
        return render_template('index.html', forms=form)

if __name__ == '__main__':
    app.run(debug=True)
