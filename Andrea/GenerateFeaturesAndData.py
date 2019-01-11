import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.stats import norm
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
sns.set()
from collections import Counter

color_palette = sns.color_palette("Set1", n_colors=5)
cmap = ListedColormap(sns.color_palette("Set1", n_colors=5).as_hex())

x = np.arange(0,10,1)
f1 = np.zeros(10)
f2 = f1.copy() 
f3 = f1.copy() 
f4 = f1.copy() 
f5 = f1.copy() 

f1[[1,3]] = 1
f2[[4,5]] = 1
f3[[5,8]] = 1
f4[[6,7]] = 1
f5[[1,9]] = 1
feats = np.array([f1,f2,f3,f4,f5])

angles = [n / float(len(x)) * 2 * np.pi for n in range(len(x))]
features = ['f-{}'.format(f) for f in range(len(x))]

ax = plt.subplot(111, polar=True)
plt.yticks([],[])
plt.xticks(angles, features, color='grey',size=8)

ax.plot(angles, f1)
ax.plot(angles, f2)
ax.plot(angles, f3)
ax.plot(angles, f4)
ax.plot(angles, f5)

ax.fill(angles, f1, alpha=0.1)
ax.fill(angles, f2, alpha=0.1)
ax.fill(angles, f3, alpha=0.1)
ax.fill(angles, f4, alpha=0.1)
ax.fill(angles, f5, alpha=0.1)

plt.show()

angles += angles[:1]
np.random.seed(42)
fake_data = np.random.rand(10,10)
ax = plt.subplot(111, polar=True)
plt.yticks([],[])
plt.xticks(angles, features, color='grey',size=8)
for i in range(5):
	ax.plot(angles, np.append(fake_data[i],fake_data[i,-1]))
	ax.fill(angles, np.append(fake_data[i],fake_data[i,-1]), alpha=0.1)
plt.show()

pca = PCA(n_components=2)
fake_data_X = pca.fit_transform(fake_data)
feats_X = pca.transform(feats)

plt.scatter(fake_data_X[:,0], fake_data_X[:,1])
plt.scatter(feats_X[:,0], feats_X[:,1], c=range(5), s=100)
plt.show()

colors = np.zeros(len(fake_data))
scores = np.zeros(len(fake_data))
eachScore = []
for item_idx, item in enumerate(fake_data):
	best_feat_idx = 0
	best_feat_score = 0
	tempScore = []
	for feat_idx, feat in enumerate(feats):
		feat_score = np.dot(feat, item)
		if feat_score > best_feat_score:
			best_feat_score = feat_score
			best_feat_idx = feat_idx
		print (feat_score)
		tempScore.append(feat_score)
	print (tempScore)
	colors[item_idx] = int(best_feat_idx)
	scores[item_idx] = best_feat_score
	eachScore.append(tempScore)

colors = list(map(int, colors))

plt.scatter(fake_data_X[:,0], fake_data_X[:,1], c=colors)
plt.scatter(feats_X[:,0], feats_X[:,1], c=range(5), s=100)
plt.show()

# fix the color map so it follows the 5 features used
ax = plt.subplot(111, polar=True)
plt.yticks([],[])
plt.xticks(angles, features, color='grey',size=8)
for idx in range(5):
	c = cmap(colors[idx]) 
	ax.scatter(angles, np.append(fake_data[idx],fake_data[idx,-1]),c=c, cmap=cmap)
	ax.fill(angles, np.append(fake_data[idx],fake_data[idx,-1]), alpha=0.1)
plt.show()

fig, ax = plt.subplots(len(feats),1, sharex=True)
for feat_idx, feat in enumerate(feats):
	ax[feat_idx].plot(feat, c=color_palette[feat_idx], linestyle='--')

for idx, (item, color) in enumerate(zip(fake_data, colors)):
	ax[color].plot(range(len(item)),item, c=color_palette[color], alpha=0.01)
plt.show()

print (Counter(colors))

plt.hist(scores, bins=25)
plt.show()

fig, ax = plt.subplots(len(fake_data))
for idx, item in enumerate(eachScore):
	ax[idx].bar(range(len(item)),len(item))

plt.show()
	
