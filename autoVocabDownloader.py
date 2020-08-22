from time import sleep
def setVariables():
	import sys
	global credentialsPath,updateDestination
	try:	
		credentialsPath=sys.argv[1]
		updateDestination=sys.argv[2]
		return True
	except:
		print("Error you have to write to parameters: credentialsPath, updateDestination")
		print("Error use relative path for credentials (for example: cred.txt) and full path for updateDestination (/home/name/Desktop/)")
		return False
def getNewDataToDesktop():
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
	import os
	

	
	password="Error"
	username="Error"
	with open(credentialsPath,"r") as file:
		contents=file.read()
		password=contents.split(" ")[1]
		username=contents.split(" ")[0]

		
	#setting up profile to never ask when downloading file and setting download location
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 0)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
	#profile.set_preference("browser.download.dir", '/home/lars/Desktop/English_Vocabulary')


	url="https://altkönigschule.net/login/index.php"
	global driver
	driver =webdriver.Firefox(firefox_profile=profile)
	driver.get(url)
	sleep(1)
	
	#get username element and then fill in the username
	usernameElement=driver.find_element_by_id("username")
	usernameElement.send_keys(username)
	#get password html-elemnt and later fill in the password
	passwordElement=driver.find_element_by_id("password")
	passwordElement.send_keys(password)

	sleep(1)
	#clicking the submit button
	driver.find_element_by_id("loginbtn").click()
	#clicking on enlgish class
	sleep(2)
	englishClassLink=driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[7]/div[1]/div/div[1]/a")
	englishClassLink.click()
	sleep(1)
	#clicking on download link
	downloadVocab=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[2]/div[3]/ul/li/div/div/div[2]/div[1]/a")
	downloadVocab.click()
	

def changeDirToSchool():
	import os
	import shutil 
	try:
		os.remove(updateDestination+"/VocabularySheet.xlsx")
	except:
		print("File didnt yet exist")
	shutil.move("/home/lars/Desktop/VocabularySheet.xlsx", updateDestination)

def main():
	if setVariables():
		setVariables()
		getNewDataToDesktop()
		sleep(1)
		changeDirToSchool()
		driver.close()
if __name__=="__main__":
	main()