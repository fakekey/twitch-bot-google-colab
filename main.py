import requests
import warnings
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
from time import sleep

warnings.filterwarnings("ignore", category=DeprecationWarning)


def check_for_updates():
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print(
                "A new version is available. Please download the latest version from GitHub.")
            sleep(3)
            return False
        return True
    except:
        return True


def save_settings(twitch_username, set_160p):
    with open('settings.txt', 'w') as file:
        file.write(f"Twitch Username: {twitch_username}\n")
        file.write(f"Set 160p: {set_160p}\n")


def load_settings():
    try:
        with open('settings.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                twitch_username = lines[0].split(': ')[1].strip()
                set_160p = lines[1].split(': ')[1].strip()
                return twitch_username, set_160p
    except:
        pass
    return None, None


def set_stream_quality(driver):
    wait = WebDriverWait(driver, 15)

    element_video = None
    while not element_video:
        try:
            # Ad
            element_video_ad_xpath = "//div[@data-test-selector='sad-overlay']"
            element_video = driver.find_element(
                By.XPATH, element_video_ad_xpath)
        except:
            # No ad
            element_video_xpath = "//div[@data-a-target='player-overlay-click-handler']"
            element_video = driver.find_element(By.XPATH, element_video_xpath)
        sleep(0.5)

    actions = ActionChains(driver)

    actions.move_to_element(element_video).perform()

    settings_button = driver.find_element(
        By.XPATH, "//button[@aria-label='Settings']")
    settings_button.click()

    quality_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='Quality']")))
    quality_option.click()

    quality_levels_parent = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@data-a-target='player-settings-menu']")))
    quality_levels = quality_levels_parent.find_elements(By.XPATH, './*')

    last_btn = quality_levels[len(quality_levels)-1]
    last_btn.click()  # Last btn because sometimes 160p not available


def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/announcement.txt",
                         headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")


def main():
    if not check_for_updates():
        return
    print_announcement()

    twitch_username, set_160p = load_settings()

    os.system(f"title Kichi779 - Twitch Viewer Bot @kichi#0779 ")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                               
                             Github  github.com/kichi779    """)))
    announcement = print_announcement()
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")
    print("")

    proxy_servers = ['https://www.blockaway.net', 'https://www.croxyproxy.com', 'https://www.croxyproxy.rocks',
                     'https://www.croxy.network', 'https://www.croxy.org', 'https://www.youtubeunblocked.live', 'https://www.croxyproxy.net']

    def selectRandom(proxy_servers):
        return random.choice(proxy_servers)

    proxy_url = selectRandom(proxy_servers)

    print(Colors.red, "Proxy servers are randomly selected every time")
    if twitch_username is None or set_160p is None:

        twitch_username = input(Colorate.Vertical(
            Colors.green_to_blue, "Enter your channel name (e.g Kichi779): "))
        set_160p = input(Colorate.Vertical(
            Colors.purple_to_red, "Do you want to set the stream quality to 160p? (yes/no): "))

        save_settings(twitch_username, set_160p)

    else:
        use_settings = input(Colorate.Vertical(
            Colors.green_to_blue, "Do you want to use your saved settings? (yes/no): "))
        if use_settings.lower() == "no":

            twitch_username = input(Colorate.Vertical(
                Colors.green_to_blue, "Enter your channel name (e.g Kichi779): "))
            set_160p = input(Colorate.Vertical(
                Colors.purple_to_red, "Do you want to set the stream quality to 160p? (yes/no): "))

            save_settings(twitch_username, set_160p)

    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue,
                      "How many proxy sites do you want to open? (Viewer to send)")))

    os.system("cls")
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/UkSJP8RUxc    
                             Github  github.com/kichi779    """)))
    print('')
    print('')
    print(Colors.red, Center.XCenter(
        "Viewers Send. Please don't hurry. If the viewers does not arrive, turn it off and on and do the same operations"))

    # Removing chromedriver.exe because we don't need it
    if os.path.exists('./chromedriver.exe'):
        print('chromedriver.exe in current folder, removing')

        try:
            os.remove("chromedriver.exe")
            print('Sucessfully removed chromedriver.exe')
        except:
            raise Exception(
                "Cannot remove chromedriver.exe, please do it manually")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    print('\n')

    for i in range(proxy_count):
        print(f"[{i}] Adding viewer")
        # Select a random proxy server for this tab
        random_proxy_url = selectRandom(proxy_servers)
        driver.execute_script("window.open('" + random_proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(random_proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

        # Waiting to be on the livestream page
        wait = WebDriverWait(driver, 240)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[@data-a-target='follow-button']")))

        print(f"[{i}] Viewer added.")
        if set_160p == "yes":
            try:
                set_stream_quality(driver)
                print(f"[{i}] Sucessfully setting the lowest quality")
            except Exception as err:
                # raise err
                print(f"[{i}] Unable to set the lowest quality")

        print('\n============================\n')

    input(Colorate.Vertical(Colors.red_to_blue,
          "Viewers have all been sent. You can press enter to withdraw the views and the program will close."))
    driver.quit()


if __name__ == '__main__':
    main()
