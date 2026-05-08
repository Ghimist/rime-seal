import pandas as pd

# 讀取數據（假設你的數據是 tab 分隔或空格分隔）
# 如果是剪貼板數據，可以直接用 pd.read_clipboard(sep='\s+', header=None)
df = pd.read_csv('n5344R2-SmallSealProposal_SealSources.txt', sep='\t', header=None, names=['Unicode', 'Source', 'Value'], encoding='utf-8', comment='#')
# df = pd.read_clipboard(sep='\s+', header=None, names=['Unicode', 'Source', 'Value'])

# 進行透視
pivot_df = df.pivot_table(index='Unicode', columns='Source', values='Value', aggfunc=lambda x: '、'.join(x.astype(str)))

# 檢查 (Unicode, Source) 組合是否有緟複
dup_mask = df.duplicated(subset=['Unicode', 'Source'], keep=False)
print(f"緟複的組合數量：{dup_mask.sum()}")
print(df[dup_mask].sort_values(['Unicode', 'Source']))

# 導出結果
pivot_df.to_csv('n5344R2-aL-result.csv')
print(pivot_df)