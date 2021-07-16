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
