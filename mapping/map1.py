import folium
import pandas

data= pandas.read_csv("Volcanoes_USA.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[7.152822, 3.305524], zoom_start= 6)
fgv= folium.FeatureGroup("Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=([lt,ln]), radius= 6, tooltip=str(el)+"m", fill_color=color_producer(el), fill= True, color=color_producer(el), fill_opacity=0.7))

fgp= folium.FeatureGroup("Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<15000000
else 'orange' if 15000000 <= x['properties']['POP2005'] < 30000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("map.html")
