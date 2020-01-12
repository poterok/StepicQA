# -*- coding: utf-8 -*-

import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
driver.get("http://suninjuly.github.io/math.html")
# time.sleep(5)


# Передаем значение в функцию
x_element = driver.find_element_by_css_selector("#input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)


# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_id("answer")



# Напишем текст ответа в найденное поле
textarea.send_keys(y)


checkbox = driver.find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton1 = driver.find_element_by_id("robotsRule")
radiobutton1.click()



# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_class_name("btn-default")
submit_button.click()

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

