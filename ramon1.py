import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Carregue a página da web com o retângulo vermelho
driver.get("file:///C:/Users/bruno.angelo/Downloads/ramon.html")

# Aguardar até a caixa vermelha aparecer na tela
try:
    '''    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "exemplo: itjm.eitisolucoes.local"))
        )
    '''
    driver.implicitly_wait(5)

    # Encontre as coordenadas da caixa vermelha
    '''rect = element.rect

    # Clique na posição do retângulo vermelho
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, rect['x'] + rect['width'] / 2, rect['y'] + rect['height'] / 2)
    action.click()
    action.perform()'''
    time.sleep(2)
    elemento =  driver.find_element(By.XPATH, "/html/body/div[1]").click()


except Exception as e:
    print("Erro ao encontrar o elemento:", e)



