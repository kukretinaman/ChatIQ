import streamlit as st
import preprocess
import re
import stats
import matplotlib.pyplot as plt
import numpy as np

st.sidebar.title("ChatIQ")

#this is for uploadin a file
uploaded_file = st.sidebar.file_uploader("Choose a file")

st.markdown("""
## Extracting WhatsApp Chat
To extract a WhatsApp chat from any group chat or individual chat, follow these steps:

1. Open WhatsApp on mobile and navigate to the chat you want to extract.
2. Tap on the three dots in the top-right corner to open the menu.
3. Select "More" and then "Export chat".
4. Choose not to include media file.
5. Select the method of sharing (e.g., email, Google Drive, etc.) and send the chat to yourself.
6. Once received, download the chat file to your computer.
7. Upload the chat file to ChatIQ for analysis.
""")

if uploaded_file is not None:
  bytes_data = uploaded_file.read()

  #conveting the bytecode t the textfile
  data = bytes_data.decode("utf-8")
  data = data.split('\n')

  #sending the file data to the preprocess function for   the further functioning
  df = preprocess.preprocess(data)

  #fetch unique users
  user_list = df['User'].unique().tolist()

  #organizing things
  user_list.sort()

  #including overall, this will be resonsible for showcasing the overall chat group analysis
  user_list.insert(0, "Overall")

  selected_user = st.sidebar.selectbox("Show Analysis with respect to",
                                       user_list)

  st.title("Whatsapp chat analysis for " + selected_user)
  if st.sidebar.button("Show Analysis"):

    #getting the stats of the user from the stats script

    num_messages, num_words, media_omitted, links = stats.fetchstats(
        selected_user, df)

    #first phase is to showcase the basic stats like number of users, number of messages, number of media shared etc.
    col1, col2, col3, col4 = st.columns(4)

    with col1:
      st.header("Total Messages")
      st.title(num_messages)

    with col2:
      st.header("Total No. of Words")
      st.title(num_words)

    with col3:
      st.header("Media Omitted")
      st.title(media_omitted)

    with col4:
      st.header("Total Links Shared")
      st.title(links)

    #finding the busiest users in the group
    if selected_user == 'Overall':
      #dividing the space into two columns
      #first col is the bar chart and the second column is the dataframe
      st.title('Most Busy Users')
      busycount, newdf = stats.fetchbusyuser(df)
      fig, ax = plt.subplots()
      col1, col2 = st.columns(2)

      #barplot
      with col1:
        ax.bar(busycount.index, busycount.values, color='blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

      #dataframe for busy users
      with col2:
        st.dataframe(newdf)

    #wordcloud
    st.title("Word Cloud")
    df_img = stats.createwordcloud(selected_user, df)
    fig, ax = plt.subplots()
    ax.imshow(df_img)
    st.pyplot(fig)

    #most common words in chat
    most_common_df = stats.getcommonwords(selected_user, df)
    fig, ax = plt.subplots()
    ax.barh(most_common_df[0], most_common_df[1])
    plt.xticks(rotation='vertical')
    st.title('Most Common Words')
    st.pyplot(fig)

    #emoji analysis
    emoji_df = stats.getemojistats(selected_user, df)
    emoji_df.columns = ['Emoji', 'Count']

    st.title("Emoji Analysis")
    col1, col2 = st.columns(2)

    with col1:
      st.dataframe(emoji_df)

    with col2:
      emojicount = list(emoji_df['Count'])
      perlist = [(i / sum(emojicount)) * 100 for i in emojicount]
      emoji_df['Percentage use'] = np.array(perlist)
      st.dataframe(emoji_df)

    #monthly timeline
    st.title("Monthly Timeline")
    time = stats.monthtimeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(time['Time'], time['Message'], color='green')
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    st.pyplot(fig)

    #Activity maps
    st.title("Activity Maps")
    col1, col2 = st.columns(2)
    with col1:
      st.header("Most Busy Day")
      busy_day = stats.weekactivitymap(selected_user, df)

      fig, ax = plt.subplots()
      ax.bar(busy_day.index, busy_day.values, color='orange')
      plt.xticks(rotation='vertical')
      plt.tight_layout()
      st.pyplot(fig)
