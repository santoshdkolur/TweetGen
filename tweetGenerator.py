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



options = Options()
options.add_argument("headless")

def get_driver():
  return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



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

def generate(iname, iusername,itweet,itweet_image):
  

    driver = webdriver.Chrome('chromedriver',chrome_options=options)
    #driver = get_driver()
    
    driver.get(os.getcwd()+"\webpage\Tweetgen.html")
    theme = driver.find_element(by=By.XPATH,value="/html/body/div/div/div[1]/form/div[2]/div[3]/label")
    theme.click()
    name = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[6]/input")
    if iname=="Null":
        name.send_keys("Thulp fiction")
    else:
        name.send_keys(iname)

    username = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[7]/div[1]/input")
    username.send_keys("wemighthavesomethinghere")
    username.clear()
    if iusername=="Null":
        username.send_keys("wemighthavesomethinghere")
    else:
        username.send_keys(iusername) 

    verified_checkbox = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[8]/div/input")

    try:
        verified_checkbox.click()
    except:
        verified_checkbox.click()

    tweet = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[9]/textarea")
    tweet.clear()
    tweet.send_keys(itweet)
    profile_image = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[5]/input")
    profile_image.send_keys(os.getcwd()+"\\spiderman.jpg")

    
    tweet_image = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[10]/input")
    """if itweet_image is not None:
        tweet_image.send_keys(os.getcwd()+"\\uploadedTweetImg.jpg")
    else:
        tweet_image.clear()"""

    time = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[11]/input")
    time.send_keys("23:59")
    date = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[12]/div[1]/div/div[1]/input")
    date.clear()
    date.send_keys("1")
    month = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[12]/div[1]/div/div[2]/select")
    month.send_keys("Apr")
    year = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[12]/div[1]/div/div[3]/input")
    year.clear()
    year.send_keys("1969")
    retweet = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[13]/div[1]/div/div[1]/input")
    retweet.clear()
    retweet.send_keys("4")
    quote = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[13]/div[1]/div/div[2]/input")
    quote.clear()
    quote.send_keys("2")
    likes = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[13]/div[1]/div/div[3]/input")
    likes.clear()
    likes.send_keys("0.0")
    client = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[14]/input")
    client.clear()
    client.send_keys("Twitter for Television")
    fact_check = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[1]/form/div[15]/input")
    fact_check.clear()
    fact_check.send_keys("Content seen above might not be an actual tweet")
    
    

    generate_image = driver.find_element(by=By.ID, value ="downloadButton")
    wait2 =WebDriverWait(driver, 10)
    wait2.until(EC.element_to_be_clickable(generate_image))
    driver.execute_script("arguments[0].click();", generate_image)
    # generate_image.click()
    sleep(3)
    final_image = driver.find_element(by=By.XPATH, value ="/html/body/div/div/div[2]/div/div[3]/img")
    src=final_image.get_attribute('src')
    img = get_file_content_chrome(driver,src)
  
    return img
