from selenium import webdriver
import os,base64
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



options = Options()
options.add_argument("headless")

def get_driver():
  return webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)



def get_file_content_chrome(driver, uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  if type(result) == int :
    raise Exception("Request failed with status %s" % result)
  return base64.b64decode(result)

def generate_tweet(iname, iusername,itweet,itweet_image,my_progress,value):

    driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)

    driver.get("https://www.tweetgen.com/create/tweet.html")
    theme = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/input")
    theme.click()
    name = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/span[1]")
    name.clear()
    name.send_keys(iname)
    username = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[3]/span")
    username.send_keys("wemighthavesomethinghere")
    username.clear()
    username.send_keys(iusername)
    main_window = driver.current_window_handle 
    my_progress.progress(value+20)
    value+=20
    tweet = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/span")
    tweet.clear()
    tweet.send_keys(itweet)
    profile_click = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[1]/img")
    driver.execute_script("arguments[0].click();", profile_click)
    sleep(2)
    popup_page=""
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    profile_image = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[2]/div/input")
    profile_image.send_keys(os.getcwd()+"/spiderman.jpg")
    profile_done = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[3]/button")
    driver.execute_script("arguments[0].click();", profile_done)
    driver.switch_to.window(main_window)
    my_progress.progress(value+10)
    value+=10
    
    
    #tweet_image = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[10]/input")
    """if itweet_image is not None:
        tweet_image.send_keys(os.getcwd()+"/uploadedTweetImg.jpg")
    else:
        tweet_image.clear()"""

    date_time = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[5]/span[1]")
    driver.execute_script("arguments[0].click();", date_time)
    sleep(2)
    popup_page=""
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    time = driver.find_element(by=By.ID, value ="timeInput")
    driver.execute_script("arguments[0].value = '12:00';",time)
    date = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[1]/input")
    driver.execute_script("arguments[0].value = '1';",date)
    month = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/select")
    driver.execute_script("arguments[0].value = 'Apr';",month)
    year = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[3]/input")
    driver.execute_script("arguments[0].value = '1969';",year)
    done = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[3]/button")
    driver.execute_script("arguments[0].click();", done)
    driver.switch_to.window(main_window)

    retweet = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[6]/span[1]/b")
    retweet.clear()
    retweet.send_keys(Keys.DELETE,"4")
    quote = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[6]/span[2]/b")
    quote.clear()
    quote.send_keys(Keys.DELETE,"2")
    
    client = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[5]/span[2]/span")
    #client.clear()
    client.send_keys("Twitter for Television")

    generate_image = driver.find_element(by=By.ID, value ="generateButton")
    wait2 =WebDriverWait(driver, 10)
    wait2.until(EC.element_to_be_clickable(generate_image))
    driver.execute_script("arguments[0].click();", generate_image)
    
    #generate_image.click()
    sleep(2)
    final_image = driver.find_element(by=By.XPATH, value ="/html/body/div[5]/div/div/div[2]/img")
    src=final_image.get_attribute('src')
    img = get_file_content_chrome(driver,src)
    my_progress.progress(value+20)
    return img


def generate_retweet(iname, iusername, itweet,itweet_image, my_progress, value):
    driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)

    driver.get("https://www.tweetgen.com/create/reply.html")
    theme = driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[1]/div[2]/div[1]/div[3]/input")
    theme.click()
    name = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    name.clear()
    name.send_keys(iname)
    username = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]")
    username.send_keys("wemighthavesomethinghere")
    username.clear()
    username.send_keys(iusername)
    main_window = driver.current_window_handle 
    my_progress.progress(value+20)
    value+=20
    tweet = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/span")
    tweet.clear()
    tweet.send_keys(itweet)
    profile_click = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/img")
    driver.execute_script("arguments[0].click();", profile_click)
    sleep(2)
    popup_page=""
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    profile_image = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[2]/div/input")
    profile_image.send_keys(os.getcwd()+"/spiderman.jpg")
    profile_done = driver.find_element(by=By.XPATH, value ="/html/body/div[2]/div/div/div[3]/button")
    driver.execute_script("arguments[0].click();", profile_done)
    driver.switch_to.window(main_window)
    my_progress.progress(value+10)
    value+=10
    
    
    #tweet_image = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[10]/input")
    """if itweet_image is not None:
        tweet_image.send_keys(os.getcwd()+"/uploadedTweetImg.jpg")
    else:
        tweet_image.clear()"""

    date_time = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]")
    driver.execute_script("arguments[0].click();", date_time)
    sleep(2)
    popup_page=""
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    date = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[2]/div/div/div[1]/input")
    driver.execute_script("arguments[0].value = '1';",date)
    month = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[2]/div/div/div[2]/select")
    driver.execute_script("arguments[0].value = 'Apr';",month)
    year = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[2]/div/div/div[3]/input")
    driver.execute_script("arguments[0].value = '1969';",year)
    done = driver.find_element(by=By.XPATH, value ="/html/body/div[3]/div/div/div[3]/button")
    driver.execute_script("arguments[0].click();", done)
    driver.switch_to.window(main_window)

    metrics = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[4]")
    driver.execute_script("arguments[0].click();", metrics)
    sleep(2)
    popup_page=""
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    retweet = driver.find_element(by=By.XPATH, value ="/html/body/div[4]/div/div/div[2]/div/div[2]/input")
    driver.execute_script("arguments[0].value = '2';",retweet)
    replies = driver.find_element(by=By.XPATH, value ="/html/body/div[4]/div/div/div[2]/div/div[1]/input")
    driver.execute_script("arguments[0].value = '4';",replies)
    done = driver.find_element(by=By.XPATH, value ="/html/body/div[4]/div/div/div[3]/button")
    driver.execute_script("arguments[0].click();", done)
    driver.switch_to.window(main_window)
    
    delete_tweet = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div")
    #client.clear()
    driver.execute_script("arguments[0].click();", delete_tweet)
    delete_tweet = driver.find_element(by=By.XPATH, value ="/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/ul/li[3]/button")
    driver.execute_script("arguments[0].click();", delete_tweet)
    sleep(2)
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    driver.switch_to.window(popup_page)
    delete_tweet = driver.find_element(by=By.XPATH, value ="/html/body/div[5]/div/div/div[3]/button[2]")
    driver.execute_script("arguments[0].click();", delete_tweet)
    driver.switch_to.window(main_window)

    generate_image = driver.find_element(by=By.ID, value ="generateButton")
    wait2 =WebDriverWait(driver, 10)
    wait2.until(EC.element_to_be_clickable(generate_image))
    driver.execute_script("arguments[0].click();", generate_image)
    
    
    #generate_image.click()
    sleep(2)
    for handle in driver.window_handles:
        if handle != main_window:
            popup_page = handle
    final_image = driver.find_element(by=By.XPATH, value ="/html/body/div[5]/div/div/div[2]/img")
    src=final_image.get_attribute('src')
    img = get_file_content_chrome(driver,src)
    my_progress.progress(value+20)
    return img
