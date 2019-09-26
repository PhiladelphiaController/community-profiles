import carto2gpd
import geopandas as gpd
from . import EPSG
from .core import Dataset, geocode, replace_missing_geometries
from .regions import *

__all__ = [
    "StreetTree",
    "TreeCanopyOutline",
    "TreeCanopyPoint",
]


class StreetTree(Dataset):
    """
    Street Tree Inventory: locations of all street trees.
    Snapshot in time from 2016
    
    Source
    ------
    http://data.phl.opendata.arcgis.com/datasets/957f032f9c874327a1ad800abd887d17_0.zip
    """
    
    @classmethod
    def download(cls, **kwargs):

        url = "http://data.phl.opendata.arcgis.com/datasets/957f032f9c874327a1ad800abd887d17_0.zip"
        df = gpd.read_file(url)

        return (
            df.to_crs(epsg=EPSG) 
            .pipe(geocode, ZIPCodes.get())
            .pipe(geocode, Neighborhoods.get())
            .pipe(geocode, PUMAs.get())
        )

    
class TreeCanopyOutline(Dataset):
    """
    Tree canopy outlines generated by Intergraph Government Solutions (IGS) for trees >6' diameter. 
    Update generated off the 2015 Leaf-Off 3" AccuPLUS Imagery representing changes in tree canopy visible within the imagery. 
    
    Source
    ------
    https://www.opendataphilly.org/dataset/ppr-tree-canopy
    """
    
    @classmethod
    def download(cls, **kwargs):

        url = "https://phl.carto.com/api/v2/sql"
        gdf = carto2gpd.get(url, "ppr_tree_canopy_outlines_2015")  ### connection terminated when I try 

        return (
            gdf.to_crs(epsg=EPSG) 
            .pipe(geocode, ZIPCodes.get())
            .pipe(geocode, Neighborhoods.get())
            .pipe(geocode, PUMAs.get())
        )

    
class TreeCanopyPoint(Dataset):
    """
    Tree canopy points generated by Intergraph Government Solutions (IGS) for trees >6' diameter. 
    Update generated off the 2015 Leaf-Off 3" AccuPLUS Imagery representing changes in tree canopy visible within the imagery. 
    
    Source
    ------
    https://www.opendataphilly.org/dataset/ppr-tree-canopy
    """
    
    @classmethod
    def download(cls, **kwargs):

        url = "https://phl.carto.com/api/v2/sql"
        gdf = carto2gpd.get(url, "ppr_tree_canopy_points_2015")

        return (
           gdf.to_crs(epsg=EPSG) 
            .pipe(geocode, ZIPCodes.get())
            .pipe(geocode, Neighborhoods.get())
            .pipe(geocode, PUMAs.get())
        )    
        
    