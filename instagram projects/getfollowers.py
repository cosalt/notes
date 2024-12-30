from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_instagram_following(username, password, target_profile):
    driver = webdriver.Chrome()
    try:
        # go to insta login
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)  # wait

        # log in
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)  #  wait

        # go to target's following
        profile_url = f"https://www.instagram.com/{target_profile}/"
        driver.get(profile_url)
        time.sleep(3)  # Wait for the profile page to load

        # Click on the "Following" link
        following_link = driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        following_link.click()
        time.sleep(3)  # wait

        # scroll
        modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = driver.find_element(By.XPATH, modal_xpath)
        
        # scroll to end
        last_height = driver.execute_script("return arguments[0].scrollHeight", modal)
        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)  # wait a bit for the scroll to load
            new_height = driver.execute_script("return arguments[0].scrollHeight", modal)
            if new_height == last_height:
                break
            last_height = new_height

        # extract all userames
        following = []
        elements = modal.find_elements(By.CSS_SELECTOR, "a[href*='/']")
        for element in elements:
            href = element.get_attribute("href")
            if href and f"/{target_profile}/" not in href:  # exclue profile links
                username = href.replace("https://www.instagram.com/", "").strip("/")
                following.append(username)

            
        following_count_displayed = driver.find_element(By.PARTIAL_LINK_TEXT, "following").text
        following_count = int(following_count_displayed.split()[0])

        if len(following) != following_count:
            print(f"Warning: Instagram shows {following_count} following, but {len(set(following))} were fetched.")
        else:
            print("All followers successfully fetched!")

        driver.quit()
        return following

    except Exception as e:
        driver.quit()
        print(f"An error occurred: {e}")
        return []

instagram_username = ""
instagram_password = ""
target_profile = ""  

following_list = get_instagram_following(instagram_username, instagram_password, target_profile)
print(following_list)
print(len(following_list))
#remove dups
following_list = set(following_list)
for i in following_list:
    print(i)
print(len(following_list))
