from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('标题', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('内容', validators=[DataRequired(), Length(1, 300)])
    submit = SubmitField('发布')


class CommentForm(FlaskForm):
    body = TextAreaField(validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('发布')
