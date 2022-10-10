import pandas as pd

# Heuristic classifier
# The following is a rule based model to quickly and efficiently classify URLs
def Heuristic_model(urls_df):
    
    heuristic_df = {}
    # Go thru urls and classify them as good or bad
    for url in urls_df["url"]:
        if url[0:5] == "http:":
            if (len(url) > 103) or any(word in url for word in bad_words):
                heuristic_df[url] = 1
            else:
                heuristic_df[url] = 0
        else:
            heuristic_df[url] = 0
    #Turn it into a pandas df
    df1 = pd.DataFrame.from_dict(heuristic_df, orient='index')
    df1 = df1.reset_index()
    df1.columns = ["url", "predicted_label"]
    
    # inner join on the distinct urls to get the true labels
    df1 = pd.merge(urls_df, df1, on=["url", "url"], how="inner")
    
    return df1