import xml.etree.ElementTree as ET
import json

namefile = open('botw_names.json')
object_names = json.load(namefile)
namefile.close()

root = ET.parse('map_objects.xml').getroot()

dropactor_objs = root.findall('./Objs/value')

for actor in dropactor_objs:
    name = actor.findall('./UnitConfigName')[0].text
    coords = [node.text for node in actor.findall('./Translate/value')]
    drop_actors = actor.findall('./_Parameters/DropActor')
    drop_tables = actor.findall('./_Parameters/DropTable')
    
    if name in object_names:
        nice_name = object_names[name]
    else:
        nice_name = name
        
    if len(drop_actors):
        drop_actor = drop_actors[0].text
        print('{"internal_name":"%s", "display_name":"%s", "x":%g, "y":%g},' % (name+':'+drop_actor, nice_name+':'+object_names[drop_actor], float(coords[0][:-1]), float(coords[-1][:-1])))
    elif len(drop_tables):
        drop_table = drop_tables[0].text
        if drop_table == 'Normal':
            print('{"internal_name":"%s", "display_name":"%s", "x":%g, "y":%g},' % (name, nice_name, float(coords[0][:-1]), float(coords[-1][:-1])))
        else:
            print('{"internal_name":"%s", "display_name":"%s", "x":%g, "y":%g},' % (name+':'+drop_table, nice_name+':'+drop_table, float(coords[0][:-1]), float(coords[-1][:-1])))
    else:
        print('{"internal_name":"%s", "display_name":"%s", "x":%g, "y":%g},' % (name, nice_name, float(coords[0][:-1]), float(coords[-1][:-1])))
    
