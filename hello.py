from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave forte'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')

