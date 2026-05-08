import pandas as pd

# 讀取數據（假設你的數據是 tab 分隔或空格分隔）
# 如果是剪貼板數據，可以直接用 pd.read_clipboard(sep='\s+', header=None)
df = pd.read_csv('n5344R2-SmallSealProposal_SealSources.txt', sep='\t', header=None, names=['Unicode', 'Source', 'Value'], encoding='utf-8', comment='#')

# 進行透視
pivot_df = df.pivot(index='Unicode', columns='Source', values='Value')

# 導出結果
pivot_df.to_csv('n5344R2-result.csv')
print(pivot_df)