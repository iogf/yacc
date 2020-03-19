"""
"""

from yacc.lexer import Lexer, LexMap, LexSeq, LexNode, SeqNode, XSpec
from yacc.token import DoubleQuote, String, Blank

class StringTokens(XSpec):
    lexmap = LexMap()

    t_dquote = LexSeq(SeqNode(r'\"', DoubleQuote),
    SeqNode(r'[^\"]+', String), SeqNode(r'\"', DoubleQuote))

    t_blank = LexNode(r' +', type=Blank)
    lexmap.add(t_dquote, t_blank)

    root = [lexmap]

lex = Lexer(StringTokens)
print('Example 1!')
data = '" This will"       "rock!"     "For sure!"'
tokens = lex.feed(data)
print('Consumed:', list(tokens))


