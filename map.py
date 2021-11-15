import folium
map = folium.Map(location=[38.56, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38, -99], [37, -96]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi!", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")