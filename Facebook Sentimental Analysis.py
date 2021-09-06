import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file = r'C:\Users\USER\Documents\fb posts.xlsx'
xl = pandas.ExcelFile(file)  # Read from excel
dfs = xl.parse(xl.sheet_names[0])   # Parsing excel sheet to data frame
dfs = list(dfs['Facebook'])   # Removes the blank space from the data frame
print(dfs)
sid = SentimentIntensityAnalyzer()
for data in dfs:
    ss = sid.polarity_scores(data)
    print(data)
    for k in ss:
        print(k, ss[k])
