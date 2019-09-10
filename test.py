import requests
from bs4 import BeautifulSoup
import csv


url = "https://github.com/trending?since=monthly"
r= requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
t=soup.findAll(class_='Box-row')
file_name = "git_trend.csv"
f = csv.writer(open(file_name, 'a', newline=''))
# f.writerow(['reponame','dev name','star'])
for word in t:
    full_repo_name = word.find('h1').text.split()
    dev_name = full_repo_name[0].strip()
    repo_name = full_repo_name[2].strip()
    star = word.find('a',{'class':'muted-link d-inline-block mr-3'}).text.strip()
    print(repo_name,"---baba---",dev_name,"---baba---",star)
    f.writerow([repo_name,dev_name,star])
print(len(t))
