import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import LineCollection

#何倍のalpha
alpha = 0.5

# キャンバス
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor("#f7f3e5")  # 方眼紙っぽい下地色（任意）

# 方眼（薄め）
ax.set_xticks(np.arange(-3, 4, 1))
ax.set_yticks(np.arange(-3, 4, 1))
ax.grid(True, color="#d7d7d7", linewidth=1.0)

# 太い黒線（外枠グリッド3×3を強調）
for x in [-2, 0, 2]:
    ax.axvline(x, color="black", linewidth=2)
for y in [-2, 0, 2]:
    ax.axhline(y, color="black", linewidth=2)

# 対角線
ax.plot([-2, 2], [-2, 2], color="black", linewidth=2)

# 赤い傾いた四角形（ダイヤ形）
red_poly = np.array([[-2, -2], [-2, 0], [0, 2], [2,2], [2, 0], [0, -2]])
ax.plot(*red_poly.T, color="red", linewidth=4)
ax.plot([red_poly[-1,0], red_poly[0,0]], [red_poly[-1,1], red_poly[0,1]], color="red", linewidth=4)

# 緑の多角形（中央の“ひし形プリズム風”）
green_poly = 0.5* red_poly
poly_patch = Polygon(green_poly, closed=True, fill=False, edgecolor="green", linewidth=3, joinstyle="round")
ax.add_patch(poly_patch)

# 緑の頂点を少しだけ可視化
ax.scatter(green_poly[:,0], green_poly[:,1], s=18, color="green")

# 多角形内部の平行斜線（クリップして描画）
# y = x + b の族を用意し、LineCollection を多角形でクリップ
b_vals = np.linspace(-1.0, 0.6, 9)  # 線の本数は調整可
segments = []
x_min, x_max = -1.2, 1.2
for b in b_vals:
    x0, x1 = x_min, x_max
    y0, y1 = x0 + b, x1 + b
    segments.append([(x0, y0), (x1, y1)])

lc = LineCollection(segments, colors="green", linewidths=2)
lc.set_clip_path(poly_patch)     # 多角形でクリップ
ax.add_collection(lc)

# 仕上げ
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-2.6, 2.6)
ax.tick_params(labelbottom=False, labelleft=False)  # 目盛りラベルは非表示
for spine in ax.spines.values():
    spine.set_visible(False)  # 枠線を消す

plt.show()