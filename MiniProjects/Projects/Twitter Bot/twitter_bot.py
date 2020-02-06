# Username = BitBot97561591
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TwitterBot() :
    username , password = '' , ''
    bot = webdriver.Firefox()
    def __init__ (self , username , password) :
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path='geckodriver.exe')
        username = 'BitBot97561591'
        password = 'iambot'
    def login ( self ) :
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(20)
        user = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        user.clear()
        password.clear()
        user.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(20)
    def liker ( self , hashtag ) :
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'t&src=typd')
        time.sleep(20)
        for i in range (1 , 5) :
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(20)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweet]
            for link in links :
                bot.get('https://twitter.com/'+link)
                try :
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(20)
                except Exception as ex :
                    time.sleep(20)
tweet = TwitterBot('BitBot97561591' , 'iambot')
tweet.login()
tweet.liker('webdevelopment')