#  Створити клас Bot з атрибутом name та методами say_name та send_message.
#
# send_message має приймати параметри self і message і має друкувати message.
## Метод say_name має друкувати значення атрибуту name.

class Bot:
    name = "name"
    def say_name(name):
        print(name)
    def send_message (self, message):
        print(message)






print ('атрибут -', Bot.name)
Bot.say_name('Robinzon')
Bot.send_message('ggg', 'bbb')

