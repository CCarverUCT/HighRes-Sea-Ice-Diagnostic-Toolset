#### NetCDF Monthly Dataset Combiner ####
# Cameron Carver Sept - 2024
# University of Cape Town - Applied Ocean Science MSc

import glob
import xarray as xr
# Define path to directory that contains all netCDF files to be combined
data_dir = glob.glob('/Data-Obs/G02202_V4_south_monthly/*.nc')

datasets = []
for file_path in data_dir:
    obs_ds = xr.open_dataset(file_path)
    datasets.append(obs_ds)
    
combined = xr.concat(datasets, dim='tdim')
combined = combined.assign_coords(tdim=combined['time'], x=combined['xgrid'], y=combined['ygrid'])
combined = combined.sortby('tdim')
siconc = combined['cdr_seaice_conc_monthly']/2.55*100 # Convert siconc to a percentage
combined['siconc'] = siconc

combined.to_netcdf('seaice_conc_monthly_sh_n07_v04r00_all.nc') #Desired name of combined file
print(combined)
