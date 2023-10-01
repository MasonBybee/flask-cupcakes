from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField
from wtforms.validators import InputRequired, URL, Optional, ValidationError

sizes = ["Small", "Medium", "Large"]


def validate_rating(form, field):
    if field.data < 0 or field.data > 10:
        raise ValidationError("Rating must be between 0 and 10")


class CupcakeForm(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired()])
    size = SelectField(
        "Size",
        choices=[(size.lower(), size) for size in sizes],
        validators=[InputRequired()],
    )
    rating = FloatField("Rating", validators=[InputRequired()])
    image = StringField("Image", validators=[URL(), Optional()])
