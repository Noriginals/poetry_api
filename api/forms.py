from flask_wtf import Form
from wtforms import TextField, BooleanField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class PoetrySearchForm(Form):
    keyword = TextField('Keywords', validators=[DataRequired()])
    url = BooleanField('Remove URLs')
    emoji = BooleanField('Remove Emoji')
    letter_ratio = DecimalField('Letter Ratio', places=3, validators=[NumberRange(0, 1)]) # 0 to 1
    syllabus = TextField('Syllabus Format')
    blacklist = TextField('Blacklist')
