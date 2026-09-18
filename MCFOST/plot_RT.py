import pymcfost as mcfost
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cm

if not hasattr(cm, 'get_cmap'):
    def get_cmap(name=None, lut=None):
        return matplotlib.colormaps[name] if name is not None else matplotlib.colormaps['viridis']
    cm.get_cmap = get_cmap

# Image of MCFOST disc
image = mcfost.Image('/home/wh418/mcfost/pds70/data_3.8/')

# Find peak flux first
vmax = image.image[0, 0, 0, :, :].max()
vmin = vmax * 1e-11   

fig, ax = plt.subplots(figsize=(6,6))
image.plot(
    i=0,
    iaz=0,
    ax=ax,
    colorbar=True,
    axes_unit='arcsec',
    scale='log',
    vmin=vmin,
    vmax=vmax,
    cmap='inferno',
    limits=[-1.1, 1.1, -1.1, 1.1]
)
plt.savefig("disc_image.png", dpi=150, bbox_inches='tight')
plt.close()

# SED
sed = mcfost.SED('/home/wh418/mcfost/pds70/data_th/')

fig, ax = plt.subplots(figsize=(8,5))
sed.plot(i=0, color='blue')
plt.savefig("sed.png", dpi=150, bbox_inches='tight')
plt.close()

# Temperature structure
fig, ax = plt.subplots(figsize=(8,5))
sed.plot_T(log=True)
plt.savefig("temperature.png", dpi=150, bbox_inches='tight')
plt.close()
