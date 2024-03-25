import streamlit as st
import numpy as np
import pandas as pd
import re
# import seaborn as sns

# def getString(text):


def preprocess(data):
  # Define a regular expression pattern to extract date, user, and message
  pattern = r'^(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}\s*[ap]m) - ([^:]+): (.*)$'

  #defining the lists to create the dataframe
  date = []
  time = []
  user = []
  message = []

  for text in data:
    # Use regular expression to match the pattern and extract date, user, and message
    match = re.match(pattern, text)
    if match:
      date_ = match.group(1)
      time_ = match.group(2)
      user_ = match.group(3)
      message_ = match.group(4)

      date.append(date_)
      time.append(time_)
      user.append(user_)
      message.append(message_)

  df = pd.DataFrame({
      'Date': date,
      'Time': time,
      'User': user,
      'Message': message
  })

  #date preprocessing
  df['Only Date'] = pd.to_datetime(df['Date']).dt.date
  df['Year'] = pd.to_datetime(df['Date']).dt.year
  df['Month_num'] = pd.to_datetime(df['Date']).dt.month
  df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
  df['Day'] = pd.to_datetime(df['Date']).dt.day
  df['Day_name'] = pd.to_datetime(df['Date']).dt.day_name()

  #time preprocessing
  df['Hour'] = pd.to_datetime(df['Time']).dt.hour
  df['Minute'] = pd.to_datetime(df['Time']).dt.minute

  return df
