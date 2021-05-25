import json
import pygal
from pygal_maps_world import i18n
from pygal_maps_world.maps import World
from country_codes import get_country_code


            
            
# ===============無法使用的舊板本===============================================
# wm = pygal.Worldmap()
# wm.title = 'North, Central, and South America'
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.render_to_file('americas.svg')
# 
# =============================================================================
          
            
wm = World() 
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')



# =============================================================================
# worldmap_chart = World()
# worldmap_chart.title = 'Some countries'
# worldmap_chart.add('F countries', ['fr', 'fi'])
# worldmap_chart.render_to_file('chart.svg')
# =============================================================================
