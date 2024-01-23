from dml import db_insert, db_update, db_delete, db_selectall
from pprint import pprint



# db_insert('Max Lemes', 'sdfsdf', 'max@ufg.br')
# db_insert('Lemes', 'sdfsdf', 'max1@ufg.br')
# db_insert('MaxLemes  t', 'sdfsdf', 'max2@ufg.br')
# db_insert('Mames ', 'sdfsdf', 'max3@ufg.br')

item = db_selectall()

for item in db_selectall():
   pprint(item)
   
