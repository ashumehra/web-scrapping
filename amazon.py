from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=r"D:\Project\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://amazon.in")

# time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.click()
element.send_keys('basketball shoes\n')
count=0
while count<=5:
    time.sleep(3)
    source = driver.page_source
    # print(source)
    soup = BeautifulSoup(source, 'html.parser')
    t=soup.findAll('span',{'class':'a-size-base-plus a-color-base a-text-normal'})
    t2=soup.findAll('span',{'class':'a-price-whole'})
    z=zip(t,t2)
    with open('basketball.tsv','a',encoding="utf-8") as f:
        f.write('shoes name\tprice\n')
        for word in z:
            # print(word[0].text,'    ₹',word[1].text)
            f.write(word[0].text)
            f.write("\t")
            f.write(word[1].text)
            f.write('\n')
    print(len(t))
    element = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[7]/div/div/div/ul/li[7]')
    webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
    count+=1
    print(count)
# print(source)
