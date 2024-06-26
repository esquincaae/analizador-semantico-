
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN CHAR ELSE EQUAL FLOAT FOR FUNC IDENTIFIER IF INT LBRACKET LPAREN OPERATOR PM PRINT RBRACKET RPAREN SEMICOLON STRING TYPE VARstart : structuresstructures : structures structure\n                  | structurestructure : var_decl\n                 | func_decl\n                 | for_decl\n                 | if_decl\n                 | statementvar_decl : VAR TYPE IDENTIFIER EQUAL value SEMICOLONfunc_decl : FUNC IDENTIFIER LPAREN RPAREN LBRACKET statements RBRACKETfor_decl : FOR LPAREN var_decl condition SEMICOLON increment RPAREN LBRACKET statements RBRACKETif_decl : IF LPAREN condition RPAREN LBRACKET statements RBRACKET else_declelse_decl : ELSE LBRACKET statements RBRACKETstatements : statements statement\n                  | statementstatement : PRINT LPAREN STRING RPAREN SEMICOLON\n                 | PRINT LPAREN IDENTIFIER RPAREN SEMICOLONvalue : INT\n             | FLOAT\n             | BOOLEAN\n             | STRING\n             | CHARcondition : IDENTIFIER OPERATOR value\n                 | IDENTIFIER OPERATOR IDENTIFIERincrement : IDENTIFIER PM'
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,7,8,14,17,45,46,47,53,59,63,65,],[9,9,-3,-4,-5,-6,-7,-8,-2,9,-16,-17,-9,-10,-12,-11,-13,]),'FUNC':([0,2,3,4,5,6,7,8,14,45,46,47,53,59,63,65,],[10,10,-3,-4,-5,-6,-7,-8,-2,-16,-17,-9,-10,-12,-11,-13,]),'FOR':([0,2,3,4,5,6,7,8,14,45,46,47,53,59,63,65,],[11,11,-3,-4,-5,-6,-7,-8,-2,-16,-17,-9,-10,-12,-11,-13,]),'IF':([0,2,3,4,5,6,7,8,14,45,46,47,53,59,63,65,],[12,12,-3,-4,-5,-6,-7,-8,-2,-16,-17,-9,-10,-12,-11,-13,]),'PRINT':([0,2,3,4,5,6,7,8,14,40,42,45,46,47,48,49,52,53,54,58,59,61,62,63,64,65,],[13,13,-3,-4,-5,-6,-7,-8,-2,13,13,-16,-17,-9,13,-15,13,-10,-14,13,-12,13,13,-11,13,-13,]),'$end':([1,2,3,4,5,6,7,8,14,45,46,47,53,59,63,65,],[0,-1,-3,-4,-5,-6,-7,-8,-2,-16,-17,-9,-10,-12,-11,-13,]),'TYPE':([9,],[15,]),'IDENTIFIER':([10,15,18,19,22,31,41,47,],[16,20,24,26,24,43,51,-9,]),'LPAREN':([11,12,13,16,],[17,18,19,21,]),'STRING':([19,27,31,],[25,38,38,]),'EQUAL':([20,],[27,]),'RPAREN':([21,23,25,26,35,36,37,38,39,43,44,50,56,],[28,30,32,33,-18,-19,-20,-21,-22,-24,-23,55,-25,]),'OPERATOR':([24,],[31,]),'INT':([27,31,],[35,35,]),'FLOAT':([27,31,],[36,36,]),'BOOLEAN':([27,31,],[37,37,]),'CHAR':([27,31,],[39,39,]),'LBRACKET':([28,30,55,60,],[40,42,58,62,]),'SEMICOLON':([29,32,33,34,35,36,37,38,39,43,44,],[41,45,46,47,-18,-19,-20,-21,-22,-24,-23,]),'RBRACKET':([45,46,48,49,52,54,61,64,],[-16,-17,53,-15,57,-14,63,65,]),'PM':([51,],[56,]),'ELSE':([57,],[60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'structures':([0,],[2,]),'structure':([0,2,],[3,14,]),'var_decl':([0,2,17,],[4,4,22,]),'func_decl':([0,2,],[5,5,]),'for_decl':([0,2,],[6,6,]),'if_decl':([0,2,],[7,7,]),'statement':([0,2,40,42,48,52,58,61,62,64,],[8,8,49,49,54,54,49,54,49,54,]),'condition':([18,22,],[23,29,]),'value':([27,31,],[34,44,]),'statements':([40,42,58,62,],[48,52,61,64,]),'increment':([41,],[50,]),'else_decl':([57,],[59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> structures','start',1,'p_start','lyra_parser.py',7),
  ('structures -> structures structure','structures',2,'p_structures','lyra_parser.py',12),
  ('structures -> structure','structures',1,'p_structures','lyra_parser.py',13),
  ('structure -> var_decl','structure',1,'p_structure','lyra_parser.py',21),
  ('structure -> func_decl','structure',1,'p_structure','lyra_parser.py',22),
  ('structure -> for_decl','structure',1,'p_structure','lyra_parser.py',23),
  ('structure -> if_decl','structure',1,'p_structure','lyra_parser.py',24),
  ('structure -> statement','structure',1,'p_structure','lyra_parser.py',25),
  ('var_decl -> VAR TYPE IDENTIFIER EQUAL value SEMICOLON','var_decl',6,'p_var_decl','lyra_parser.py',30),
  ('func_decl -> FUNC IDENTIFIER LPAREN RPAREN LBRACKET statements RBRACKET','func_decl',7,'p_func_decl','lyra_parser.py',36),
  ('for_decl -> FOR LPAREN var_decl condition SEMICOLON increment RPAREN LBRACKET statements RBRACKET','for_decl',10,'p_for_decl','lyra_parser.py',41),
  ('if_decl -> IF LPAREN condition RPAREN LBRACKET statements RBRACKET else_decl','if_decl',8,'p_if_decl','lyra_parser.py',46),
  ('else_decl -> ELSE LBRACKET statements RBRACKET','else_decl',4,'p_else_decl','lyra_parser.py',50),
  ('statements -> statements statement','statements',2,'p_statements','lyra_parser.py',55),
  ('statements -> statement','statements',1,'p_statements','lyra_parser.py',56),
  ('statement -> PRINT LPAREN STRING RPAREN SEMICOLON','statement',5,'p_statement_print','lyra_parser.py',63),
  ('statement -> PRINT LPAREN IDENTIFIER RPAREN SEMICOLON','statement',5,'p_statement_print','lyra_parser.py',64),
  ('value -> INT','value',1,'p_value','lyra_parser.py',69),
  ('value -> FLOAT','value',1,'p_value','lyra_parser.py',70),
  ('value -> BOOLEAN','value',1,'p_value','lyra_parser.py',71),
  ('value -> STRING','value',1,'p_value','lyra_parser.py',72),
  ('value -> CHAR','value',1,'p_value','lyra_parser.py',73),
  ('condition -> IDENTIFIER OPERATOR value','condition',3,'p_condition','lyra_parser.py',78),
  ('condition -> IDENTIFIER OPERATOR IDENTIFIER','condition',3,'p_condition','lyra_parser.py',79),
  ('increment -> IDENTIFIER PM','increment',2,'p_increment','lyra_parser.py',84),
]
