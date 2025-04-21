from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Name, String, Number, Operator, Text, Punctuation, Comment

class NmsLexer(RegexLexer):
    name = 'NMS'
    aliases = ['nms']
    filenames = ['*.nms']

    tokens = {
        'root': [
            # Comments
            (r'#.*$', Comment),

            # Namespaced object method call: Namespace::Object.methodName()
            (r'\b([a-zA-Z]\w*)(::)([A-Z]\w*)(\.)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Namespace, Punctuation, Name.Class, Punctuation, Name.Function, Text, Punctuation)),

            (r'\b([a-zA-Z]\w*)(::)([A-Z]\w*)',
            bygroups(Name.Namespace, Punctuation, Name.Class)),

            # Namespaced function call: Namespace::functionName()
            (r'\b([a-zA-Z]\w*)(::)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Namespace, Punctuation, Name.Function, Text, Punctuation)),

            # Regular method call: object.methodName()
            (r'\b([a-z_]\w*)(\.)([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Variable, Punctuation, Name.Function, Text, Punctuation)),

            # Standalone function call: functionName()
            (r'\b([a-z]\w*)(\s*)(\()', 
            bygroups(Name.Function, Text, Punctuation)),

            # Strings with interpolation
            (r'"', String.Double, 'string'),

            (r'(@namespace)(\s+)(\w+)',
             bygroups(Keyword.Declaration, Text, Name.Namespace)),

            # Declaration keywords
            (r'@(class|endnamespace|endclass)\b', Keyword.Declaration),

            # Keywords
            (r'\b(final|relative)\b', Keyword),

            # Boolean literals
            (r'(?<!\w)(true|false)(?!\w)', Keyword.Constant),

            # Float literals
            (r'(?<!\w)(\d+\.\d*[Dd]?)(?!\w)', Number.Float),

            # Integer literals
            (r'(?<!\w)(\d+[Lsmhdw]?)(?!\w)', Number.Integer),

            # Types (Custom types starting with capital letter)
            (r'\b[A-Z][a-zA-Z0-9_]*\b', Name.Class),

            # Operators
            (r'[\+\-\*/=!\&\|\%\^]', Operator),

            # Punctuation
            (r'[.,\(\)\[\]\{\}]|\:\:', Punctuation),

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
    }