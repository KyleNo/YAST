from pygments.lexer import RegexLexer, bygroups, using, this
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

            (r'(@using)(\s+)(\w+)', bygroups(Keyword, Text, Name.Namespace)),

            (r'(@elseif)', Keyword.Control),
            (r'(@(?:if|fi|else|for|done|return)|in)', Keyword.Control),

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

            # Namespaced object method call
            (r'\b([a-zA-Z]\w*)(::)([a-zA-Z_]\w*)(\.)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Namespace, Punctuation, Name.Variable, Punctuation, Name.Function, Text, Punctuation)),

            # Namespaced function call
            (r'\b([a-zA-Z]\w*)(::)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Namespace, Punctuation, Name.Function, Text, Punctuation)),

            # Regular method call
            (r'\b([a-zA-Z_]\w*)(\.)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Variable, Punctuation, Name.Function, Text, Punctuation)),

            # Function call
            (r'\b([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Function, Text, Punctuation)),

            # Optional: fallback chained method parsing
            (r'\b([a-z]\w*)((?:\.[a-z]\w*\s*\(\))*)', 
            bygroups(Name.Variable, using(this))),

            (r'\b([a-zA-Z]\w*)(::)([a-zA-Z_]\w*)((?:\.[a-z]\w*\s*\(\))*)', 
            bygroups(Name.Namespace, Punctuation, Name.Variable, using(this))),

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

        # 'function'

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