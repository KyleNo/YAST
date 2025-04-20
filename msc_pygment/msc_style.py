from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Token

class MscLight(Style):
    default_style = ""
    styles = {
        Comment:                'italic #A0A1A7',
        Keyword:                'bold #e65cac',
        # Keyword.Declaration:    'bold #A626A4',
        Keyword.Control:        'bold #0000FF',
        Keyword.Type:           'bold #0184BC',
        Name:                   '#383A42',
        Name.Class:             'bold #0184BC',
        Name.Tag:               'bold #0184BC',
        String:                 '#50A14F',
        Number:                 '#986801',
        Operator:               '#E45649',
        Error:                  'border:#E45649',
        String.Interpol:        'bold #e36209',
        Token.Interpolation:    'bold #e36209',
        Token.PromptCommand:    'bold #005cc5',
        Token.PromptArgument:   '#24292e',
    }

class MscDark(Style):
    default_style = ""
    styles = {
        Comment:                'italic #02a302',
        Keyword:                'bold #7126fc',
        Keyword.Declaration:    'bold #1f8ef0',
        Keyword.Control:        'bold #0000FF',
        Keyword.Type:           'bold #22863a',
        Name:                   '#333333',
        Name.Class:             'bold #6f42c1',
        Name.Tag:               'bold #FFFF00',
        String:                 '#FF5cc5',
        Number:                 '#005cc5',
        Operator:               '#d73a49',
        Error:                  'border:#FF0000',
        Token.Interpolation:    'bold #e36209',
        Token.PromptCommand:    'bold #005cc5',
        Token.PromptArgument:   '#24292e',
    }