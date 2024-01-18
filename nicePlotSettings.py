import matplotlib.pyplot as plt
from matplotlib import cm

evenly_spaced_interval = np.linspace(0, 1, 10)
colors = [cm.viridis(x) for x in evenly_spaced_interval]

fig, ax = plt.subplots(1,1, figsize=(7,4), sharex=False) #the size is in inches and the final figure has not exactly the dimension set in figsize
    
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Times New Roman",
    'font.size': 12
})

plt.rcParams["axes.linewidth"] = 1

ax.plot(xData,yData,color = colors[0], alpha = 1,lw = 4, label = "text")
ax.set(xlabel='text')
ax.set(ylabel='text')
ax.grid(alpha = 0.4)
ax.legend(loc = 'lower right')
ax.set(title = "")

ax.text(xLocation, yLocation, "text", fontsize=20)
ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

plt.xlim(minX,maxX)
plt.ylim(minY,maxY)
fig.tight_layout()
fig.subplots_adjust(hspace=0.1)

plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")
