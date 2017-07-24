import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns

sns.set_context("notebook", font_scale = 1.2)
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})


#pickle = hi_res_wlgrid, hi_res_-2sigma, hi_res_-1sigma, hi_res_median, hi_res_+1sigma, hi_res+2sigma, data_wl_grid, raw_data, data_err, median_binned_model

d= np.genfromtxt("w107_spectrum_06-22-17.txt")
plt.errorbar(d[:,0], d[:,1]*100., d[:,2]*100., linestyle = 'none', zorder = 100, marker = 'o', color = 'w', markeredgecolor = 'k', ecolor ='k', markeredgewidth = 1.3)


p = pickle.load(open("WASP107b_Global_Cloud_limit_Metallicity_spectra.pic", "rb"))
w = p[0]

plt.fill_between(w, p[1], p[5], color = "navy", alpha = '0.2')
plt.fill_between(w, p[2], p[4], color = "navy", alpha = '0.3')
plt.plot(w, p[3], color = 'navy', label = "Best fit model")


"""d = pickle.load(open("Model_Solar.pic", "rb"))
x, y = d[0], d[1]*100. - 0.7
plt.plot(x, y, color = '0.5', alpha = 0.5, label = "1X solar, cloud-free", zorder = -20) 
plt.legend(loc= 'upper right')"""

plt.ylabel("Transit depth (%)")
plt.ylim(2.03, 2.1)
plt.xlabel("Wavelength (microns)")

x2 = plt.gca().twinx()
scaleheight = 460./1.e6*100.
plt.plot(w,p[3]/scaleheight - np.min(p[3]/scaleheight), linewidth=0.)

plt.ylabel("Scale heights")
plt.xlim(1, 1.8)



plt.tight_layout()
plt.savefig("spectrum.pdf")
plt.show()
