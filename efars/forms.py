from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms import SubmitField
from config import Config


class FileForm(FlaskForm):
    """
        FileAllowed(['allowed file extensions'])
        Verify file by extension based on what's inside FileAllow
    """
    file = FileField('File', validators=[FileRequired(), FileAllowed([*Config.ALLOWED_EXTENSIONS]),
                                         FileSize(max_size=Config.MAX_CONTENT_LENGTH)])
    submit = SubmitField()
