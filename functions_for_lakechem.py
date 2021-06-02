#!/usr/bin/env python
# coding: utf-8

import geopandas as gpd

# Custom functions for alpine-lakes workflow
# Function one : for checking coordinate column names.
def name_check(source_df):
    '''Check the column names in the profided dataframe. If they meet the
    requirements for function two (pull_coords), the check will pass. If not,
    the check will fail and raise an error.
    
    Parameters
    -----------
    source_df : pandas dataframe object
        The dataframe containing site names, coordinates, and data (lake water
        chemistry, for example).
    
    Returns
    -----------
    A print statement reassurance or an exception.
    '''
    colnames = list(source_df.columns)
    needed_names = ['LAT', 'LONG']
    
    for name in needed_names:
        if name in colnames:
            print('The', name, 'column does not need to be renamed.')
        else:
            raise ValueError('The column does not exist or needs to be renamed for pull_coords to run.')
        
# Function two : for pulling unique coordinate pairs from a dataframe
def pull_coords(source_df, site_ID, lat_col, long_col, crs):
    '''Create a geopandas dataframe (gdf) containing the coordinates for your 
    features of interest (for example, lakes) and a unique identifier for each
    site (for example, the lake name). This is ideal for dataframes containing
    multiple rows of data for a single location. The returned gdf contains
    only unique instances of site names and coordinates - so there are only as
    many rows as you have feature/study locations. This function is meant to 
    give you a more compact gdf to make plotting your study locations easier.

    Parameters
    -----------
    source_df : pandas dataframe object
        The dataframe containing site names, coordinates, and data (lake water
        chemistry, for example).

    site_ID : str
        The column name from source_df containing your site/feature identifier
        (this may be something like a lake name, site ID, forest name, etc).

    lat_col : str
        The column name from source_df containing Latitude coordinates.

    long_col : str
        The column name from source_df containing Longitude coordinates.

    crs : str
        A string describing the coordinate reference system you want to use.
        For instance, if you are using the standard WGS84 projection, input
        crs = 'EPSG:4326'.

    Returns
    -----------
    coords_gdf : geopandas geodataframe object
        A gdf containing unique instances of site names and coordinate pairs
        meant to make plotting site/feature locations simpler.

    '''
    # Check that the column names are correct and rename them if necessary so
    # that gpd.GeoDataFrame() does not fail.
    try:
        name_check(source_df)
    except ValueError:
        source_df = source_df.rename(columns={lat_col: 'LAT', long_col: 'LONG'})
        return source_df

    # Subset the data and pull unique coordinate pairs to make a geodataframe.
    coords_subset = source_df[[site_ID, lat_col, long_col]]
    coords_unique = coords_subset.groupby(
        [site_ID, lat_col, long_col]).count().reset_index()
    
    # Convert coords_unique to a gdf by specifying geometry and crs.
    coords_gdf = gpd.GeoDataFrame(coords_unique, geometry=gpd.points_from_xy(
        coords_unique.LONG, coords_unique.LAT))
    coords_gdf = coords_gdf.set_crs("EPSG:4326")

    return coords_gdf

# Function three : for quickly generating timeseries plots
def time_plot(grouped_df, a_param, axis, color_dict):
    """Create a single plot of ion concentration/chemical property for the
    specified years and lake group.
    
    Parameters
    -----------
    grouped_df : grouped pandas df object
        The grouped dataframe containing data you want to plot.

    a_param : string
        A string describing the name of the ion or other parameter you want to
        plot (this should be a column name in grouped_df).

    axis : string
        The name of the axis you want to plot on (eg 'ax1')
    
    color_dict : string
        The name of a custom color dictionary for plotting.

    Returns
    -----------
    plot_obj : 
        A plot showing changes in ion concentration over time for a specified
        lake or group of lakes.
    """

    for alake, anarray in grouped_df[a_param]:
        plot_obj = anarray.plot(ax=axis,
                                ls='None',
                                marker='o',
                                markersize=10,
                                mfc='None',
                                mew=1.5,
                                markeredgecolor=color_dict[alake],
                                label=alake)
    return plot_obj

# Function four : for quickly generating parameter plots
# def param_plot():
#     '''
#     Parameters
#     -----------
    
    
#     Returns
#     -----------
#     plot_obj : 
#         A plot object.
#     '''
#     for alake in :
#     ax2.plot(lakechem_subset['Ca'],
#          lakechem_subset['ANC'],
#          ls='None',
#          marker='o',
#          markersize=8,
#          mfc='None')