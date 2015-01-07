from django.core.exceptions import ValidationError
import re


def validate_pennname(pennname):
    """
    Ensure PennName is conforms to this definition:

       2-8 lowercased letters or digits where the first character is a letter

    from: http://www.upenn.edu/computing/pennnames/
    """
    regex = r'^[a-z][a-z0-9]{1,7}$'
    if not re.match(regex, pennname):
        msg = "'{}' is not a valid PennName."
        raise ValidationError(msg)


def validate_pennid(pennid):
    """Ensure PennID is 8 digits."""
    regex = r'^[0-9]{8}$'
    if not re.match(regex, pennid):
        msg = "'{}' is not a valid PennID."
        raise ValidationError(msg)
