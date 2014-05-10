from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired

class PoetrySearchForm(Form):
    keyword = TextField('Keywords', validators=[DataRequired()])
    url = BooleanField('Remove URLs')
    emoji = BooleanField('Remove Emoji')
    letter_ratio = TextField('Letter Ratio') # 0 to 1
    syllabus = TextField('Syllabus Format')
    blacklist = TextField('Blacklist')
