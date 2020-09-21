
import time
from selenium import webdriver

videoFileName = "VideoList.txt"
viewFileName = "ViewCount.txt"
btPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"


videoFile = open(videoFileName)
listVideo = videoFile.readlines()

NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(listVideo)
LOOP_TIME = 3

videoIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0

# Open browser
browser = webdriver.Chrome()

# Open url 1st => tabIndex = 0
browser.get(listVideo[videoIndex])

# Click play button
time.sleep(2)
playButton = browser.find_element_by_css_selector(btPlaySelector)
playButton.click()

while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
    tabIndex = (tabIndex + 1) % NUMBER_OF_TAB

    if tabCount < NUMBER_OF_TAB:
        tabCount = tabCount + 1
        browser.execute_script("window.open('"+listVideo[videoIndex].strip()+"')")
    else:
        browser.switch_to.window(browser.window_handles[tabIndex])
        time.sleep(1)
        browser.get(listVideo[videoIndex])

    viewCount = viewCount + 1
    saveFile = open(viewFileName, "w")
    saveFile.write(str(viewCount))
    saveFile.close()

    time.sleep(LOOP_TIME)
