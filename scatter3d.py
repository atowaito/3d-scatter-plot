import pandas as pd
import plotly.graph_objects as go
import re

# RGB値を取得する関数
def get_color(x, y, z):
    r = int((x / 10) * 255) if x <= 10 else 255
    g = int((y / 10) * 255) if y <= 10 else 255
    b = int((z / 10) * 255) if z <= 10 else 255

    # ビビッドにするために、色の強度を強調
    r = min(255, int(r * 1.2))
    g = min(255, int(g * 1.2))
    b = min(255, int(b * 1.2))
    
    return f'rgb({r},{g},{b})'

# データを読み込んでパースする関数
def parse_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'(.+)\((.+),(.+),(.+)\)', line.strip())
            if match:
                name = match.group(1)
                x = float(match.group(2))
                y = float(match.group(3))
                z = float(match.group(4))
                data.append([name, x, y, z])
    return pd.DataFrame(data, columns=['name', 'x', 'y', 'z'])

# ファイルからデータを読み込む
data_file = 'data/data001.txt'  # ファイル名を指定してください
data = parse_data(data_file)

# 3Dグラフを作成する
fig = go.Figure()

# 各データポイントに球とラベルを追加する
for _, row in data.iterrows():
    color = get_color(row['x'], row['y'], row['z'])
    fig.add_trace(go.Scatter3d(
        x=[row['x']],
        y=[row['y']],
        z=[row['z']],
        mode='markers+text',
        marker=dict(size=5, color=color),
        text=row['name'],
        textposition='top center'
    ))

# グラフのレイアウトを設定する
fig.update_layout(
    scene=dict(
        xaxis_title='Horizontal',
        yaxis_title='Vertical',
        zaxis_title='Height'
        
    ),
    title='3D Scatter Plot with Labels'
)

# グラフを表示する
fig.show()
