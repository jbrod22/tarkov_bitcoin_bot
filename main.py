import pyautogui, time, json

class Tarkov_Bot:
    def __init__(self, config):
        self.locations = config["locations"]
        self.sleep = config["sleep_time"]
    
    def get_location(self, location_key):
        return self.locations[location_key]

    def get_sleep_time(self, sleep_key):
        return self.sleep[sleep_key]

    def execute(self):
        pyautogui.moveTo(*self.get_location("windows_button"))
        pyautogui.click()
        pyautogui.typewrite('battlestate')
        pyautogui.press('enter')
        pyautogui.moveTo(*self.get_location("launcher_play"))
        print("Clicking play in 5...")
        time.sleep(self.get_sleep_time("launcher_wait"))
        pyautogui.click()
        print("Waiting for game to load")
        time.sleep(self.get_sleep_time("application_wait"))
        print("Moving to Hideout")
        pyautogui.moveTo(*self.get_location("hideout"), duration=1)
        pyautogui.click()
        time.sleep(self.get_sleep_time("loading_hideout"))
        print("Moving to Bitcoin")
        pyautogui.moveTo(*self.get_location("bitcoin_generator"), duration=1)
        pyautogui.click()
        time.sleep(self.get_sleep_time("loading_bitcoin"))
        print("Collecting Bitcoins")
        pyautogui.moveTo(*self.get_location("get_all"), duration=1)
        pyautogui.click()
        time.sleep(self.get_sleep_time("collect_bitcoin"))
        print("Moving to main menu")
        pyautogui.moveTo(*self.get_location("main_menu"), duration=1)
        pyautogui.click()
        print("Moving to exit")
        pyautogui.moveTo(*self.get_location("exit_menu_button"), duration=1)
        pyautogui.click()
        print("Clicking Exit")
        pyautogui.moveTo(*self.get_location("confirm_exit"), duration=1)
        pyautogui.click()
        print("Completed")

def main():
    with open('config.json') as f:
        config = json.load(f)
    bot = Tarkov_Bot(config)
    bot.execute()

main()