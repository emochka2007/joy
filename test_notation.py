from index import polish_notation, match_brackets, tokenizer

assert(polish_notation(match_brackets(tokenizer("4 2 -")))== [2])
assert(polish_notation(match_brackets(tokenizer("[1 2 3] first"))) == [1])
assert(polish_notation(match_brackets(tokenizer("[1 2 3] rest"))) == [[2, 3]])
assert((polish_notation(match_brackets(tokenizer("42 [1 2 3] cons")))) == [[42, 1, 2, 3]])
assert(polish_notation(match_brackets(tokenizer("[1 2 3] dup first swap rest cons"))) == [[1, 2, 3]])
assert(polish_notation(match_brackets(tokenizer("2 3 == [1 2 +] [2 3 *]  if"))) == [6])
assert(polish_notation(match_brackets(tokenizer("[sq dup *] def 3 sq 1 +"))) == [10])
assert(polish_notation(match_brackets(tokenizer("[fact dup  1 == [][dup 1 - fact *] if] def 5 fact")))== [120])



assert(polish_notation(match_brackets(tokenizer("2 3 4 rot"))) == [4, 2, 3])
assert(polish_notation(match_brackets(tokenizer("[to_power dup 1 == [*][swap dup rot swap 1 - to_power *] if] def 10 2 to_power"))) == [100])
assert(polish_notation(match_brackets(tokenizer("[to_power dup 1 == [*][swap dup rot swap 1 - to_power *] if] def 4 4 to_power"))) == [256])

assert(polish_notation(match_brackets(tokenizer("[len dup null [drop 0][rest len 1 +] if] def [] len"))) == [0]) #0
assert(polish_notation(match_brackets(tokenizer("[only_one dup null [False] [rest null] if] def [312] only_one"))) == [True])
#Support multiline & comments
assert(polish_notation(match_brackets(tokenizer("# comment \n 4 2 -\n4 2 -"))) == [2,2])
assert(polish_notation(match_brackets(tokenizer("[last dup rest null [first][rest last] if] def [1 2 3] last"))) == [3])
"""
[uncons dup first swap rest] def
[pop dup rest null [rest][uncons pop cons] if] def [1 2 3 4] pop
"""

#15
[sum dup rest null [first][uncons sum +] if] def [1 2 3 4 5] sum 