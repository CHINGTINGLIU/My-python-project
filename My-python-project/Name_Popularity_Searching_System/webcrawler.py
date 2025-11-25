"""
File: webcrawler.py
Name: Alice Liu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

GROUP_SIZE = 5  # rank, male_name, male_count, female_name, female_count
MAX_GROUP = 200


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #
        tags = soup.find_all('td')
        data_list = []
        for tag in tags:
            target = tag.text.strip()
            if target != '':
                data_list.append(target)

        sum_male = 0
        sum_female = 0
        group_count = 0
        for i in range(0, len(data_list), GROUP_SIZE):

            if i+GROUP_SIZE > len(data_list):
                break
            elif group_count >= MAX_GROUP:
                break
            else:
                data_list[i]
                group = data_list[i: i+GROUP_SIZE]
                male_number = string_manipulation(group[2])
                sum_male += male_number
                female_number = string_manipulation(group[4])
                sum_female += female_number

                group_count += 1

        print(f"Male Number: {sum_male}")
        print(f"Female Number: {sum_female}")

        driver.quit()


def string_manipulation(text):
    ans = ''
    for ch in text:
        if ch.isdigit():
            ans += ch
        if ans == '':
            return 0
    return int(ans)


if __name__ == '__main__':
    main()
