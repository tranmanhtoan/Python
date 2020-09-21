
import time
from selenium import webdriver

videoFileName = "VideoList.txt"
btPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"


videoFile = open(videoFileName)
listVideo = videoFile.readlines()


videoIndex = 0
tabIndex = 0

# Open browser
browers = webdriver.Chrome()

# Open url 1st => tabIndex = 0
browers.get(listVideo[videoIndex])

# Click play button
time.sleep(1)
playButton = browers.find_element_by_css_selector(btPlaySelector)
playButton.click()

# Open new tab with 2nd video => tabIndex = 1
time.sleep(0.5)
videoIndex = videoIndex + 1
js = "window.open('"+listVideo[videoIndex].strip()+"')"
browers.execute_script(js)

# Go to previous tab and open new video
time.sleep(2)
tabIndex = 0
handle = browers.window_handles[tabIndex]
browers.switch_to.window(handle)

videoIndex = videoIndex + 1
browers.get(listVideo[videoIndex])
