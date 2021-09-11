
def json_formatter(json_string: str, indentor: str = '  ') -> str:
    res = ''
    indent_level = 0
    temp = ''
    for i, char in enumerate(json_string):
        if char in '{[':
            res += indentor * indent_level + temp.strip() + char + '\n'
            indent_level += 1
            temp = ''
        elif char in '}]':
            res += indentor * indent_level + temp.strip() + '\n' + indentor * (indent_level - 1) + char
            indent_level -= 1
            temp = ''
        elif char in ',':
            res += indentor * (0 if json_string[i - 1] in '{}[]' else indent_level) + temp.strip() + char + '\n'
            temp = ''
        else:
            temp += char
    return res


def get_formatted_message(source) -> str:
    return '<code>' + json_formatter(str(source)) + '</code>'

