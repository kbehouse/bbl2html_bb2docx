# LaTeX accents replacement
latexAccents = [
  [ u"à", "\\`a" ], # Grave accent
  [ u"è", "\\`e" ],
  [ u"ì", "\\`\\i" ],
  [ u"ò", "\\`o" ],
  [ u"ù", "\\`u" ],
  [ u"ỳ", "\\`y" ],
  [ u"À", "\\`A" ],
  [ u"È", "\\`E" ],
  [ u"Ì", "\\`\\I" ],
  [ u"Ò", "\\`O" ],
  [ u"Ù", "\\`U" ],
  [ u"Ỳ", "\\`Y" ],
  [ u"á", "\\'a" ], # Acute accent
  [ u"é", "\\'e" ],
  [ u"í", "\\'\\i" ],
  [ u"ó", "\\'o" ],
  [ u"ú", "\\'u" ],
  [ u"ý", "\\'y" ],
  [ u"Á", "\\'A" ],
  [ u"É", "\\'E" ],
  [ u"Í", "\\'\\I" ],
  [ u"Ó", "\\'O" ],
  [ u"Ú", "\\'U" ],
  [ u"Ý", "\\'Y" ],
  [ u"â", "\\^a" ], # Circumflex
  [ u"ê", "\\^e" ],
  [ u"î", "\\^\\i" ],
  [ u"ô", "\\^o" ],
  [ u"û", "\\^u" ],
  [ u"ŷ", "\\^y" ],
  [ u"Â", "\\^A" ],
  [ u"Ê", "\\^E" ],
  [ u"Î", "\\^\\I" ],
  [ u"Ô", "\\^O" ],
  [ u"Û", "\\^U" ],
  [ u"Ŷ", "\\^Y" ],
  [ u"ä", "\\\"a" ],    # Umlaut or dieresis
  [ u"ë", "\\\"e" ],
  [ u"ï", "\\\"\\i" ],
  [ u"ö", "\\\"o" ],
  [ u"ü", "\\\"u" ],
  [ u"ÿ", "\\\"y" ],
  [ u"Ä", "\\\"A" ],
  [ u"Ë", "\\\"E" ],
  [ u"Ï", "\\\"\\I" ],
  [ u"Ö", "\\\"O" ],
  [ u"Ü", "\\\"U" ],
  [ u"Ÿ", "\\\"Y" ],
  [ u"ç", "\\c{c}" ],   # Cedilla
  [ u"Ç", "\\c{C}" ],
  [ u"œ", "{\\oe}" ],   # Ligatures
  [ u"Œ", "{\\OE}" ],
  [ u"æ", "{\\ae}" ],
  [ u"Æ", "{\\AE}" ],
  [ u"å", "{\\aa}" ],
  [ u"Å", "{\\AA}" ],
  [ u"–", "--" ],   # Dashes
  [ u"—", "---" ],
  [ u"ø", "{\\o}" ],    # Misc latin-1 letters
  [ u"Ø", "{\\O}" ],
  [ u"ß", "{\\ss}" ],
  [ u"¡", "{!`}" ],
  [ u"¿", "{?`}" ],
  [ u"\\", "\\\\" ],    # Characters that should be quoted
  [ u"~", "\\~" ],
  [ u"&", "\\&" ],
  [ u"$", "\\$" ],
  [ u"{", "\\{" ],
  [ u"}", "\\}" ],
  [ u"%", "\\%" ],
  [ u"#", "\\#" ],
  [ u"_", "\\_" ],
  [ u"≥", "$\\ge$" ],   # Math operators
  [ u"≤", "$\\le$" ],
  [ u"≠", "$\\neq$" ],
  [ u"©", "\copyright" ], # Misc
  [ u"ı", "{\\i}" ],
  [ u"µ", "$\\mu$" ],
  [ u"°", "$\\deg$" ],
  [ u"‘", "`" ],    #Quotes
  [ u"’", "'" ],
  [ u"“", "``" ],
  [ u"”", "''" ],
  [ u"‚", "," ],
  [ u"„", ",," ],
]

def replace_utf8(s):
    for l in latexAccents:
        s = s.replace(l[1],l[0])

    return s