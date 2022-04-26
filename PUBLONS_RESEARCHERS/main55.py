#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    import pandas as pd
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import requests
    import numpy as np 
    from selenium.webdriver.chrome.options import Options
    
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'performance':'ALL' }

    chrome_options = Options()
    chrome_options.add_experimental_option('w3c', False)

    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe',desired_capabilities=d, options=chrome_options)
    
    driver.get('https://publons.com/researcher/?institution=674072&country=123&is_core_collection=1&is_last_twelve_months=1&order_by=num_reviews')  
    timeout = 10
    
    p=0
    a = (By.CSS_SELECTOR, '.table-container')
    wait = WebDriverWait(driver,30)
    df = wait.until(EC.element_to_be_clickable(a))

    for i in df.find_elements_by_tag_name('div'):
        if i.text != "":
            try:
                x=df.find_elements_by_xpath('//*[@id="browse"]/div[2]/div/div[3]/div/div[1]/span')[p].text
                df1=pd.Series(x,index=['Id'])
                df1= pd.DataFrame(df1)
                df1 = df1.rename(columns = {0:'Id'})
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
                time.sleep(1.5)

                c=df.find_elements_by_xpath('//*[@id="browse"]/div[2]/div/div[3]/div/a[1]/div/span[2]')[p].text
                
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
                time.sleep(0.6)

                d=df.find_elements_by_xpath('//*[@id="browse"]/div[2]/div/div[3]/div/div[2]/span')[p].text
        
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
                time.sleep(3.55)  

                e=df.find_elements_by_xpath('//*[@id="browse"]/div[2]/div/div[3]/div/div[3]/span')[p].text
            
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(4.0009)

                f=df.find_elements_by_xpath('//*[@id="browse"]/div[2]/div/div[3]/div/div[4]/span')[p].text 
      
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
                time.sleep(5.222)
         

                thelist = [[x],[c],[d],[e],[f]]
                df2 = pd.Series( (v[0] for v in thelist) )
                df2= pd.DataFrame(df2)
                df2 = df2.T
                df2 = df2.rename(columns = {0:'id',1:'investigadores',2:'publicaciones',3:'comentarios',4:'registros'},axis=1)
                print(df2)
                df2.to_csv('DATA/lista.csv')
            except:
                pass
        p+=1
   




# In[3]:


main()


# In[ ]:





# In[ ]:





# In[ ]:




