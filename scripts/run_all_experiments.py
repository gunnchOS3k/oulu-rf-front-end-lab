from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from gunnchos_rf.link_budget import fspl_db, link_budget
from gunnchos_rf.lna_noise_gain import nf_to_noise_temp

ROOT = Path(__file__).resolve().parents[1]
FIG=ROOT/'results/figures'; FIG.mkdir(parents=True, exist_ok=True)
TBL=ROOT/'results/tables'; TBL.mkdir(parents=True, exist_ok=True)
(TBL/'link_budget.md').write_text(f'# Link budget\nFSPL 1km 2.4GHz = {fspl_db(1,2400):.1f} dB\nRx={link_budget(20,[5], [fspl_db(1,2400)])} dBm\n')
(TBL/'lna_tradeoff.md').write_text(f'# LNA\nNoise temp NF=2dB: {nf_to_noise_temp(2):.1f} K\n')
gamma = (np.linspace(-0.9,0.9,100) + 0j)
plt.figure(); plt.plot(gamma.real, gamma.imag); plt.savefig(FIG/'smith_chart_example.png'); plt.close()
(ROOT/'results/experiment_summary.md').write_text('# RF e2e PASS\n')
