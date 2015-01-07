from django.core.exceptions import ValidationError


def validate_pennname(pennname):
    """
    Ensure PennName is conforms to this definition:

       2-8 lowercased letters or digits where the first character is a letter

    from: http://www.upenn.edu/computing/pennnames/
    """


def validate_pennid(pennid):
    """Ensure PennID is 8 digits."""

