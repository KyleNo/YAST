from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Token, Punctuation

class MscLight(Style):
    default_style = ""
    styles = {
        Comment:                'italic #6A9955',
        Keyword:                'bold #7A45A2',
        Keyword.Control:        'bold #0069B1',
        Keyword.Type:           'bold #0069B1',
        Keyword.Constant:       'bold #098658',
        Name:                   '#333333',
        Name.Class:             'bold #2A7F62',
        Name.Tag:               'bold #2A7F62',
        Name.Function:          'bold #AA7700',
        Name.Namespace:         'bold #C2185B',
        String:                 '#A31515',
        String.Interpol:        'bold #AF8500',
        Number:                 '#098658',
        Operator:               '#000000',
        Punctuation:            '#000000',
        Error:                  'border:#E53935',
        Token.Interpolation:    'bold #AF8500',
        Token.PromptCommand:    'bold #005cc5',
        Token.PromptArgument:   '#444444',
    }

class MscDark(Style):
    default_style = ""
    styles = {
        # Comments
        Comment:                'italic #6A9955',

        # Keywords
        Keyword:                'bold #C586C0',
        Keyword.Control:        'bold #D16969',
        Keyword.Declaration:    'bold #C586C0',
        Keyword.Type:           'bold #4EC9B0',
        Keyword.Constant:       'bold #B5CEA8',

        # Names
        Name:                   '#D4D4D4',
        Name.Variable:          '#9CDCFE',
        Name.Function:          'bold #DCDCAA',
        Name.Namespace:         'bold #569CD6',
        Name.Class:             'bold #4EC9B0',
        Name.Tag:               'bold #4EC9B0',

        # Strings
        String:                 '#CE9178',
        String.Double:          '#CE9178',
        String.Interpol:        'bold #FFD700',

        # Numbers
        Number:                 '#B5CEA8',

        # Operators and punctuation
        Operator:               '#D4D4D4',
        Punctuation:            '#D4D4D4',

        # Misc
        Error:                  'border:#E45649',
        Token.Interpolation:    'bold #FFD700',
        Token.PromptCommand:    'bold #569CD6',
        Token.PromptArgument:   '#D4D4D4',
    }
