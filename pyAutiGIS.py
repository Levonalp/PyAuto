import geopandas as gpd
import folium

# Load property data with geospatial information (replace with your data file)
property_data_file = 'property_data.shp'
property_data = gpd.read_file(property_data_file)

# Calculate the center of the map (mean latitude and longitude)
center_lat = property_data.geometry.centroid.y.mean()
center_lon = property_data.geometry.centroid.x.mean()

# Create an interactive map centered on the properties
property_map = folium.Map(location=[center_lat, center_lon], zoom_start=14)

# Define a function to style the GeoJSON features
def style_function(feature):
    return {
        'fillColor': 'blue',  # or use feature['properties']['your_property_field'] for dynamic color
        'color': 'black',
        'weight': 2,
        'opacity': 0.5
    }

# Add property boundaries to the map
folium.GeoJson(
    property_data,
    name='Property Boundaries',
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['property_id', 'address'], aliases=['Property ID', 'Address'])
).add_to(property_map)

# Add a layer control to toggle property boundaries
folium.LayerControl().add_to(property_map)

# Save the map as an HTML file
property_map.save('property_map.html')
