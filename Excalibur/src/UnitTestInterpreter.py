#!/usr/bin/python
import unittest

class TestInterpreter(unittest.TestCase):
    def makeInterpreter(self,text):
        from interpreter import Lexer,Interpreter
        lexer = Lexer(text)
        return Interpreter(lexer)

    def testExpressions(self):
        interpreter = self.makeInterpreter('2 + 3*4*2 + 12')
        result = interpreter.expr()
        self.assertEqual(result,38)

        interpreter = self.makeInterpreter('2 + 3*4*2 + 12/2')
        result = interpreter.expr()
        self.assertEqual(result,32)

        interpreter = self.makeInterpreter('7 + 3*(10/(12/(3+1)-1))')
        result = interpreter.expr()
        self.assertEqual(result,22)

        interpreter = self.makeInterpreter('7+3*(10/(12/(3+1)-1))/(2+3)-5-3+(8)')
        result = interpreter.expr()
        self.assertEqual(result,10)

        interpreter = self.makeInterpreter('7 + (((3+2)))')
        result = interpreter.expr()
        self.assertEqual(result,12)

        interpreter = self.makeInterpreter('(21 + ((2*3)))')
        result = interpreter.expr()
        self.assertEqual(result,27)

if __name__ == '__main__':
     unittest.main()
