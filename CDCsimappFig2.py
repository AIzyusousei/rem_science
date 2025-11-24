import matplotlib.pyplot as plt
import numpy as np

# ---- 座標設定 ----
A = np.array([0, 0])
B = np.array([2, 0])
C = np.array([2.5, 1])
D = np.array([1, 2])

# ポリゴン
poly = np.array([A, B, C, D])

# ---- 図の準備 ----
fig, ax = plt.subplots(figsize=(6,6))

# ---- 灰色の塗りつぶし（奥に） ----
ax.fill(poly[:,0], poly[:,1], color='gray', alpha=0.3, zorder=1)

# ---- 各辺を描画 ----
ax.plot([A[0], B[0]], [A[1], B[1]], color='green', linewidth=8, zorder=2)
ax.plot([B[0], C[0]], [B[1], C[1]], color='blue', linewidth=8, zorder=2)
ax.plot([C[0], D[0]], [C[1], D[1]], color='purple', linewidth=8, zorder=2)
ax.plot([D[0], A[0]], [D[1], A[1]], color='red', linewidth=8, zorder=2)

# 内部のオレンジ線
ax.plot([D[0], B[0]], [D[1], B[1]], color='orange', linewidth=5, zorder=3)

# 破線（A → C）
ax.plot([A[0], C[0]], [A[1], C[1]], 'k--', linewidth=2, zorder=2)

# ---- 頂点（最前面） ----
for p in [A, B, C, D]:
    ax.scatter(p[0], p[1], s=150, color='black', zorder=10)

# ---- 比率固定 ----
ax.set_aspect('equal')

# 🚫 格子線削除
ax.grid(False)

plt.show()