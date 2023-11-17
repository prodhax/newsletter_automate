#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# In[32]:


df=pd.read_excel("./seedlist.xlsx")
df.head()


# In[34]:


accounts = df.apply(lambda row: {"email": row["Emails"]}, axis=1).to_list()


# In[35]:


newsletter_urls = [
"https://edition.cnn.com/newsletters",
"https://www.theskimm.com/newsletters",
"https://www.producthunt.com/newsletters/archive/new",
"https://www.wired.com/",
"https://char.gd/",
]

# Set the path to the ChromeDriver executable in 'options'
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("webdriver.chrome.driver=C:/Users/Ali/Desktop/Data Analyst/Etl/email/chromedriver")

# Initialize the Chrome webdriver with 'options'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(3)

# driver = webdriver.Chrome(executable_path="C:/Users/Ali/Desktop/Data Analyst/Etl/email/chromedriver", options=options)
# driver.maximize_window()
# time.sleep(3)


for account in accounts:
    email = account["email"]
    for url in newsletter_urls:
    # Open the newsletter subscription URL
        driver.get(url)
        print("running")
        time.sleep(3)
        
        # cnn news
        if url == "https://edition.cnn.com/newsletters":
            time.sleep(3)
            s_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='newsletter-0']/button")))
            s_next_button.click()

            time.sleep(3)

            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "newsletter-subscribe-email-input")))
            email_input.send_keys(email)

            # Click the "Next" button
            time.sleep(3)
            e_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "newsletter-subscribe-button")))
            e_next_button.click()
            time.sleep(3)

        # skimm news
        elif url == "https://www.theskimm.com/newsletters":
            time.sleep(3)
            s_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[1]/main/div[1]/div[2]/div/div[1]")))
            s_next_button.click()
            

            time.sleep(3)
            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
            email_input.send_keys(email)

            # Click the "Next" button
            time.sleep(3)
            e_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[1]/main/div[2]/div/div[3]/form/button")))
            e_next_button.click()
            time.sleep(3)

        # producthunt news
        elif url == "https://www.producthunt.com/newsletters/archive/new":
            time.sleep(3)
            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[3]/aside/div/div[1]/form/div/div/input")))
            email_input.send_keys(email)
            time.sleep(3)

            # Click the "Next" button
            e_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[3]/aside/div/div[1]/form/button/div")))
            e_next_button.click()
            time.sleep(3)

        # wiredaily news
        elif url=="https://www.wired.com/":
            time.sleep(3)
            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='homepage_newsletter-text-field-email']")))
            email_input.send_keys(email)
            time.sleep(3)

            # Click the "Next" button
            e_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='homepage_newsletter']/span/button/span")))
            e_next_button.click()
            time.sleep(3)

        #charged news
        elif url == "https://char.gd/":
            time.sleep(3)

            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email-signup']")))
            email_input.send_keys(email)
            time.sleep(3)

            # Click the "Next" button
            time.sleep(3)
            e_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/form/button")))
            e_next_button.click()
            time.sleep(3)
        
        else:
            print("error")


# Close the WebDriver
driver.quit()


# In[ ]:




