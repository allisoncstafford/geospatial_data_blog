import folium
import geopandas as gpd

def create_geo_map(geo_df, index, location, zoom=17, tiles='Stamen Terrain'):
    """creates a folium map with the geometry highlighted

    Args:
        geo_df: a geopandas dataframe (must have a column 'geometry')
        index: the index of the row you want mapped
        location: [lat, long] list with the center location for the map
        zoom: start zoom level. Default: 17
        tiles: Folium tiles / design. Default: Stamen Terrain

    Returns:
        folium map with geometry highlighted
    """
    # create geodataframe for zip code
    zip_code = gpd.GeoDataFrame(geo_df.iloc[index]).T

    # get the geojson for the zipcode
    gjson = zip_code['geometry'].to_json()
    
    # create folium map
    m = folium.Map(location=location,
                   tiles=tiles,
                   zoom_start=zoom)

    # add geojson to the map
    folium.GeoJson(
        gjson,
        name='geojson'
    ).add_to(m)
    
    return m