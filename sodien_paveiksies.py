import pandas as pd
from bs4 import BeautifulSoup 
import requests 

x = input('ievadi loterijas nosaukumu(eurojackpot;viking-lotto;superbingo;latloto;keno;loto5;joker;joker7) \n')
y = []
i = 1
if x =='loto5':
    web = 'https://www.latloto.lv/lv/rezultati/loto5'
    
    source = requests.get(web).text
    soup = BeautifulSoup(source, 'lxml')
    skaitli = soup.find_all('div', class_='numbered-items')
    
    
    for mammite in skaitli:
        milfene = mammite.text
       
        milf = milfene.split('\n')
        milf.remove('')
        milf.remove('')
        y.append(milf)

else:

    web = 'https://www.latloto.lv/lv/arhivs/'


    
    while(i<=5):
        m = str(i)
        saite = web+x+'/'+m
        source = requests.get(saite).text
        soup = BeautifulSoup(source, 'lxml')
        skaitli = soup.find_all('div', class_='numbered-items')
        
        i = i+1
        for mammite in skaitli:
            milfene = mammite.text
            milf = milfene.split('\n')
            milf.remove('')
            milf.remove('')
            y.append(milf)



df=pd.DataFrame(y)
df = df.mode()
print(df)
