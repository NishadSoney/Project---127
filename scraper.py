from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrap():
    headers = ["Name","Distance","Mass","Radius"]
    planet_data = []
    new_planet_data = []
    for i in range(0,453):
        while True:
            time.sleep(2)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        current_page_no = int(soup.find_all("input",attrs = {"class","page_no"})[0].get("value"))
        if current_page_no < i:
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        elif current_page_no > i:
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
        else:
            break
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tag = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tag[0]
            temp_list.append("https://exoplanets.nasa.gov/"+hyperlink_li_tag.find_all("a",href = True)[0]["href"])
            planet_data.append(temp_list)
            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            print(f"{i}page done 1")

scrap()