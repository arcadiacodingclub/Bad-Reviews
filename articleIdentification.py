## Harit Talwar and Jason Agus

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score

df = pd.read_csv('fake-news/train.csv')
conversion_dict = {0: 'Real', 1: 'Fake'}
df ['label'] = df['label'].replace(conversion_dict)
df.label.value_counts()
df
## train and test set eill be necessary for finding relation between text and label, in other words the full text article and its reliability ##

x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size = 0.25, random_state = 7, shuffle=True) 
tfidf_vectorizer = TfidfVectorizer(stop_words = 'english', max_df = 0.75)

vec_train = tfidf_vectorizer.fit_transform(x_train.values.astype('U'))
vec_test = tfidf_vectorizer.transform(x_test.values.astype('U'))

pac = PassiveAggressiveClassifier(max_tier = 50)
pac.fit(vec_train, y_train)

y_pred = pac.predict(vec_test)
score = accuracy_score(y_test, y_pred)
print(f'PAC Accuracy: {round(score*100,2)}%')

confusion_matrix(y_test, y_pred, labels = ['Real', 'Fake'])
X = tfidf_vectorizer.transform(df['text'].values.astype('U'))

scores=  cross_val_score(pac, X, df['label'].values, cv = 5)
print(f'K Fold Accuracy: {round(scores.mean()*100,2)}%')

df_true = pd.read_csv('True.csv')
df_true['label'] = 'Real'
df_true_rep=[df_true['text'][i].replace('WASHINGTON (Reuters) - ','').replace('LONDON (Reuters) - ','').replace('(Reuters) - ','') for i in range(len(df_true['text']))]
df_true['text'] = df_true_rep
df_fake = pd.read_csv('Fake.csv')
df_fake['label'] = 'Fake'
df_final = pd.concat([df_true,df_fake])
df_final = df_final.drop(['subject','date'], axis=1)

def findlabel (newtext) :
    vec_newest = t.fidf_vectorizer.transform([newest])
    y_pred1 = pac.predict(vec_newest)
    return y_pred1[0]

findlabel((df_true['text'][0]))
sum([1 if findlabel((df_true['text'][i])) == 'Real' else 0 for i in range(len(df_true['text']))])/df_true['text'].size
