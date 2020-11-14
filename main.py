import time
import datetime as dt
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Scrap:

	def __init__(self):
		self.__driver_path = "your_driver_path"
		self.options = webdriver.ChromeOptions()
		self.maximized = self.options.add_argument("start-maximized")
		self.browser = webdriver.Chrome(executable_path = self.__driver_path, options = self.options)
		self.url = "https://www.kap.org.tr/tr/"
		# Flow
		self.browser.get(self.url)
		self._getInScrapMode()
		self._scrollDown()
		self._getData()
		self._closeBrowser()

	def _scrollDown(self):
		ht = self.browser.execute_script("return document.documentElement.scrollHeight;")
		
		while True:
		    prev_ht = self.browser.execute_script("return document.documentElement.scrollHeight;")
		    self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
		    time.sleep(2)
		    ht = self.browser.execute_script("return document.documentElement.scrollHeight;")
		    
		    if prev_ht==ht:
		        break

	def _getInScrapMode(self):
		try:
			firstButton = self.browser.find_element_by_xpath("/html/body/div[6]/div/div[6]/disclosure-list/div/div/div/div[1]/div[1]/div/button[3]").click()
		
		except:
			pass

	def _getData(self):
		counter = 1
		kod = self.browser.find_elements_by_css_selector("disclosure-list-item")
		for i in tqdm(kod):
		 	self._toTxt(i.text + "\n")
		 

	def _closeBrowser(self):
		self.browser.close()

	def _ifNotExists(self, file, txt):
		with open(file, "r+", encoding = "utf-8") as f:
			r = f.read()

		if txt not in r:
			return True

		else:
			return False

	def _toTxt(self, x):
		now = dt.datetime.now()
		year = now.strftime("%d-%m-%Y")

		with open(f"kap-{year}.txt", "a+", encoding ="utf-8") as f:

			if self._ifNotExists(f"kap-{year}.txt", x) == True:
				f.write(x + "\n")

			else:
				print("\nNo new notification.\n")

if __name__ == "__main__":
		x = Scrap()

	
