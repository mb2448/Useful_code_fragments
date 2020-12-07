Scripts to search for writing errors.
Work best with .tex files.

"weasel words" and "passive voice" were inspired by Matt Might's blog post:
http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/

"repeated_words" searches for egregiously similar repeated words in paragraphs.
Edit the parameters (how many repititions, minimum word length) in the script for now.

Usage:

python weasel_words.py (myfile.tex)

python passive_voice.py (myfile.tex)

python repeated_words.py (myfile.tex)
