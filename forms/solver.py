from wtforms import FloatField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class SolverForm(FlaskForm):
    a = FloatField('a')
    b = FloatField('b')
    c = FloatField('c')
    d = FloatField('d')
    e = FloatField('e')
    submit = SubmitField('Решить')
