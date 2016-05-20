#ifndef _Excalibur_Interpreter
#define _Excalibur_Interpreter

#include <string>
using namespace std;

class Interpreter {
    public:
        Interpreter(Lexer lexer);
        ~Interpreter();
};

class Token {
    public:
        Token(string str);
        ~Token();
};

class Lexer {
    public:
        Lexer(string str);
        ~Lexer();
};

#endif
