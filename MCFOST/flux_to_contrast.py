"""
Takes a MCFOST output file and converts the disc from flux units to
contrast units by reading the value of the central pixel (the star) from
the total intensity image and divides the whole image by that single value

Saves the result as a new .fits file
"""

import numpy as np
from astropy.io import fits

# input and load model
mcfost_file = 'RT.fits'
mcfost_data = fits.getdata(mcfost_file)

# pull out total intensity image
i_total = mcfost_data[0,0,0]

ny, nx, = i_total.shape
yc, xc = ny // 2, nx // 2
star_value = i_total[yc,xc]

print(f'Star flux: {star_value:.6e}')

# divide whole image by star's flux to get contrast
contrast_image = i_total / star_value

print(f'Contrast image max: {np.nanmax(contrast_image):.4e}') # Should be 1.0 at the star

# save as .fits file
hdu = fits.PrimaryHDU(contrast_image)
hdu.header['BUNIT'] = 'contrast'
hdu.header['NORMTYPE'] = 'central pixel'
hdu.header['STARFLUX'] = star_value
hdu.writeto('RT_contrast.fits', overwrite=True)
print(f'Saved contrast image as RT_contrast.fits')
