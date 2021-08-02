import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import json
from gensim.utils import simple_preprocess

data = pd.read_csv('file_name.csv')
dataCopy = data
data.head()
data['Tags'].value_counts()
data.Title = data.Title.apply(simple_preprocess, min_len=3)
data.Title.head()
stop_words = set(stopwords.words('english'))


def stemmingandstop(lis):
    lemmatizer = WordNetLemmatizer()
    filtered_lis = [lemmatizer.lemmatize(w) for w in lis if not w in stop_words and len(w) > 2]
    return filtered_lis


data.Title = data.Title.apply(stemmingandstop)
data.Title.head()
type(data.Title)
data.Title = data.Title.apply(' '.join)
data.head()
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])
X = data.Title
y = data.Tags
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
text_clf.fit(X_train, y_train)
predictions = text_clf.predict(X_test)
print(accuracy_score(y_test, predictions))
svm_clftfidf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SVC()),
])
svm_clftfidf.fit(X_train, y_train)
tfsvmpred = svm_clftfidf.predict(X_test)
print(accuracy_score(y_test, tfsvmpred))
text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',
                           alpha=1e-3, random_state=42,
                           max_iter=5, tol=None)),
])
parameters = {
 'vect__ngram_range': [(1, 1), (1, 2)],
 'tfidf__use_idf': (True, False),
 'clf__alpha': (1e-3, 1e-4),
}
gs_clf = GridSearchCV(text_clf, parameters, cv=5, n_jobs=-1)
gs_clf = gs_clf.fit(X_train, y_train)
gs_value = gs_clf.predict(X_test)
print(accuracy_score(y_test, gs_value))

with open('C:/Users/DR281ST/OneDrive - EY/Desktop/Python Output/scholar-vertical-search-engine/scholar_engine/Classification/Final_Cov_Research_Paper.json') as f:
    dataj = json.load(f)
    dataj = [row for row in dataj if not (row['Title'] is None)]
    df = pd.DataFrame(dataj)
    df.head()
    classification = gs_clf.predict(df.Title + df.Abstract)
    df['Tags'] = classification
    df.to_json('C:/Users/DR281ST/OneDrive - EY/Desktop/Final_Cov_Research_Paper_1.json', orient="records")
