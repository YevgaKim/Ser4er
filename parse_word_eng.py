import glob
import re

from docx import Document

document = Document(glob.glob("data\\doc\\*.docx")[0])



df_tables = []
for table in document.tables:
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            if cell.text:
                df[i][j] = cell.text
    


for i in df:
    if "\n" in i[-1]:
        i[-1] = re.sub(r"\n","",i[-1])
    if i[-1]=="" and not re.search(r"/\W*\S*/",i[1]) and not "adj" in i[1]:
        continue    
    eng = i[1].split("\n")
    if len(eng)!=1:
        eng.pop()
    word=""
    for j in eng:
        word+=j
    if "," in word and not re.search(r"\d\)",word):
        word = word.split(",")
    elif " adj" in word:
        word = word.split("adj")
        if "," in word[0]:
            word[0]=re.sub(r",","",word[0])
    else:
        word=[word]

    answer=""
    if len(word)==2:
        answer=word[0].strip()
    elif len(word)>=3:
        answer=f"{word[0].strip()}, {word[1].split('=')[-1].strip()}"
    else:
        if re.search(r"\d\)",word[0]):
            with open("data\\words\\words_eng.txt","a",encoding="utf-8") as f:
                f.write(f"{i[-1]}")
                continue
        answer="error"

    if ", n " in answer:
        answer = answer.split(", n ")[0]
    elif ", v " in answer:
        answer = answer.split(", v ")[0]
    elif ", adj" in answer:
        answer = answer.split(", adj")[0]
    elif "/" in answer:
        answer = re.sub(r"/\W*\S*/","",answer)
    elif not re.search(r"\w",i[-1]) and i[-1]!="" and i[-1]!="\n":
        i[-1]="error"
    
    with open("data\\words\\words_eng.txt","a",encoding="utf-8") as f:
        f.write(f"\n{answer.lower().strip()} - {i[-1].strip().lower()}")
    
    