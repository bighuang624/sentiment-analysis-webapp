# coding=UTF-8
import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib

def make_label(df):
    df['sentiment'] = df['star']
    # df['sentiment'] = df['star'].apply(lambda x: 1 if x > 3 else 0)

def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))

df = pd.read_csv('./restaurant-comment.csv', encoding='gb18030')
make_label(df)

X = df[['comment']]
y = df.sentiment

X['cutted_comment'] = X.comment.apply(chinese_word_cut)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

max_df = 0.8  # 在超过这一比例的文档中出现的关键词（过于平凡），去除掉。
min_df = 3  # 在低于这一数量的文档中出现的关键词（过于独特），去除掉。

vect = CountVectorizer(max_df = max_df, 
                       min_df = min_df, 
                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b')

term_matrix = pd.DataFrame(vect.fit_transform(X_train.cutted_comment).toarray(), columns=vect.get_feature_names())

nb = MultinomialNB()
pipe = make_pipeline(vect, nb)
pipe.fit(X_train.cutted_comment, y_train)

joblib.dump(pipe, 'restaurant_comment.pkl')

# print(pipe.predict(X_test.cutted_comment))
# result = pipe.predict(['菜品丰富', '价格有点小贵', '品种很多，味道不错，还会再来', '卫生很差', '说真的，不晓得有人排队的理由，香精香精香精香精，拜拜！'])
# print(result)
