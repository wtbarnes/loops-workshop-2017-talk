import matplotlib.pyplot as plt
import seaborn.apionly as sns
import numpy as np

#sns.set_style('white')

# list reported slopes and ranges
observed_slopes = []
observed_slopes.append(('Warren et al. (2012)',[3.26]))
observed_slopes.append(('Warren et al. (2012)',[2.17,3.26]))
observed_slopes.append(('Winebarger et al. (2012)',[3.2]))
observed_slopes.append(('Tripathi et al. (2011)',[[2.08,2.47],[2.05,2.7]]))
observed_slopes.append(('Mulu-Moore et al. (2011)',[[1.6,2],[2,2.3]]))
observed_slopes.append(('Warren et al. (2012)',[[1.7,4.5]]))
observed_slopes.append(('Schmelz and Pathak (2012)',[[1.91,5.17]]))
# add bradshaw, reep, and cargill results
# add color depending on theory or observation

offset=0.1
# setup figure
fig = plt.figure(figsize=(6,9))
ax = fig.gca()
# plot points
for i,slope in enumerate(observed_slopes):
    ax.text(-1.3,i,slope[0],rotation=-13)
    for j,a in enumerate(slope[1]):
        if type(a) == list:
            ax.errorbar(np.array(a).mean(),j*offset + i,
                        color='k',ls='-',marker='',capsize=15,
                        xerr=np.fabs(np.array(a).reshape((2,1)) - np.array(a).mean()))
            #ax.plot(a,j*offset+np.array([i,i]),color='k',ls='-',marker='')
        else:
            ax.plot(a,i,color='k',ls='',marker='o')

# set limits
ax.set_xlim([0,6])
ax.set_ylim([-1,len(observed_slopes)])
# set labels
ax.set_xlabel(r'$a$')
new_x_lab = [int(lab) if 1<=int(lab)<=5 else '' for lab in ax.get_xticks().tolist()]
ax.set_xticklabels(new_x_lab)
ax.set_yticklabels([])
ax.set_yticks([])

sns.despine(left=True)

fig.savefig('../loops-workshop-2017-talk/template/img/reported_slopes.png',dpi=200,bbox_inches='tight')
