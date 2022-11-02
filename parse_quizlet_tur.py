import time

from bs4 import BeautifulSoup
from selenium import webdriver


def get_tur():
    driver = webdriver.Chrome(
            executable_path="sys\\chromedriver",
        )
    try:
        
        driver.get(url="https://quizlet.com")
        time.sleep(80)

        with open("sys\\index.html", "w",encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("sys\\index.html","r",encoding="utf-8") as f:
        src = f.read()

    soup = BeautifulSoup(src,"lxml")

    words_tur= soup.findAll("span",class_="TermText notranslate lang-tr")
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
        with open("data\\words\\words_tur.txt","a",encoding="utf-8") as f:
            f.write(f"{tur[i].lower()} - {ukr[i].lower()}\n")

if __name__=="__main__":
    pass