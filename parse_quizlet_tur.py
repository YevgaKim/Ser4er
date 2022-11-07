import time

from bs4 import BeautifulSoup
from selenium import webdriver


def get_tur_or_eng(lan:str,file:str):
    driver = webdriver.Chrome(
            executable_path="sys\\chromedriver",
        )
    try:
        
        driver.get(url="https://quizlet.com")
        time.sleep(60)

        with open("sys\\index.html", "w",encoding="utf-8") as f:
            f.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("sys\\index.html","r",encoding="utf-8") as f:
        src = f.read()
    if lan=="en":
        with open(f"data\\words\\words_{file}.txt","a",encoding="utf-8") as f:
            f.write(f"\n")

    soup = BeautifulSoup(src,"lxml")

    words_tur= soup.findAll("span",class_=f"TermText notranslate lang-{lan}")
    tur=[]
    for i in words_tur:
        word=i.text
        tur.append(word)

    words_ukr= soup.findAll("span",class_="TermText notranslate lang-uk")
    ukr=[]
    for i in words_ukr:
        word=i.text
        ukr.append(word)

    for i in range(len(tur)):
        with open(f"data\\words\\words_{file}.txt","a",encoding="utf-8") as f:
            f.write(f"{tur[i].lower()} - {ukr[i].lower()}\n")

if __name__=="__main__":
    pass