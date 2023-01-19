import askuser as au

ask_bot = au.get_string('поговори со мной: ')

bot = \
    {
    'привет': 'здравствуйте',
    'как тебя зовут': 'скайнет',
    'что ты можешь': 'могу уничтожить человечество',
    'сколько тебе лет': '39 лет',
    'hi': 'Hello!!'
    }
    
for item in bot:
    if item == ask_bot:
        print(bot[ask_bot])
        break
    else:
        print('i cannot answer. good buy :(')