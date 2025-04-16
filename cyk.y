%{
#include <stdio.h>
#include <stdlib.h>
int yylex(void);
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
%}

%start S

%%

S : B A B A   { printf("Cadena reconocida por la gramática.\n"); }
  | B A A     { printf("Cadena reconocida por la gramática.\n"); }
  ;

A : 'a' ;
B : 'b' ;

%%

