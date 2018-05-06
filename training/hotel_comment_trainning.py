# -*- coding: utf-8 -*-
import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib



def make_label(df):
    df["sentiment"]=df["rank"]
    
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


df = pd.read_csv('fengwo_hotel_comment.csv', encoding='utf-8')

make_label(df)

X=df[['comment']]
y=df.sentiment


X['cutted_comment']=X.comment.apply(chinese_word_cut)

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=1)


max_df=0.8 #在超过这一比例的文档中出现的关键词过于平凡，去除掉
min_df=3 #在低于这一数量的文档中出现的关键词过于独特，去除掉

vect = TfidfVectorizer(max_df=max_df, min_df=min_df, token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b')
term_matrix = pd.DataFrame(vect.fit_transform(X_train.cutted_comment).toarray(), columns=vect.get_feature_names())

nb=MultinomialNB()
pipe = make_pipeline(vect,nb) 

pipe.fit(X_train.cutted_comment, y_train)
y_pred=pipe.predict(X_test.cutted_comment)


joblib.dump(pipe, "hotel_comment.pkl")
