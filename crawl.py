import re
import json
from typing import *
from banner import banners
import random

class Analasy:
    def __init__(self,link: str) -> None:
        self.link = link
        # self.status = option["status"] or ""
        # self.season = option["season"] or ""
        # self.year = option["year"] or "2024"
        # self.sort = option["sort"] or random.choice(["comment","year","popular"])
    def checkLink(self) -> bool:
        if(re.match("^https?:\/\/[\d|\w]+\.[a-z]{1,3}",self.link)):
            return True
        else:
            return False
    def crawler(self) -> None:
        import requests
        r=requests.get(self.link)
        r.encoding = "utf-8"
        pattern = r'title="(.*?)" href="./phim/'
        x = re.findall(pattern,r.text)
        z = 1
        for i in x:
            print(f"[{z}]:{i}")
            z+=1
def main():
    banners()
    link = input("Enter link: ")
    check = Analasy(link=link)
    if(not check.checkLink()):
        print("Your link is not valid")
    else:
        check.crawler()
if __name__ =="__main__":
    main()
#http://anime47.com/tim-nang-cao/?status=&season=&year=2024&sort=comment
