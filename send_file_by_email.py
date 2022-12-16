rom email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



from email.message import EmailMessage
import os
import datetime
from datetime import datetime
import csv
import time
import re
import base64

import urllib.request, urllib.error

import warnings
warnings.filterwarnings('ignore')

#prepare functions

def actual_date():
  """ return date """
    now = datetime.now()
    date_now = now.date()
   
    return date_now

def select_file():
  """ Select file, in thos case is a date format """
    pattern = r"\\([\d]{8})"
    pattern_date = r"^([\d]*)-([\d]*)-([\d]*)"
    #pattern_third = r"(\[\]\')"

    date_now = str(actual_date())
    control_date = re.sub(pattern_date, r"\1\2\3", date_now)
    
    dir = "C:\\Users\\user\\Downloads\\"
    
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        
        if not os.path.isdir(fullname):
            
            sub_result = re.search(pattern, fullname)
            
            #result = re.sub(pattern_third,  r"", str(sub_result))
            if any(x in sub_result[0] for x in control_date):
                return name
            else:
                print("REVISAR")

def change_path():
  """Change path of the file to the work directory"""
    path_source = "C:\\Users\\user\\Downloads\\" + select_file()
    path_destination = "C:\\Users\\user\\Documents\\Python Scripts\\" + select_file()
    print(path_destination)

    os.replace(path_source, path_destination)


def select_file2():
  """select the file again, this time in the working directory"""
  
    pattern = r"\\([\d]{8})"
    pattern_date = r"^([\d]*)-([\d]*)-([\d]*)"
    #pattern_third = r"(\[\]\')"

    date_now = str(actual_date())
    control_date = re.sub(pattern_date, r"\1\2\3", date_now)
    
    dir = os.getcwd()
    
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        
        if not os.path.isdir(fullname):
            
            sub_result = re.search(pattern, fullname)
            
            #result = re.sub(pattern_third,  r"", str(sub_result))
            if any(x in sub_result[0] for x in control_date):
                return name
            else:
                print("REVISAR")





# prepare de navigator
url = "https://urltogo.com"
 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

driver_options = Options()
driver_options.add_argument(headers)
driver_options.add_argument('--no-sandbox')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
print("abrir navegador")
#driver.execute_script("window.scrollTo(500, 1080);")

time.sleep(30)

#log in

decoded_user = base64.b64decode("dXNlcg==")
decoded_pw = base64.b64decode("cGFzc3dvcmQ=")

user = decoded_user.decode("utf-8")
passw = decoded_pw.decode("utf-8")

user_login = driver.find_element("xpath", "//*[@id='username']").send_keys(user)
user_passw = driver.find_element("xpath", "//*[@id='password']").send_keys(passw)
user_passw = driver.find_element("xpath", "//*[@id='password']").send_keys(Keys.RETURN)

print("login")
time.sleep(30)

#search the right option

main_menu1 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]").text
main_menu2 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]").text
main_menu3 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]").text
main_menu4 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[1]").text

if main_menu1 == "Correct menu":
    main_menu1 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/a").click()
if main_menu2 == "Correct menu":
    main_menu2 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/a").click()
if main_menu3 == "Correct menu":
    main_menu3 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/a").click()
if main_menu4== "Correct menu":
    main_menu4 = driver.find_element("xpath", "/html/body/div[4]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[1]/a").click()  
else: 
    print("Thinking...[]")

time.sleep(5)


#options button
driver.find_element("xpath", "html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/article/div[1]/div/div/div[2]/button/div/span[2]").click()
print("click button")

#download option
driver.find_element("xpath", "/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/article/div[1]/div/div/div[2]/ul/li[7]/a").click()
print("download file")

#wait for the download
time.sleep(90)

#change the downloaded file to working directory
change_path()
print("Directory change")
time.sleep(10)

os.chdir("C:\\Users\\user\\Documents\\Python Scripts\\")

#prepare the file to send

msg = MIMEMultipart()
files =  select_file2()
user = 'user@domain.com'
send_to ="sendto@domain.com
msg['From'] = user
msg['To'] = send_to
msg['Subject'] = "Tittle"

part = MIMEBase('application', "octet-stream")
with open(files, 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
                'attachment; filename={}'.format(file))
msg.attach(part)

#prepare the email server

server = smtplib.SMTP('10.9.3.2:5' )
server.set_debuglevel(1)


server.ehlo()
server.starttls()
server.ehlo() #second ehlo it's necesary for any servers...

#send email

try:
    server.sendmail(
        msg['From'],
        msg['To'],
        msg.as_string())
 
    server.quit()
 
    print ("successfully sent email to %s:" % (msg['To']))
except:
    print("unable to connect")


try:
    os.remove(select_file2())
except:
    print("file not deleted")
