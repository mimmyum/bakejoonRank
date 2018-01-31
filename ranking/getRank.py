from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/mingyulee/Develop/Web/chromedriver')
driver.implicitly_wait(3)

def getRank(id, password) :
    driver.get('https://www.acmicpc.net/login/?next=%2F')
    driver.find_element_by_name('login_user_id').send_keys(id)
    driver.find_element_by_name('login_password').send_keys(password)

    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/form/div[4]/div[2]/button').click()

    driver.implicitly_wait(2)

    personalPage = 'https://www.acmicpc.net/user/' + id
    req = requests.get(personalPage)
    html = req.text

    soup = BeautifulSoup(html,'html.parser')
    tables = soup.select(
        '#statics > tbody > tr > td '
    )

    rank = str(tables[0])
    rank = rank[4:len(rank)-5]
    solved = str(tables[1])
    solved = solved[len(solved) - 12:len(solved) - 9]

    return rank, solved


print(getRank('mimmyum','Alaaba2ek'))