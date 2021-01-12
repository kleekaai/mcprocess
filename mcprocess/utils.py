import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")


def derive_time_features(df, col):
    """ Extract time features from date time """

    df[col] = pd.to_datetime(df[col], errors="coerce")

    df["year"] = df[col].dt.year
    df["month"] = df[col].dt.month
    df["day"] = df[col].dt.day
    df["hour"] = df[col].dt.hour
    df["minute"] = df[col].dt.minute
    df["dayofyear"] = df[col].dt.dayofyear
    df["week"] = df[col].dt.weekofyear
    df["dayofweek"] = df[col].dt.dayofweek
    df["day_name"] = df[col].dt.day_name()
    df["quarter"] = df[col].dt.quarter
    df["weekday"] = ((df[col].dt.dayofweek) // 5 == 1).astype(float)

    df.drop([col], inplace=True, axis=1)
    return df


def derive_features(df):
    """ Add features: Keyword Count, Keyword list"""
    df = derive_time_features(df, "Date")
    df["KeywordList"] = df.apply(lambda x: x.Keyword.split(";"), axis=1)
    df["KeywordDoc"] = [nlp(text) for text in df.Keyword]
    df["KeywordCount"] = [len(token) for token in df["KeywordDoc"]]
    df["Org"] = df.apply(lambda x: x.Email.split("@")[1].split(".")[0], axis=1)
    return df


def transform_data(df):
    df = derive_time_features(df, "Date")
    df.drop_duplicates(subset="Title Clicked", keep="first", inplace=True)
    df["title_token_count"] = df["Title Clicked"].apply(lambda x: len(x.split(" ")))
    df["KeywordList"] = df.apply(lambda x: x.Keyword.split(";"), axis=1)
    df["KeywordDoc"] = [nlp(text) for text in df.Keyword]
    df["KeywordCount"] = [len(token) for token in df["KeywordDoc"]]
    df["Org"] = df.apply(lambda x: x.Email.split("@")[1].split(".")[0], axis=1)
    return df
