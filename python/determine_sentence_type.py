# https://rosettacode.org/wiki/Determine_sentence_type

import re

def breaklines(sentences: str) -> list[str]:
    sign_map = {
        '?': 'Q',
        '!': 'E',
        '.': 'S'
    }

    items = list(map(str.strip, re.split('([?!.])', sentences)))
    for i, item in enumerate(items):
        if i != len(items) - 1:
            if items[i + 1] in '?.!':
                yield f"{item} ==> {sign_map[items[i + 1]]}"
        elif item != '?.!':
            yield f'{item} ==> N'

def main():
    text = "hi there, how are you today? I'd like to present to you the washing machine 9001. You have been nominated to win one of these! Just make sure you don't break it"
    print(*breaklines(text), sep='\n')

if __name__ == '__main__':
    main()
