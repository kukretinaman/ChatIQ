import re
import pandas as pd


def preprocess(data):
  pattern1 = r'^(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}\s*[APap][Mm]) - ([^:]+): (.+)$'
  pattern2 = r'^\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2}\s*[APap][Mm])\] ([^:]+): (.+)$'

  date = []
  time = []
  user = []
  message = []
  unmatched_lines = []

  for text in data:
    match1 = re.match(pattern1, text)
    match2 = re.match(pattern2, text)

    if match1:
      date.append(match1.group(1))
      time.append(match1.group(2))
      user.append(match1.group(3))
      message.append(match1.group(4))
    elif match2:
      date.append(match2.group(1))
      time.append(match2.group(2))
      user.append(match2.group(3))
      message.append(match2.group(4))
    else:
      unmatched_lines.append(text)

  # print("Unmatched Lines:", unmatched_lines[:10])  # Log unmatched lines

  if not date:
    # print("No messages matched the patterns.")
    return None

  df = pd.DataFrame({
      'Date': date,
      'Time': time,
      'User': user,
      'Message': message
  })
  df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'],
                                  errors='coerce')

  # Date components
  df['Only Date'] = df['DateTime'].dt.date
  df['Year'] = df['DateTime'].dt.year
  df['Month_num'] = df['DateTime'].dt.month
  df['Month'] = df['DateTime'].dt.month_name()
  df['Day'] = df['DateTime'].dt.day
  df['Day_name'] = df['DateTime'].dt.day_name()

  # Time components
  df['Hour'] = df['DateTime'].dt.hour
  df['Minute'] = df['DateTime'].dt.minute

  df = df.dropna(subset=['DateTime'])  # Drop rows with invalid DateTime

  # print("Final DataFrame:", df.head())  # Log the resulting DataFrame
  return df
