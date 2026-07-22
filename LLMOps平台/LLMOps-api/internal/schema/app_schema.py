from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CompletionReq(FlaskForm):
    query = StringField("query", validators=[
        DataRequired(message="query is required"),
        Length(max=2000, message="query cannot be longer than 2000 characters")
    ])
