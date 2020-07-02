from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re, time
from datetime import datetime

# PREPARE TO SHART
email = 'poopypants69@cumzone.com'
password = 'engadine_chocolate_milkshake'
poopRegex = re.compile(r'and (\d*,\d*)')
poops = 0
post = 'https://www.facebook.com/110921237094461/posts/170714697781781/'
sex_funny_number = 69

#START ENDLESS POOP - NO NEED TO WIPE
while True:
    # INITIATE POOP MACHINE
    poop_machine = webdriver.Firefox()
    poop_machine.get('https://facebook.com')
    myPants = browser.find_element_by_id('email')
    myPants.send_keys(email)
    engadineBathroom = poop_machine.find_element_by_id('pass')
    engadineBathroom.send_keys(password)
    try: # IF YOU GET CRUSTY POOP
        poopinButton = poop_machine.find_element_by_id('loginbutton')
    except: # IF YOU GET SOGGY POOP
        poopinButton = poop_machine.find_element_by_name('login')
    poopinButton.click()
    time.sleep(3)
    # OPEN DOOR 
    poop_machine.get(post)
    time.sleep(sex_funny_number)
    # SEARCH FOR OPEN TOILET
    poopsButton = poop_machine.find_element_by_css_selector('span._3dlh:nth-child(1)')
    shart = ActionChains(poop_machine).move_to_element(poopsButton)
    shart.perform()
    time.sleep(sex_funny_number)
    # SEARCH FAILED, SHIT SELF (VIOLENTLY)
    poopsDirty = poop_machine.find_element_by_css_selector('._4kg > li:nth-child(20)')
    poops = poopRegex.findall(poopsDirty.text)
    poopNumber = int(poops[0].replace(',', ''))
    poopNumber = poopNumber+20
    # FIND MARKETING ANGLE TO FIX REPUTATION
    dots = poop_machine.find_element_by_xpath('//*[@aria-label="Story options"]')
    dots.click()
    time.sleep(sex_funny_number)
    # OH FUCK SOMEONE POSTED ABOUT IT ON TWITTER
    poopifyPost = poop_machine.find_element_by_xpath('//*[@data-testid="feed_post_edit"]')
    poopifyPost.click()
    time.sleep(sex_funny_number)
    # CRY
    toilet_AKA_pants = poop_machine.find_element_by_name('status_text')
    # UPDATE POOPBOOK POST
    toilet_AKA_pants.clear()
    toilet_AKA_pants.send_keys("ok ok i'll invest in renewables if this post gets " + str(int(poopNumber)+5) + " likes")
    # FIND AND CLICK FINISHED EDITING BUTTON
    finishedShitting = poop_machine.find_element_by_xpath('//*[@name="save"]')
    finishedShitting.click()
    fart = datetime.now()
    poop_time = fart.strftime("%H:%M:%S")
    print('Post has ' + str(poopNumber) + ' likes at ' + poop_time)
    poop_machine.quit()
    time.sleep(sex_funny_number)
    
