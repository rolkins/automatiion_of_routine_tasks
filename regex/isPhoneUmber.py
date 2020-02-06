import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
           return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Позвони мне завтра по номеру 415-555-1011. 415-555-9999 - это телефонный номер моего офиса'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Найденный телефонный номер ' + chunk)

print('Готово')


#Regex
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Мой номер 415-555-1111')
print('Найденный телефонный номер ' + mo.group())

#Regex Group()

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('Мой номер 415-111-5555')
print(mo.group(1))
print(mo.group(2))
print(mo.group())


phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('Мой номер (415) 555-3232')
print(mo.group(1))
print(mo.group(2))


heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile потерял колесо')
print(mo.group())
print(mo.group(1))


batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())


phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('Мой номер 932-444-3412')
print(mo1.group())
mo2 = phoneNumberRegex.search('Мой номер 334-3213')
print(mo2.group())


batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowowowowoman')
print(mo3.group())
