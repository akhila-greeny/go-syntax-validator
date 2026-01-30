"""
Go Language Syntax Validator (using PLY)
----------------------------------------
Supported Constructs:
1. Variable Declaration
2. Constant Declaration
3. Assignment
4. Increment / Decrement
5. If-Else Statement
6. For Loop
7. Function Definition
8. Struct Definition
"""

import ply.yacc as yacc
from lexer import tokens

used_constructs = set()
help_text = __doc__

# --------------------
# Syntax List (user command)
# --------------------
syntax_list = """
VALID SYNTAX RULES
------------------

1. Variable Declaration
   var x = 10
   var y int = 20

2. Constant Declaration
   const PI = 3.14

3. Assignment
   x = 5

4. Increment / Decrement
   x++
   x--

5. If Statement
   if x < 10 {
       x = x + 1
   }

6. If-Else Statement
   if x > 0 {
       x = x - 1
   } else {
       x = 0
   }

7. For Loop (Classic)
   for i := 0; i < 10; i++ {
       x = x + i
   }

8. For Loop (Condition Only)
   for x < 10 {
       x = x + 1
   }

9. Function Definition
   func add(a int, b int) int {
       return a + b
   }

10. Struct Definition
    type Person struct {
        name string;
        age int
    }

11. Return Statement
    return x
"""

# --------------------
# Operator precedence
# --------------------
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# --------------------
# Statements
# --------------------
def p_statement(p):
    '''statement : var_declaration
                 | const_declaration
                 | assignment
                 | increment
                 | ifelse
                 | forloop
                 | function
                 | struct
                 | return_stmt'''
    pass

# --------------------
# Variable Declaration
# --------------------
def p_var_declaration(p):
    '''var_declaration : VAR ID type ASSIGN expression
                       | VAR ID ASSIGN expression'''
    print("Valid variable declaration")
    used_constructs.add("Variable Declaration")

# --------------------
# Constant Declaration
# --------------------
def p_const_declaration(p):
    'const_declaration : CONST ID ASSIGN expression'
    print("Valid constant declaration")
    used_constructs.add("Constant Declaration")

# --------------------
# Assignment
# --------------------
def p_assignment(p):
    'assignment : ID ASSIGN expression'
    print("Valid assignment")
    used_constructs.add("Assignment")

# --------------------
# Increment / Decrement
# --------------------
def p_increment(p):
    '''increment : ID PLUS PLUS
                 | ID MINUS MINUS'''
    print("Valid increment/decrement")
    used_constructs.add("Increment/Decrement")

# --------------------
# If / Else
# --------------------
def p_ifelse(p):
    '''ifelse : IF condition block
              | IF condition block ELSE block'''
    print("Valid if/else statement")
    used_constructs.add("If-Else Statement")

# --------------------
# For Loop
# --------------------
def p_forloop(p):
    '''forloop : FOR ID DECLARE expression SEMI condition SEMI ID PLUS PLUS block
               | FOR condition block'''
    print("Valid for loop")
    used_constructs.add("For Loop")

# --------------------
# Function Definition
# --------------------
def p_function(p):
    'function : FUNC ID LPAREN paramlist RPAREN type block'
    print("Valid function definition")
    used_constructs.add("Function Definition")

def p_paramlist(p):
    '''paramlist : ID type
                 | ID type COMMA paramlist
                 | empty'''
    pass

# --------------------
# Struct Definition
# --------------------
def p_struct(p):
    'struct : TYPE ID STRUCT LBRACE fields RBRACE'
    print("Valid struct definition")
    used_constructs.add("Struct Definition")

def p_fields(p):
    '''fields : ID type
              | ID type SEMI fields
              | empty'''
    pass

# --------------------
# Return
# --------------------
def p_return_stmt(p):
    'return_stmt : RETURN expression'
    print("Valid return statement")
    used_constructs.add("Return Statement")

# --------------------
# Condition
# --------------------
def p_condition(p):
    '''condition : expression LT expression
                 | expression GT expression
                 | expression EQ expression
                 | expression GE expression
                 | expression LE expression
                 | expression NE expression'''
    pass

# --------------------
# Block
# --------------------
def p_block(p):
    'block : LBRACE inner_statements RBRACE'
    pass

def p_inner_statements(p):
    '''inner_statements : statement
                        | statement inner_statements
                        | empty'''
    pass

# --------------------
# Types
# --------------------
def p_type(p):
    '''type : INTTYPE
            | STRINGTYPE'''
    pass

# --------------------
# Expressions
# --------------------
def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    pass

def p_empty(p):
    'empty :'
    pass

# --------------------
# Error Handling
# --------------------
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# --------------------
# Interactive Mode
# --------------------
print("Go Language Syntax Validator (Interactive)\n")
print("Type 'help' or 'show' to see features.")
print("Type 'syntax' or 'list' to see valid syntax.")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    try:
        s = input("Enter Go code: ").strip()
    except EOFError:
        break

    if not s:
        continue

    cmd = s.lower()

    if cmd in ("exit", "quit"):
        print("\nExiting program...")
        print("\nConstructs used in this session:")
        if used_constructs:
            for c in used_constructs:
                print(f"   • {c}")
        else:
            print("   (No valid constructs detected)")
        break

    elif cmd in ("help", "show"):
        print(help_text)
        continue

    elif cmd in ("syntax", "list", "rules"):
        print(syntax_list)
        continue

    parser.parse(s)