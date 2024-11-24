from urlextract import URLExtract
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

import emoji

extract = URLExtract()


#fetching the stats
def fetchstats(selected_user, df):
  #if the selected user is a specified user, then make changes in the dataframe, else do not
  if selected_user != "Overall":
    df = df[df['User'] == selected_user]

  num_messages = df.shape[0]
  words = []
  for message in df['Message']:
    words.extend(message.split())

  #counting the number of media files shared
  mediaomitted = df[df['Message'] == '<Media omitted>']

  #links shared
  links = []
  for message in df['Message']:
    links.extend(extract.find_urls(message))

  return num_messages, len(words), mediaomitted.shape[0], len(links)


#most busy users {group level}
def fetchbusyuser(df):
  count = df['User'].value_counts().head()

  newdf = pd.DataFrame((df['User'].value_counts() / df.shape[0]) * 100)
  return count, newdf


#creating word cloud
def createwordcloud(selected_user, df):
  file = open('stop_hinglish.txt')
  stopwords = file.read()
  stopwords = stopwords.split('\n')

  if selected_user != 'Overall':
    df = df[df['User'] == selected_user]

  wc = WordCloud(width=500,
                 height=500,
                 min_font_size=10,
                 background_color='white')

  df_wc = wc.generate(df['Message'].str.cat(sep=" "))
  return df_wc


#most common words
def getcommonwords(selected_user, df):

  #getting the stopwords

  file = open('stop_hinglish.txt')
  stopwords = file.read()
  stopwords = stopwords.split('\n')

  if selected_user != 'Overall':
    df = df[df['User'] == selected_user]

  temp = df[df['User'] != '<Media omitted>']

  words = []

  for message in df['Message']:
    for word in message.lower().split():
      if word not in stopwords:
        words.append(word)

  mostcommon = pd.DataFrame(Counter(words).most_common(20))
  return mostcommon


def getemojistats(selected_user, df):
  if selected_user != 'Overall':
    df = df[df['User'] == selected_user]

  emojis = []
  for message in df['Message']:
    emojis.extend(c for c in message if c in emoji.UNICODE_EMOJI['en'])

  emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
  return emoji_df


def monthtimeline(selected_user, df):
  if selected_user != 'Overall':
    df = df[df['User'] == selected_user]

  temp = df.groupby(['Year', 'Month_num',
                     'Month']).count()['Message'].reset_index()

  time = []
  for i in range(temp.shape[0]):
    time.append(temp['Month'][i] + "-" + str(temp['Year'][i]))

  temp['Time'] = time
  return temp


def weekactivitymap(selected_user, df):
  if selected_user != 'Overall':
    df = df[df['User'] == selected_user]

  return df['Day_name'].value_counts()
