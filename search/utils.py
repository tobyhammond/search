import re

PUNCTUATION_REGEX = re.compile(ur'[^\w -\'"+]', re.U)
WHITESPACE_REGEX = re.compile(ur'[\s]+', re.U)


def clean_value(value):
    value = value or u''
    value = PUNCTUATION_REGEX.sub(u' ', value)
    value = WHITESPACE_REGEX.sub(u' ', value)
    return value.strip()
