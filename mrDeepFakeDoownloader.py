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
driver = webdriver.Firefox(options=opts)


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
        

def checkElementExist(reso):
    driver.find_element_by_link_text(reso)

def VideoDownload(url):
    driver.get(url)
    listResolution = ["360p","480p","720p","1080p"]
    # driver.implicitly_wait(60 * 10)
    # breakpoint()
    # WebDriverWait(driver, 10).until(
    # ) .fp-engine
    time.sleep(10)
    hiddenDiv = driver.find_element_by_css_selector(".fp-player > div:nth-child(5)")
    driver.execute_script("arguments[0].scrollIntoView();", hiddenDiv)
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

def main():
    opts = Options()
    opts.set_headless()
    driver = webdriver.Firefox(options=opts)

if __name__ == "__main__":
    # main()
    with open("links.opml","r") as fp:
        for url in fp:
            VideoDownload(url.strip())
    driver.close()
            # driver.get(url)
