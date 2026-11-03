"""v1.5 preregistration figures. NO simulation: only the formula of README Sec. 0 and published v1.3/v1.4 numbers."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------- Figure P1: conversion-hypothesis mimicry of an opening angle (analytic)
PT = 10.0                                            # GeV per leg (illustrative, as in README Sec. 0)
dphi = np.logspace(-1, np.log10(30), 200) * 1e-3     # rad
fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
for B, ls in ((3.8, '-'), (2.0, '--')):
    dw = 2 * 0.3 * B / 1000 / PT                     # |w1|+|w2| [1/mm]
    ax[0].plot(dphi * 1e3, dphi / dw, ls, c='C0', label=f'B = {B} T')
    ax[1].plot(dphi * 1e3, dphi**2 / (2 * dw) * 1e3, ls, c='C3', label=f'B = {B} T')
ax[1].axhline(15, c='gray', lw=1, ls=':'); ax[1].text(0.12, 17, '15 µm pixel hit resolution', color='gray', fontsize=8)
for a in ax:
    a.set_xscale('log'); a.set_yscale('log'); a.set_xlabel(r'transverse opening angle $\Delta\phi$ [mrad]')
    for x in (1, 10):
        a.axvline(x, c='k', lw=0.6, alpha=0.4)
    a.legend(fontsize=8, loc='upper left'); a.grid(alpha=0.25, which='both')
ax[0].set_ylabel(r'vertex shift $s_0=\Delta\phi/\Delta\omega$ [mm]')
ax[0].set_title('(a) vertex shift that absorbs the opening', fontsize=10)
ax[1].set_ylabel(r'remaining mismatch $\Delta\phi^2/(2\Delta\omega)$ [µm]')
ax[1].set_title('(b) mismatch left for the χ² test', fontsize=10)
for a in ax:
    lo, hi = a.get_ylim()
    for x, t in ((1, '≈17 MeV'), (10, '≈200 MeV')):
        a.text(x * 1.08, lo * 1.6, t, fontsize=7, color='k', alpha=0.7)
fig.suptitle(r'Fig. P1 (analytic, no simulation): conversion-hypothesis fit of two tracks with opening $\Delta\phi$, '
             r'$p_T$ = 10 GeV per leg', fontsize=9.5)
plt.tight_layout(); plt.savefig('figP1_mechanism_analytic.png', dpi=160)

# ---------------- Figure P2: preregistered prediction ranges on top of published results
mm = np.array([17, 50, 100, 200])
pub = {'v1.3 mode B (brems-blind)': ([178, 93, 42, 16], 'o-', 'C3'),
       'v1.4 (a) inner 6 hits': ([169, 89, 39, 14], 's-', 'C1'),
       'v1.4 (b) brems-noise fit': ([126, 68, 32, 14], 'D-', 'C0'),
       'no-brems bound (v1.3, exploratory)': ([1.9, 2.0, 1.9, 1.8], 'x-.', 'gray')}
fig, ax = plt.subplots(figsize=(6.4, 4.6))
for lab, (y, mk, c) in pub.items():
    ax.plot(mm, y, mk, c=c, label=lab, ms=5)
# P1: >=100 (and <= v1.4 b by construction); P4: >=34; P2: 5-20; P3: 2-7
bands = [(17, 100, 126, 'P1'), (50, 34, 68, 'P4'), (100, 5, 20, 'P2'), (200, 2, 7, 'P3')]
for i, (x, lo, hi, t) in enumerate(bands):
    ax.fill_between([x * 0.9, x * 1.1], lo, hi, color='C2', alpha=0.35, lw=0,
                    label='v1.5 preregistered range' if i == 0 else None)
    ax.text(x * 1.12, np.sqrt(lo * hi), t, fontsize=8, color='C2', va='center')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xticks(mm); ax.set_xticklabels(['17', '50', '100', '200'])
ax.minorticks_off(); ax.set_ylim(1, 400); ax.set_xlim(13, 280)
ax.set_xlabel(r'$m_a$ [MeV]'); ax.set_ylabel(r'limit degradation from conversions (c$\tau$ = 1 mm)')
ax.legend(fontsize=7, loc='lower left'); ax.grid(alpha=0.25)
ax.set_title('Fig. P2: preregistered v1.5 ranges vs. published v1.3/v1.4 results\n'
             '(v1.5 cannot exceed v1.4 (b) by construction; no v1.5 result shown)', fontsize=9)
plt.tight_layout(); plt.savefig('figP2_predictions_vs_published.png', dpi=160)
print('ok')
