"""
Searches for passive voice in a text file.
Usage: python passive_voice.py (myfile.tex)
Inspired by Matt Might
"""

import sys
import string

irregulars = "awoken|\
been|born|beat|\
become|begun|bent|\
beset|bet|bid|\
bidden|bound|bitten|\
bled|blown|broken|\
bred|brought|broadcast|\
built|burnt|burst|\
bought|cast|caught|\
chosen|clung|come|\
cost|crept|cut|\
dealt|dug|dived|\
done|drawn|dreamt|\
driven|drunk|eaten|fallen|\
fed|felt|fought|found|\
fit|fled|flung|flown|\
forbidden|forgotten|\
foregone|forgiven|\
forsaken|frozen|\
gotten|given|gone|\
ground|grown|hung|\
heard|hidden|hit|\
held|hurt|kept|knelt|\
knit|known|laid|led|\
leapt|learnt|left|\
lent|let|lain|lighted|\
lost|made|meant|met|\
misspelt|mistaken|mown|\
overcome|overdone|overtaken|\
overthrown|paid|pled|proven|\
put|quit|read|rid|ridden|\
rung|risen|run|sawn|said|\
seen|sought|sold|sent|\
set|sewn|shaken|shaven|\
shorn|shed|shone|shod|\
shot|shown|shrunk|shut|\
sung|sunk|sat|slept|\
slain|slid|slung|slit|\
smitten|sown|spoken|sped|\
spent|spilt|spun|spit|\
split|spread|sprung|stood|\
stolen|stuck|stung|stunk|\
stridden|struck|strung|\
striven|sworn|swept|\
swollen|swum|swung|taken|\
taught|torn|told|thought|\
thrived|thrown|thrust|\
trodden|understood|upheld|\
upset|woken|worn|woven|\
wed|wept|wound|won|\
withheld|withstood|wrung|\
written".split("|")

pre_words = "am|are|were|being|is|been|was|be".split('|')

passives = [p+' '+i for i in irregulars for p in pre_words]      

def find_substring(needle, haystack):
    """determines string1 is in string2 but ends with a 
    word continuation character like space"""
    index = haystack.find(needle)
    if index == -1:
        return False
    if index != 0 and haystack[index-1] not in string.whitespace:
        return False
    L = index + len(needle)
    if L < len(haystack) and haystack[L] not in string.whitespace:
        return False
    return True

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please execute by specifying a file name as \
              python passive_voice.py (myfile.tex)")
        sys.exit(0)
    
    with open(filename) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        possible_violations = 0
        for idx, line in enumerate(content):
            needtofix = False
            for w in passives:
                if find_substring(w, line):
                    needtofix = True
                    possible_violations = possible_violations+1
                    line = line.replace(w, '***'+w.upper()+'***')
                    if needtofix:
                        print('Line: '+str(idx+2))
                        print( line)
                        print('\n')
    print(str(possible_violations) + " possible violations found.")
