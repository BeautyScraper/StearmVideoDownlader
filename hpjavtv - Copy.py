from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import galleryCrawler as gC
import msvcrt
import os
import time
# breakpoint()
# binary = FirefoxBinary(".\\geckodriver-v0.26.0-win64\\geckodriver.exe")
opts = Options()
# opts.set_headless()
driver = webdriver.Firefox(options=opts)
driver.implicitly_wait(60)


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
        filename = 'VideoList1.txt'
        p = "".join(args)
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
    
    time.sleep(10)
    try:
        trg = driver.find_element_by_css_selector("iframe.lazyloaded")
        driver.get(trg.get_attribute("src"))
    except Exception as e:
        breakpoint()
    
    # breakpoint()
    
    listResolution = ["360p","480p","720p","1080p"]
    
    # driver.implicitly_wait(60 * 10)
    # breakpoint()
    # WebDriverWait(driver, 10).until(
    # ) .fp-engine
    time.sleep(10)
    # hiddenDiv = driver.find_element_by_css_selector(".fp-player > div:nth-child(5)")document.querySelector(".fp-engine").click()
    # breakpoint()
    try:
        hiddenDiv = driver.find_element_by_css_selector(".loading-container")
        driver.execute_script("arguments[0].click();", hiddenDiv)
        print('first play Click Success')
    # except:
        # hiddenDiv = driver.find_element_by_css_selector("div[aria-label=Play]")
        # driver.execute_script("arguments[0].scrollIntoView();", hiddenDiv)
    except:
        vpd = driver.find_element_by_css_selector("video")
        driver.execute_script("arguments[0].play();", vdp)
        print('second play Click might Success')
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])
        print('tab Changed')
        time.sleep(10)
    try:
        qButton = driver.find_element_by_css_selector("div.jw-icon[button=qSwitch]")
    except Exception as e:
        vpd = driver.find_element_by_css_selector("video")
        driver.execute_script("arguments[0].play();", vdp)
        try:
            print('Quality Button Found')
            qButton = driver.find_element_by_css_selector("div.jw-icon[button=qSwitch]")
        except:
            print('Quality Button still not Found')
            qButton = None
        # breakpoint()
    if qButton != None:
        driver.execute_script("arguments[0].scrollIntoView();", qButton)
        print('Bring into the view')
        # driver.switch_to_window(driver.window_handles[0])
        qButton.click()
        print('Clicked On Qbutton')
    # driver.execute_script("arguments[0].click();", qButton)
        try:
            avail_reso = driver.find_elements_by_css_selector("div.jw-settings-submenu[role=menu]>button")
        except Exception as e:
            print(e)
            breakpoint()    
        flag = False
        for reso_l in listResolution[::-1]:
            for reso in avail_reso:
                resoString = reso.get_attribute("innerHTML")
                if resoString == reso_l:
                    print(resoString)
                    try:
                        reso.click()
                    except Exception as e:
                        breakpoint()
                    # driver.execute_script("arguments[0].click();", reso)
                    flag = True
                    break
            if flag:
                break
        # breakpoint()
                
        time.sleep(10)
    # VideoResoButton = driver.find_element_by_class_name('fp-settings')
    # time.sleep(10)
    # VideoResoButton.click()
    # driver.execute_script("arguments[0].click();", VideoResoButton)
    # time.sleep(10)
    # highesResoFound = getLastArgWithoutException(checkElementExist,listResolution)
    # time.sleep(10)
    # print(highesResoFound)
    # tirElem = driver.find_element_by_link_text(highesResoFound)
    # driver.execute_script("arguments[0].click();", tirElem)
    # time.sleep(10)
    # breakpoint()
    video = driver.find_element_by_css_selector(".jw-video")
    videoUrl = video.get_attribute("src")
    # breakpoint()
    ret = gC.rssImageExtractor()
    ret.downloadThisVideo(10,"D:\\paradise\\stuff\\new\\JAV",url.rstrip('/').split('/')[-1]+'HD.mp4',videoUrl)
    # gC.rssImageExtractor.downloadThisVideo(10,"D:\\paradise\\stuff\\new\\DeepFakeVideos",url.split("/")[-1]+".mp4",videoUrl)
    print(videoUrl)

def UserCommand(key=b'm'):
    if msvcrt.kbhit():
        pKey = msvcrt.getch()
        print("you pressed: ",pKey)
        if pKey == key:
            return True
        return False
    
if __name__ == "__main__":
    # main()
    with open("hpjav.opml","r") as fp:
        for url in fp:
            if UserCommand(b'q'):
              # driver.close()
              print('Closing webDriver')
              break  
            try:
                VideoDownload(url.strip())
                
            except Exception as e:
                print(f"while processing {url} something happend {e}" + e)
                continue
            
    driver.quit()
            # driver.get(url)
