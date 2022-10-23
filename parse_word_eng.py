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
    if i[-1]=="":
        continue
    eng = i[1].split("\n")
    eng.pop()
    word=""
    for j in eng:
        word+=j
    word = word.split(",")
    answer=""
    if len(word)==2:
        answer=word[0].strip()
    elif len(word)>=3:
        answer=f"{word[0].strip()}, {word[1].split('=')[-1].strip()}"
    else:
        print(i)
        answer="ERROR"
    if ", n " in answer:
        answer = answer.split(", n ")[0]
    elif ", v " in answer:
        answer = answer.split(", v ")[0]
    elif "/" in answer:
        answer = re.sub(r"/\W*\S*/","",answer)
    with open("data\\words\\words_eng.txt","a",encoding="utf-8") as f:
        f.write(f"{answer.lower()} - {i[-1].strip().lower()}\n")
    
    