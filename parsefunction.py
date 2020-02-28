'''
-> CONTEXT-FREE GRAMMAR <-
expr     --> expr PLUS term      |  expr MINUS term    |  term
term     --> term TIMES factor   |  term DIVIDE factor |  factor
factor   --> exponent POW factor |  exponent
exponent --> MINUS exponent      |  final
final    --> DIGIT               |  ( expr )
'''

class Expression:

    def __init__(self):
        raise NotImplementedError()

    def Evaluate(self):
        raise NotImplementedError()

    def __repr__(self):
        klass = self.__class__.__name__
        private = '_{0}__'.format(klass)
        args = []
        for name in self.__dict__:
            if name.startswith(private):
                value = self.__dict__[name]
                name = name[len(private):]
                args.append('{0}={1}'.format(name, repr(value)))
        return '{0}({1})'.format(klass, ', '.join(args))


class Constant(Expression):

    def __init__(self, value):
        self.__value = value

    def Evaluate(self):
        return self.__value

class Operation(Expression):

    def __init__(self, operation, left, right):
        self.__op = operation
        self.__left = left
        self.__right = right

    def Evaluate(self):
        x = self.__left.Evaluate()
        y = self.__right.Evaluate()

        if self.__op == '+':
            return x + y
        if self.__op == '-':
            return x - y
        if self.__op == '*':
            return x * y
        if self.__op == '/':
            return x / y
        if self.__op == '^':
            return pow(x, y)
        raise Exception('Unknown operator: ' + self.__op)

class Parser:

    def parse(self, tokens):
        self.tokens = tokens
        self.nextToken()
        return self.expr()

    def nextToken(self):
        if len(self.tokens):
            # remove first element from token list\
            self.current = self.tokens.pop(0)
        else:
            self.current = None

    def expr(self):
        result = self.term()
        while self.current in ('+', '-'):
            if self.current == '+':
                self.nextToken()
                a = result
                b = self.term()
                result = Operation('+', a, b)
            if self.current == '-':
                self.nextToken()
                minuend = result
                subtrahend = self.term()
                result = Operation('-', minuend, subtrahend)
        return result

    def term(self):
        result = self.factor()
        while self.current in ('*', '/'):
            if self.current == '*':
                self.nextToken()
                factor = result
                multiplier = self.term()
                result = Operation('*', factor, multiplier)
            if self.current == '/':
                self.nextToken()
                dividend = result
                divisor = self.term()
                result = Operation('/', dividend, divisor)
        return result

    def factor(self):
        result = self.exponent()
        while self.current == '^':
            self.nextToken()
            base = result
            exp = self.factor()
            result = Operation('^', base, exp)
        return result

    def exponent(self):
        if self.current == '-':
            self.nextToken()
            positive = self.final()
            result = Constant(-positive.Evaluate())
        else:
            result = self.final()
        return result

    def final(self):
        result = None
        if type(self.current) is float:
            result = Constant(self.current)
            self.nextToken()
        elif self.current == '(':
            self.nextToken()
            result = self.expr()
            if self.current != ')':
                raise Exception('Expected )')
            self.nextToken()
        else:
            raise Exception('Expected number or (expr)')
        return result

class MathExp:

    SYMBOLS = ['+', '-', '*', '/', '^', '(', ')']

    def __init__(self):
        self.parser = Parser()

    def eval(self, string):
        chars = list(string)
        tokens = self.tokenizer(chars)
        if not tokens:
            # not parse if empty
            return None
        tree = self.parser.parse(tokens)
        # print(tree)   # uncomment to see parser results
        return tree.Evaluate()

    def tokenizer(self, chars):
        tokens = []
        pos = 0
        while pos < len(chars):
            c = chars[pos]

            if c == ' ':
                # do nothing...
                pass
            elif c in self.SYMBOLS:
                tokens.append(c)
            elif c.isdigit():
                num = float(c);
                # read the entire number before append
                while pos + 1 < len(chars) and chars[pos + 1].isdigit():
                    pos += 1
                    num = num * 10 + float(chars[pos])
                tokens.append(num)
            else:
                raise Exception('Unknown symbol at position: ' + str(pos))

            pos += 1
        return tokens