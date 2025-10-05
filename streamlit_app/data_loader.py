import pandas as pd
def load_data():
    
    # =======Loading Data=======
    df = pd.read_csv("imdb_top_1000.csv")
    #   Some cleaning
    # ____Rename columns____
    df.columns = df.columns.str.lower()

    # ____Drop some columns____
    df = df.drop(['poster_link', 'overview'], axis=1)

    df['gross']= df['gross'].replace(',','', regex=True)

    # ____Convert the data type for some columns____
    df['gross'] = pd.to_numeric(df['gross'], errors='coerce')
    df['released_year'] = pd.to_numeric(df['released_year'], errors='coerce')
    df['runtime'] = df['runtime'].replace('min','', regex=True) # to exclude just numbers 
    df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')

    # ____Fill Misaing Data____
    df['certificate'] = df['certificate'].fillna(0)
    df['gross'] = df['gross'].fillna(df['gross'].mean())
    df['meta_score'] = df['meta_score'].fillna(df['meta_score'].mean())
    df['released_year']= df['released_year'].fillna(df['released_year'].mean())

    df['genre'] = df['genre'].str.split(', ') # Modify genre
    df = df.explode('genre')
    return df