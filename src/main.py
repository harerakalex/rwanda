from provinces import provinces as data

def format_input(name: str) -> str:
    return name.strip().capitalize()

def get_provinces() -> list:
    return [province for province in data.keys()]

def get_districts(province = ''):
    try:
        if province:
            return [key for key in data[format_input(province)].keys()]
        if not province:
            return [district for province in data.keys() for district in data[province]]
    except:
        return None

def get_sectors(province = '', district = ''):
    try:
        if province and district and data[format_input(province)]:
            return [sector for sector in data[format_input(province)][format_input(district)].keys()]
        if not province and not district:
            return [sector for province in data.keys() for district in data[province] for sector in data[province][district]]
    except:
        return None

def get_cells(province = '', district = '', sector = ''):
    try:
        if province and district and sector and get_sectors(province, district):
            return [cell for cell in data[format_input(province)][format_input(district)][format_input(sector)].keys()]
        if not province and not district and not sector:
            return [cell for province in data.keys() for district in data[province] for sector in data[province][district] for cell in data[province][district][sector]]
    except:
        return None

def get_villages(province = '', district = '', sector = '', cell = ''):
    try:
        if province and district and sector and cell and get_cells(province, district, sector):
            return [village for village in data[format_input(province)][format_input(district)][format_input(sector)][format_input(cell)]]
        if not province and not district and not sector and not cell:
            return [village for province in data.keys() for district in data[province] for sector in data[province][district] for cell in data[province][district][sector] for village in data[province][district][sector][cell]]
    except:
        return None
