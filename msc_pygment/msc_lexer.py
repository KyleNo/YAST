from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Name, String, Number, Operator, Text, Punctuation, Comment

class MscLexer(RegexLexer):
    name = 'MSC2'
    aliases = ['msc2']
    filenames = ['*.msc']

    tokens = {
        'root': [
            # Comments
            (r'^\s*#\s.*$', Comment),

            # Strings
            (r'"', String.Double, 'string'),

            # Match @player, @bypass, @command, @console followed by unquoted string
            (r'(@(?:player|bypass|command|console))(\s+)', bygroups(Keyword, Text), 'unquoted_string'),

            (r'(@define|@var)\b', Keyword.Declaration),

            (r'(@elseif)', Keyword.Control),
            (r'(@(?:if|fi|else|for|done|return))', Keyword.Control),

            # Keywords (mostly control, some need special treatment)
            #(r'@(cancel|chatscript|cooldown|delay|done|else|elseif|fast|fi|for|global_cooldown|if|prompt|return|slow|using)\b', Keyword.Control),
            # All @commands (any word after @)
            (r'(@\w+)', bygroups(Keyword)),


            # Numeric literals
            (r'(?<!\w)(\d+\.\d*[Dd]?)(?!\w)', Number.Float),
            (r'(?<!\w)(\d+[Lltsmhdwy]?)(?!\w)', Number.Integer),
            (r'(?<!\w)(true|false)(?!\w)', Keyword.Constant),

            # Types
            (r'(?<!\w)(String|Int|Long|Float|Double|Boolean|Player|Entity|Block|Item|Location|BlockLocation|Position|Vector2|BlockVector2|Vector3|BlockVector3|Region)(?!\w)', Name.Tag),

            # Includes
            # (r'<#[^#][^\n]*?>', Name.Tag),

            # Operators
            (r'[\+\-\*/=!\&\|\%\^<>]|\|\||&&', Operator),

            # Punctuation
            (r'[.,\(\)\[\]\{\}]|\:\:', Punctuation),

            # Custom Types
            (r'\b[A-Z][a-zA-Z0-9_]*\b', Name.Class),

            # Fallback
            # (r'\w+', Name.Variable),

            # Identifiers
            (r'\b\w+\b', Name.Variable),

            # Whitespace
            (r'\s+', Text),

        ],

        'string': [
            (r'\{\{', String.Interpol, 'interpolation'),
            (r'\\.', String.Escape),
            (r'"', String.Double, '#pop'),
            (r'[^\\{"]+', String.Double),
            (r'.', String.Double),
        ],

        'interpolation': [
            (r'\}\}', String.Interpol, '#pop'),
            (r'[^}]+', Name.Variable),
            (r'.', String.Interpol),
        ],

        # Unquoted strings with interpolation
        'unquoted_string': [
            (r'\{\{', String.Interpol, 'interpolation'),
            (r'[^\n{}]+', String),
            (r'.', String),
            (r'\n', Text, '#pop'),
        ],
    }