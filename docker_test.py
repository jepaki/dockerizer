import sys
import numpy as np
import rasterio as rio
from pathlib import Path


def read_raster(raster_file):
    raster_path = Path(raster_file)

    if not raster_path.exists():
        print("Input raster path does not exist! ", raster_path)

    print("Opening raster: ", raster_path)
    ds = rio.open(raster_path)
    print("Meta:\n", ds.meta)
    ds.close()


if __name__ == '__main__':
    print("Name of script: ", sys.argv[0])
    read_raster(sys.argv[1])
