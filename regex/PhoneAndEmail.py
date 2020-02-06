import pyperclip, re

phoneRegex = re.compile(
    r'''(
        (\d{3}|\(\d{3}\))? # территориальный код
        (\s|-|\.)? # разделитель
        (\d|-|\.) # первые три цифры
        (\d{4}) # последние четыре цифры
        (\s*(ext|x|ext.)\s*(\d{2, 5})) ? # добавочный номер 
    )''', re.VERBOSE)

emailRegex = re.compile(
    r'''(
        [a-zA-Z0-9._%+-]+ # username
        @                 # @
        [a-zA-Z0-9.-]+    # domain name
        (\.[a-zA-Z]{2, 4}) # other part ot address
    )''', re.VERBOSE
)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 1:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена: ')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены')



