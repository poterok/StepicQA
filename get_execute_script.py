# -*- coding: utf-8 -*-

import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/execute_script.html")

# time.sleep(5)

text_x = driver.find_element_by_id("input_value")
x = text_x.text
print(x)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)


answer = driver.find_element_by_id("answer")
answer.send_keys(y)




# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
# driver.quit()

