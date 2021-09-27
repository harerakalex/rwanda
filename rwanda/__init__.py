from .main import get_provinces, get_districts, get_sectors, get_cells, get_villages

__all__ = [
    'get_provinces',
    'get_districts',
    'get_sectors',
    'get_cells',
    'get_villages'
]

print('Get Provinces====', get_provinces())
print('Get Districts====', get_districts('kiGali'))
print('Get sectors====', get_sectors('kigali', 'nyarugenge'))
print('Get Cells====', get_cells('kigaLI', district='Nyarugenge', sector='nyarugenge'))
print('Get villages====', get_villages('kigaLI', district='Nyarugenge', sector='nyarugenge', cell='rwampara'))

