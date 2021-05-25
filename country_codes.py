import pygal
from pygal_maps_world import i18n
for country_code in sorted(i18n.COUNTRIES.keys()):
    print(country_code, i18n.COUNTRIES[country_code])



def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))