# first_name = 'Mulia Ayu'
# last_name = 'Fatimah'
# full_name = f'{first_name} {last_name}'
# print (full_name)

from datetime import datetime

today = datetime.now()

datetime = today.strftime('%Y-%m-%d-%H-%M-%S')
print (datetime)