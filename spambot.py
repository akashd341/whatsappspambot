from selenium import webdriver
import time
def banner():
    print(''' 

,--.                    ,--.  ,---.                 
|  |    ,--.,--.  ,---. `--' /  .-'  ,---.  ,--.--. 
|  |    |  ||  | | .--' ,--. |  `-, | .-. : |  .--' 
|  '--. '  ''  ' \ `--. |  | |  .-' \   --. |  |    
`-----'  `----'   `---' `--' `--'    `----' `--' 
                                                        ''')

banner()
print("\n")
print("\n")
print("********* Whatsapp spam ********")
p=1
while p<6:
    time.sleep(1),
    print(" - "),
    p=p+1,

print("\n")
driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')
driver.get('https://web.whatsapp.com')


driver.find_element_by_css_selector("span[title='" + raw_input("enter name :") + "']").click()
x = raw_input("Enter message to send: ")
while True:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(x)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span').click()
