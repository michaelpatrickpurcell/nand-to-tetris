keywords = {
    'CLASS',
    'METHOD',
    'FUNCTION',
    'CONSTRUCTOR',
    'INT',
    'BOOLEAN',
    'CHAR',
    'VOID',
    'VAR',
    'STATIC',
    'FIELD',
    'LET',
    'DO',
    'IF',
    'ELSE',
    'WHILE',
    'RETURN',
    'TRUE',
    'FALSE',
    'NULL',
    'THIS',
}

token_types = {
    'KEYWORD',
    'SYMBOL',
    'IDENTIFIER',
    'INT_CONST',
    'STRING_CONST',
}

class Tokenizer:
    def __init__(self, infile):
        with (open(infile,'r')) as f:
            ifstring = f.read()
        uncommented_string = self.remove_comments(ifstring)
        stripped_string = self.strip_whitespace(uncommented_string)
        self.tokens = self.split_tokens(stripped_string)


    #         for line in f:
    #             temp = self.strip_whitespace(line)
    #             if temp:
    #                 self.lines.append(line)

    def remove_comments(self, s):
        characters = []
        line_comment = False
        block_comment = False
        api_comment = False
        for i,c in enumerate(s):
            if s[i:i+3] == '/**':
                api_comment = True
            elif s[i:i+2] == '/*':
                block_comment = True
            elif s[i:i+2] == '//':
                line_comment = True
            if not (line_comment or block_comment or api_comment):
                characters .append(c)
            if (s[i-1:i+1] == '*/') and (block_comment or api_comment):
                block_comment = False
                api_comment = False
            elif (s[i] == '\n') and line_comment:
                line_comment = False
        return ''.join(characters)

    def strip_whitespace(self, s):
        lines = s.split('\n')
        stripped_lines = []
        for line in lines:
            temp = line.strip()
            if temp:
                stripped_lines.append(temp)
        stripped_string = ' '.join(stripped_lines)
        return stripped_string

    def split_tokens(self, s):
        temp = []
        for c in s:
            if c in {'(', ')', ';', '[', ']'}:
                temp.append(f' {c} ')
            else:
                temp.append(c)
        foo = ''.join(temp)
        tokens = foo.split()
        return tokens

if __name__ == '__main__':
    print('Starting tokenizer')
    tokenizer = Tokenizer('projects/10/ArrayTest/Main.jack')
    # print(tokenizer.ucifstring)
    print(' '.join(tokenizer.tokens))
