from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
data = [
    ("Огромное спасибо, автору за кропотливый труд! Замечательное оформление, детально прорисованные  крупные схемы, очень информативно! Плотная бумага, удобный формат", "Положительный"),
    ("Нужная книга начинающим вязальщикам крючком. Рекомендую.", "Положительный"),
    ("Долгое время занимаюсь вязанием и такие книги отличные помощники. Крючок подзабылся, а книга поможет не только вспомнить, но и вдохновит на новые шедевры!", "Положительный"),
    ("Хорошая книга всё расписано подробно, всё понятно", "Положительный"),
    ("Всё замечательно, информация в книге полезная.", "Положительный"),
    ("Я купила эту книжку как учебное пособие, чтобы связать несложный элемент крючком. Если честно, то представленные схемы не дают нужной информации, вообщем я разочарована", "Отрицательный"),
    ("Дано всего два узора и те без схем, не показано , где можно применить ту или иную схему, не рекомендую к покупке", "Отрицательный"),
    ("Картинки где показано по петлям для меня показались очень мелкими. Пособие неудобно к обучению  ", "Отрицательный"),
    ("Половина страниц оказались залитыми клеем, я разочарована в покупке и буду требовать возврата денег", "Отрицательный"),
    ("Вот я дура, когда моя бабка была жива , могла бы у нее научиться , чем покупать эту бездарную книгу, жалко потраченых 500 рублей", "Отрицательный")
]

texts = [review[0] for review in data]
labels = [review[1] for review in data]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

feature_names = vectorizer.get_feature_names_out()
bow_df = pd.DataFrame(X.toarray(), columns=feature_names)

bow_df['label'] = labels

print(bow_df)