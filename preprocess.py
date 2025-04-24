
import re
import pandas as pd
import streamlit as st

def preprocess(data):
    pattern1 = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}),?\s*(\d{1,2}:\d{2}(?::\d{2})?\s*[APap][Mm])\s*[-\[]?\s*([^:]+):\s*(.+)'
    pattern2 = r'\[?(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}),?\s*(\d{1,2}:\d{2}(?::\d{2})?\s*[APap][Mm])\]?\s*([^:]+):\s*(.+)'

    date = []
    time = []
    user = []
    message = []
    unmatched_lines = []

    for text in data:
        text = text.strip()
        if not text:  # Skip empty lines
            continue
            
        match1 = re.search(pattern1, text)
        match2 = re.search(pattern2, text)

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

    if len(unmatched_lines) > 0:
        st.warning(f"Found {len(unmatched_lines)} unmatched lines. First few: {unmatched_lines[:3]}")

    if not date:
        st.error("No messages matched the expected format. Please check your input file format.")
        return None

    try:
        df = pd.DataFrame({
            'Date': date,
            'Time': time,
            'User': user,
            'Message': message
        })
        
        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], 
                                      format='mixed', 
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

        # Drop rows with invalid DateTime
        invalid_count = df['DateTime'].isna().sum()
        if invalid_count > 0:
            st.warning(f"Dropped {invalid_count} rows with invalid date/time format")
            
        df = df.dropna(subset=['DateTime'])

        if len(df) == 0:
            st.error("No valid messages remained after processing")
            return None
            
        st.success(f"Successfully processed {len(df)} messages")
        return df
        
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        return None
