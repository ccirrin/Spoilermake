from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, AnyOf
from flask_navigation import Navigation


app = Flask(__name__)
nav = Navigation(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'reallyreallyreallysecretkey'

class analyze_form(FlaskForm):
    uri = StringField(u'URI: ', validators=[Required()])
    submit = SubmitField(u'Submit')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    form=analyze_form()
    uri = None
    if form.validate_on_submit():
        uri = form.uri.data
        return render_template('analyze.html', form=form, uri=uri)
    return render_template('analyze.html', form=form, uri=uri)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    return render_template('generate.html')

@app.route('/environment', methods=['GET', 'POST'])
def environment():
    return render_template('environment.html')

#Run app
if __name__ == '__main__':
    app.run()