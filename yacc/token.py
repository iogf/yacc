class XNode:
    def __init__(self):
        pass

class PTree(list):
    """
    """
    __slots__ = ['type', 'result', 'data']

    def __init__(self, type):
        super(PTree, self).__init__()
        self.type = type
        self.data = type
        self.result = None

    def eval(self, handle):
        if handle:
            self.result = handle(*self)

    def val(self):
        return self.result

class Token:
    __slots__=['data', 'offset', 'type', 'value', 'pos', 'start', 'end']

    def __init__(self, data, type=None, cast=None, start=None, end=None):
        self.data = data
        self.value = cast(data) if cast else data
        self.type = type
        self.pos = (start, end)
        self.start = start
        self.end = end

    def val(self):
        return self.value
    
    def __repr__(self):
        return '%s(%s)' % (self.type.__name__, repr(self.data))

class TSeq(list):
    """
    This is meant to be returned by XNode's instances
    that extract strings from a given doc sequentially.
    """

class TokType:
    @classmethod
    def validate(cls, slc):
        tok = slc.get()
        if tok and cls.istype(tok):
            return tok

    @classmethod
    def istype(cls, tok):
        return tok.type is cls

class TokVal:
    def __init__(self, data):
        self.data = data
        self.type = TokVal

    def validate(self, slc):
        tok = slc.get()
        if tok and self.istype(tok):
            return tok

    def istype(self, tok):
        return self.data == tok.data

    def __repr__(self):
        return 'TokVal(%s)' % repr(self.data)

class Eof(TokType):
    pass

class Sof(TokType):
    pass

class Num(TokType):
    pass

class Plus(TokType):
    pass

class Minus(TokType):
    pass

class Div(TokType):
    pass

class Mul(TokType):
    pass

class RP(TokType):
    pass

class LP(TokType):
    pass

class Blank(TokType):
    pass

class Keyword(TokType):
    pass

class Identifier(TokType):
    pass

class Colon(TokType):
    pass

class DoubleQuote(TokType):
    pass

class Quote(TokType):
    pass

class Comma(TokType):
    pass

class LB(TokType):
    pass

class RB(TokType):
    pass

class LSB(TokType):
    pass

class RSB(TokType):
    pass

class Word(TokType):
    pass

class UnkToken(TokType):
    pass

class Greater(TokType):
    pass

class Lesser(TokType):
    pass

class Question(TokType):
    pass

class BackSlash(TokType):
    pass

class Period(TokType):
    pass

class Char(TokType):
    pass