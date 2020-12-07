"""
Searches for weasel words in a text file.
Usage: python weasel_words.py (myfile.tex)
Inspired by Matt Might
"""

import sys

weasels="many|various|very|fairly|several|extremely\
|exceedingly|quite|remarkably|few|surprisingly\
|note that|notice that\
|mostly|largely|huge|tiny|are a number|is a number\
|excellent|interestingly|significantly\
|substantially|clearly|vast|relatively|completely".split('|')


weasels = weasels + [x.capitalize() for x in weasels]

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please execute by specifying a file name as \
              python weasel_words.py (myfile.tex)")
        sys.exit(0)
    
    with open(filename) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        possible_violations = 0
        for idx, line in enumerate(content):
            needtofix = False
            for w in weasels:
                if w in line:
                    possible_violations = possible_violations+1
                    needtofix = True
                    line = line.replace(w, '***'+w.upper()+'***')
            if needtofix:
                print('Line: '+str(idx+2))
                print( line)
                print('\n')
    print(str(possible_violations) + " possible violations found.")
