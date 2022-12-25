text = 'я сижу и смотрю из чужого окна'
print('сижу' in text) # проверяет наличие слова - bool
print(len(text)) # длина текста - int
print(text.isdigit()) # проверка на цифровую строку - все знаки - цифры - bool
print(text.islower()) # проверка на все прописные  - bool
print(text.replace('из','ИЗ')) # заменяет - str

help(text.istitle) # встроененая помощь по питону

# СРЕЗЫ
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-8]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...