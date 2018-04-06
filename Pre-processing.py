#load data
data_file='1.txt'
f= open(data_file, 'rt')
text = f.read()
#apply Preprocessing
wd = text.split()
print(wd)
import string
tbl = str.maketras('', '', string.punctuation)
print(tbl)
import re
wd= re.split(r'\W+', text)
wd = text.split()
wd = [w.lower() for w in wd]
print(wd)
doc=nlp(text)
for en in doc.ents:
    print(en.text,en.start_char,en.end_char,en.label_) 


