from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from bs4 import BeautifulSoup
import time, re, sys

from PyQt5.QtWidgets import QApplication
from pickGroupsQt import pickGroupsToPost
from loginQt import loginCredentials

class FacebookBot:
    URL = 'https://mbasic.facebook.com'

    def __init__(self, driver):
        '''Usually chrome driver but could be phantomJS'''
        self.driver = driver

    def login(self, username, password):
        '''Go to basic facebook page and login with given credentials'''
        self.driver.get(self.URL)

        login_elem_string = '#m_login_email'
        password_elem_string = '#login_form > ul > li:nth-child(2) > div > input'

        username_pg_elem = self.driver.find_element(By.CSS_SELECTOR, login_elem_string)
        password_pg_elem = self.driver.find_element(By.CSS_SELECTOR, password_elem_string)

        username_pg_elem.send_keys(username)
        password_pg_elem.send_keys(password)
        password_pg_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def getGroups(self):
        '''Use webdriver to return only groups you are in'''
        self.driver.get(self.URL + '/groups/?seemore&refid=27')

        groups = []
        source = self.driver.page_source
        soup = BeautifulSoup(source, "html.parser")

        # find all group's url link
        for group in soup.find_all("a", href=re.compile(r"groups/\d")):
            groups.append([group.contents, self.URL + group['href']])

        return groups

    def postToGroup(self, posts, groups, checkedGroups):
        for idx, (post, group) in enumerate(zip(posts, groups)):

            if not checkedGroups[idx]:
                continue

            self.driver.get(group[1])
            time.sleep(3)
            try:

                post_pg_element = self.driver.find_element(By.CSS_SELECTOR, '#u_0_0')
                submit_pg_element = self.driver.find_element(By.NAME, 'view_post')

                post_pg_element.send_keys(post)
                submit_pg_element.click()
            except NoSuchElementException:
                print (group, 'failed')
                continue


def main():
    usr = 'g7158808@nwytg.net'
    pwd = 'vujmub-Pikkyv-1mihdy'

    # need to make these global so garbage collected does not cause crash
    global app
    global app2

    app = QApplication(sys.argv)
    login = loginCredentials()
    result = login.exec_()
    if result == login.Rejected:
        sys.exit(0)

    credentials = [x.text() for x in login.login_creds]

    driver = webdriver.Chrome()
    fbBot = FacebookBot(driver)
    # fbBot.login(*credentials)
    fbBot.login(usr, pwd)

    groups = fbBot.getGroups()

    app2 = QApplication(sys.argv)
    pickGroups = pickGroupsToPost(groups)
    result = pickGroups.exec_()
    checkedGroups = [cbox.isChecked() for cbox in pickGroups.checkboxes]
    posts = [post.toPlainText() for post in pickGroups.posts]

    if result == pickGroups.Accepted:
        fbBot.postToGroup(posts, groups, checkedGroups)

    sys.exit(login)
    sys.exit(pickGroups)

if __name__ == '__main__':
    main()
