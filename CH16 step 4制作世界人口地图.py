import json
import pygal
from pygal_maps_world import i18n
from pygal_maps_world.maps import World
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        
        if code:
            print(code + ": "+ str(population))
        else:
            print('ERROR - ' + country_name)
            
            
            
wm = World() 
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
                         'pe', 'py', 'sz', 'uy', 've'])

wm.render_to_file('americas.svg')
# =============================================================================
# #wm = pygal.maps.world.World()#pygal.Worldmap()
# wm = pygal.Worldmap()
# wm.title = 'North, Central, and South America'
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.render_to_file('americas.svg')
# 
# =============================================================================

# =============================================================================
# worldmap_chart = World()
# worldmap_chart.title = 'Some countries'
# worldmap_chart.add('F countries', ['fr', 'fi'])
# worldmap_chart.render_to_file('chart.svg')
# =============================================================================
