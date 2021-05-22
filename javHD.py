from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import galleryCrawler as gC

import os
import time
# breakpoint()
# binary = FirefoxBinary(".\\geckodriver-v0.26.0-win64\\geckodriver.exe")
opts = Options()
opts.set_headless()
driver = webdriver.Firefox()


# url = "https://mrdeepfakes.com/video/9133/shraddha-kapoor-doggy-style-faceset-test-dfl-2-0-request"
# driver.get(url)
# assert "Python" in driver.title


def getLastArgWithoutException(testF,listResolution):
    lastWorking = ""
    for reso in listResolution:
        try:
            testF(reso)
            lastWorking = reso
        except:
            break
    return lastWorking

def alreadyNotDone(func):
    def wrapper(*args, **kwargs):
        p = "".join(args)
        filename = "VideoList1.txt"
        print(p)
        ret = gC.rssImageExtractor()
        if ret.alreadyNotDownloaded(filename,p):
            func(*args, **kwargs)
            ret.downloadCompleteRegister(filename,p)
    return wrapper

def checkElementExist(reso):
    driver.find_element_by_link_text(reso)

@alreadyNotDone
def VideoDownload(url):
    driver.get(url)
    listResolution = ["360p","480p","720p","1080p"]
    
    # if "mrdeepfakes" not in  driver.current_url:
        
        # return VideoDownload(url)
    # driver.implicitly_wait(60 * 10)
    # breakpoint()
    # WebDriverWait(driver, 10).until(
    # ) .fp-engine
    breakpoint()
    # time.sleep(10)
    tv = driver.find_element_by_css_selector(".loading-container > svg:nth-child(1) > path:nth-child(1)")
    tv.click()
    
    
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    
    
    # time.sleep(20)
    breakpoint()
    cssP = "div.jw-icon:nth-child(13)"
    resoBtn = driver.find_element_by_css_selector(cssP)
    resoBtn.click()
    time.sleep(10)
    # hiddenDiv.scrollIntoView()
    hiddenDiv.click()
    time.sleep(10)
    VideoResoButton = driver.find_element_by_class_name('fp-settings')
    time.sleep(10)
    VideoResoButton.click()
    time.sleep(10)
    highesResoFound = getLastArgWithoutException(checkElementExist,listResolution)
    time.sleep(10)
    print(highesResoFound)
    driver.find_element_by_link_text(highesResoFound).click()
    # breakpoint()
    video = driver.find_element_by_css_selector(".fp-engine")
    videoUrl = video.get_attribute("src")
    # breakpoint()
    ret = gC.rssImageExtractor()
    ret.downloadThisVideo(10,"D:\\paradise\\stuff\\new\\DeepFakeVideos",url.split("/")[-1]+".mp4",videoUrl)
    # gC.rssImageExtractor.downloadThisVideo(10,"D:\\paradise\\stuff\\new\\DeepFakeVideos",url.split("/")[-1]+".mp4",videoUrl)
    print(videoUrl)

if __name__ == "__main__":
    # main()
    with open("javLinks.opml","r") as fp:
        for url in fp:
            try:
                VideoDownload(url.strip())
            except Exception as e:
                print(f"while processing {url} something happend {e}")
                continue
    driver.close()
            # driver.get(url)
