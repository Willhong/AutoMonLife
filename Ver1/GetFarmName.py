import requests
from bs4 import BeautifulSoup

def GetFarmList(monsterName):

    url = 'https://meso.kr/monster.php?n='+monsterName

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tag = soup.find_all(attrs={'class': 'btn btn-primary btn-sm copybtn'})
        subtag=[]
        for i in tag:
            subtag.append(i['dt-name'])
        return subtag
    else : 
        print(response.status_code)