# -*- coding: utf-8 -*-

"""
@autor: PC Elian
"""

import emodeconnection as emc
import numpy as np
import pandas as pd
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from matplotlib import rc as mplrc


data = emc.get(variable='sweep_data', simulation_name='dispersionSiN')

vals = np.array(data['values'])           # longitudes de onda (nm)
neff = np.array(data['effective_index'])  # puede ser (N,) o (N, num_modes)

if vals.ndim > 1:
    vals = vals.ravel()

if neff.ndim == 2:
    neff = neff[:, 0]     
elif neff.ndim > 2:
    neff = neff.reshape(-1)


ind = np.argsort(vals)
wav_nm_raw = vals[ind]    # [nm]
neff_raw   = neff[ind]

print("λ(min), λ(max) =", wav_nm_raw.min(), wav_nm_raw.max(), "nm")

df = pd.DataFrame({'lambda_nm': wav_nm_raw, 'neff': neff_raw})
df.to_csv('FH_modes_raw.csv', index=False)
print("Saved FH_modes_raw.csv with", len(df), "points.")

n_eff_spl = UnivariateSpline(wav_nm_raw, neff_raw, s=0, k=4)
n_eff_spl_2d = n_eff_spl.derivative(n=2)

lam_min = 1520.0
lam_max = 1600.0
wav_nm_fit = np.linspace(lam_min, lam_max, 200)  # [nm]

# GVD: D = -(λ/c) d²n_eff/dλ²  -> ps/(nm·km)
D = -wav_nm_fit/3e8 * n_eff_spl_2d(wav_nm_fit) * 1e12 / 1e-3  # [ps/nm/km]

fw, LW = 8/2.54, 0.5
mplrc('font', **{'family': 'sans-serif', 'size': 7})
mplrc('axes', linewidth=LW, axisbelow=True)
mplrc('xtick', bottom=True, top=True, direction='in')
mplrc('ytick', left=True, right=True, direction='in')
mplrc('xtick.major', size=3, width=LW)
mplrc('xtick.minor', size=1.5, width=LW)
mplrc('ytick.major', size=3, width=LW)
mplrc('figure', figsize=[fw, fw/2**0.5])

fig, ax = plt.subplots(1, 1)

ax.set_xlabel(u'Wavelength (\u03bcm)')
ax.set_ylabel('GVD (ps/nm/km)', color='tab:blue')

ax2 = ax.twinx()
ax2.set_ylabel('Effective index', color='tab:red')

ax.grid(visible=True, which='major', axis='both',
        linewidth=LW/2, color='grey', alpha=0.25)

ax.plot(wav_nm_fit, D,
        color='tab:blue', linestyle='-',
        lw=LW*1.5)

ax2.plot(wav_nm_fit, n_eff_spl(wav_nm_fit),
         color='tab:red', linestyle='--',
         lw=LW*1.5)

ax2.plot(wav_nm_raw, neff_raw,
         color='tab:red', marker='o', linestyle=':',
         lw=LW, ms=2.0, mec='k', mew=0.2)

ax.set_xlim([lam_min, lam_max])

xticks_nm = np.array([1520, 1540, 1560, 1580, 1600])
ax.set_xticks(xticks_nm)
ax.set_xticklabels(['%.3f' % (x*1e-3) for x in xticks_nm])

ax.set_ylim([0, 400])
ax2.set_ylim([
    np.min(neff_raw)*0.98,
    np.max(neff_raw)*1.02
])

ax3 = ax.twiny()
ax3.set_xlim(ax.get_xlim())
ax3.set_xlabel('Frequency (THz)')
ax3.set_xticks(xticks_nm)
ax3.set_xticklabels(['%0.1f' % (3e8/x*1e-3) for x in xticks_nm])

ax.set_zorder(ax2.get_zorder() + 1)
ax.patch.set_visible(False)

fig.savefig('dispersionSiN_1520_1600.png', dpi=600, bbox_inches='tight')
print("Saved dispersionSiN_1520_1600.png")

