from main import *

print('Get Provinces====', get_provinces())
print('Get Districts====', get_districts('kiGali'))
print('Get sectors====', get_sectors('kigali', 'nyarugenge'))
print('Get Cells====', get_cells('kigaLI', district='Nyarugenge', sector='nyarugenge'))
print('Get villages====', get_villages('kigaLI', district='Nyarugenge', sector='nyarugenge', cell='rwampara'))

