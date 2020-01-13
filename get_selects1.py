# -*- coding: utf-8 -*-

import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
driver.get("http://suninjuly.github.io/selects1.html")

# time.sleep(5)

num1 = driver.find_element_by_id("num1").text
num2 = driver.find_element_by_id("num2").text

num_all = int(num1) + int(num2)
print(num_all)


# dropdown = driver.find_element_by_id("dropdown")
# dropdown.click()

select = Select(driver.find_element_by_id("dropdown"))
select.select_by_value(str(num_all)) # ищем элемент с текстом "Python"

submit_button = driver.find_element_by_class_name("btn-default")
submit_button.click()

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
# driver.quit()

