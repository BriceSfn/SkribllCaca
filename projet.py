from selenium import webdriver
from selenium.webdriver.common.by import By
from google_images_search import GoogleImagesSearch
import requests



drive = webdriver.Chrome()

drive.get("https://skribbl.io/?hcCajZzG")

NAME_INPUT = '//*[@id="home"]/div[2]/div[2]/div[1]/input'
RANDOM_SKIN_BUTTON = '//*[@id="home"]/div[2]/div[2]/div[2]/div[4]'
BUTTON_START = '#home > div.panels > div.panel > button.button-play'
BUTTON_DE_MERDE = '//*[@id="cmpwelcomebtnyes"]/a'
GAME_INDICATOR = '//*[@id="game-word"]/div[1]'

def play(name):
    drive.find_element(By.XPATH, BUTTON_DE_MERDE).click()
    drive.find_element(By.XPATH, NAME_INPUT).send_keys(name)
    drive.find_element(By.XPATH, RANDOM_SKIN_BUTTON).click()
    drive.find_element(By.CSS_SELECTOR, BUTTON_START).click()
    while True :
        game = drive.find_element(By.ID,"game-word").find_element(By.CLASS_NAME, "description")
        if game.text == "GUESS THIS":
            pass
        elif game.text == "DRAW THIS":
            print("DRAW THIS")
        elif game.text == "WAITING":
            print("WAITING")
            if "show" in drive.find_element(By.XPATH, '//*[@id="game-canvas"]/div[2]/div[2]').get_attribute("class"):
                game = drive.find_element(By.XPATH, '//*[@id="game-canvas"]/div[2]/div[2]').find_element(By.CLASS_NAME, "word")
                word= game.text
                gis = GoogleImagesSearch('AIzaSyCaNmJqnUZVUqDfaJ42AXz9-0Z78CD24sE', '52e363b86b1c2467f')
                
                search = {
                    'q': word.strip(),
                    'num': 1,
                }

                gis.search(search)

                result = gis.results()[0]
                image_url = result.url

                response = requests.get(image_url)
                with open('table_image.jpg', 'wb') as f:
                    f.write(response.content)

            
        
    
    
play("caca")

while True :
        game = drive.find_element(By.ID,"game-word").find_element(By.CLASS_NAME, "description")
        if game.text == "GUESS THIS":
            pass
        elif game.text == "DRAW THIS":
            print("DRAW THIS")
        elif game.text == "WAITING":
            print("WAITING")
            if "show" in drive.find_element(By.XPATH, '//*[@id="game-canvas"]/div[2]/div[2]').get_attribute("class"):
                game = drive.find_element(By.XPATH, '//*[@id="game-canvas"]/div[2]/div[2]').find_element(By.CLASS_NAME, "word")
                WORD = game.text
                game.click()