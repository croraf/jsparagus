import pgen_runtime

actions = [
    {'nt': 1, 'goal': 2},
    {'IDENT': 5},
    {'nt': 6},
    {'nt': 1, 'goal': 2, None: -9223372036854775807},
    {None: -1, 'nt': -1, 'goal': -1},
    {'{': 8},
    {'IDENT': 9},
    {None: -2, 'nt': -2, 'goal': -2},
    {'}': 10, 'IDENT': 11, 'STR': 12},
    {'{': 18},
    {None: -3, 'nt': -3, 'goal': -3},
    {';': -14, '?': -14, 'IDENT': -14, 'STR': -14},
    {';': -15, '?': -15, 'IDENT': -15, 'STR': -15},
    {'}': 19, 'IDENT': 11, 'STR': 12},
    {'}': -7, 'IDENT': -7, 'STR': -7},
    {';': 21, 'IDENT': 22, 'STR': 23},
    {';': -10, 'IDENT': -10, 'STR': -10},
    {'?': 25, ';': -12, 'IDENT': -12, 'STR': -12},
    {'}': 26, 'IDENT': 11, 'STR': 12},
    {None: -4, 'nt': -4, 'goal': -4},
    {'}': -8, 'IDENT': -8, 'STR': -8},
    {'}': -9, 'IDENT': -9, 'STR': -9},
    {';': -14, 'IDENT': -14, 'STR': -14, '?': -14},
    {';': -15, 'IDENT': -15, 'STR': -15, '?': -15},
    {';': -11, 'IDENT': -11, 'STR': -11},
    {';': -13, 'IDENT': -13, 'STR': -13},
    {None: -5, 'nt': -5, 'goal': -5},
    {'}': 28, 'IDENT': 11, 'STR': 12},
    {None: -6, 'nt': -6, 'goal': -6},
]

ctns = [
    {'grammar': 3, 'nt_def': 4},
    {},
    {},
    {'nt_def': 7},
    {},
    {},
    {},
    {},
    {'prods': 13, 'prod': 14, 'terms': 15, 'term': 16, 'symbol': 17},
    {},
    {},
    {},
    {},
    {'prod': 20, 'terms': 15, 'term': 16, 'symbol': 17},
    {},
    {'term': 24, 'symbol': 17},
    {},
    {},
    {'prods': 27, 'prod': 14, 'terms': 15, 'term': 16, 'symbol': 17},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {'prod': 20, 'terms': 15, 'term': 16, 'symbol': 17},
    {},
]

reductions = [
    ('grammar', 1, lambda x0: ('grammar', 0, [x0])),
    ('grammar', 2, lambda x0, x1: ('grammar', 1, [x0, x1])),
    ('nt_def', 4, lambda x0, x1, x2, x3: ('nt_def', 0, [x0, x1, x2, None, x3])),
    ('nt_def', 5, lambda x0, x1, x2, x3, x4: ('nt_def', 0, [x0, x1, x2, x3, x4])),
    ('nt_def', 5, lambda x0, x1, x2, x3, x4: ('nt_def', 1, [x0, x1, x2, x3, None, x4])),
    ('nt_def', 6, lambda x0, x1, x2, x3, x4, x5: ('nt_def', 1, [x0, x1, x2, x3, x4, x5])),
    ('prods', 1, lambda x0: ('prods', 0, [x0])),
    ('prods', 2, lambda x0, x1: ('prods', 1, [x0, x1])),
    ('prod', 2, lambda x0, x1: ('prod', 0, [x0, x1])),
    ('terms', 1, lambda x0: ('terms', 0, [x0])),
    ('terms', 2, lambda x0, x1: ('terms', 1, [x0, x1])),
    ('term', 1, lambda x0: ('term', 0, [x0])),
    ('term', 2, lambda x0, x1: ('term', 1, [x0, x1])),
    ('symbol', 1, lambda x0: ('symbol', 0, [x0])),
    ('symbol', 1, lambda x0: ('symbol', 1, [x0])),
    ('grammar_1', 1, lambda x0: ('grammar_1', 0, [x0])),
]

parse_grammar = pgen_runtime.make_parse_fn(actions, ctns, reductions, 0)
