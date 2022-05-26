from selenium import webdriver
from win10toast import ToastNotifier
from selenium.webdriver.chrome.options import Options 

class youtubePlayer():
    def __init__(self):
        # name = input("Enter a youtube channels name: ")
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.name = name
    
    def play(self,name):
        self.name = name
        self.driver.get("https://www.youtube.com/user/"+self.name+"/videos")
        new = self.driver.find_element_by_xpath('//*[@id="video-title"]').text
        # new.click() #to traverse to first video
        toaster = ToastNotifier()
        toaster.show_toast("New Video from "+self.name+"\nCheck it out",new)
            

        
name=""
file = open("D:\My Stuff\Work\Code\Projects\youtube_channel.txt","r")   
youtubers = file.readline().split(",")
while youtubers!=[]:
    name = youtubers[0]
    youtubers.remove(name)
    bot = youtubePlayer()
    bot.play(name)
bot.driver.close()
exit()