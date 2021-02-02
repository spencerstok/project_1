import pandas as pd

df = pd.read_csv("reddit_data_full.csv")

stock_list = ["KODK", "AMC", "GME", "BB"]

for ticker in stock_list:
    stock_df = df[df['body'].str.contains(str(ticker), case=False)]

    stock_df.to_csv("stock_dfs/"+ticker+".csv")
    

    
