from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
from textblob import TextBlob
import random

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words), num_media_messages, len(links)

# def most_busy_users(df):
#     x = df['user'].value_counts().head()
#     df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
#         columns={'index': 'name', 'user': 'percent'})
#     return x, df
def most_busy_users(df):
    x = df['user'].value_counts().head()

    # 🛠 Fix: Ensure correct column names
    df = df['user'].value_counts().reset_index()
    df.columns = ['user', 'count']  # ✅ 'user' ko sahi column name diya
    df['percent'] = round((df['count'] / df['count'].sum()) * 100, 2)  # ✅ Percent column add kiya

    return x, df


def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


import pandas as pd
import emoji
from collections import Counter


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]  # Filter data for selected user

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    if not emojis:
        return pd.DataFrame(columns=["Emoji", "Count"])  # Return empty DataFrame if no emojis found

    # Count occurrences of each emoji
    emoji_counts = Counter(emojis).most_common()

    # Convert to DataFrame
    emoji_df = pd.DataFrame(emoji_counts, columns=["Emoji", "Count"])

    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap

def get_sentiment(message):
    analysis = TextBlob(message)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"






# def longest_message(df):

def longest_message(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]  # Filter for selected user

    if df.empty:
        return "No messages found", "", 0  # Handle empty data

    longest_msg = df.loc[df['message'].str.len().idxmax()]
    return longest_msg['user'], longest_msg['message'], len(longest_msg['message'])



def active_time_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['hour'] = df['date'].dt.hour  # Extracting hour from timestamp
    active_hours = df['hour'].value_counts().sort_index()

    return active_hours

from itertools import combinations

def most_engaging_conversations(df):
    """
    Identifies the most engaging user pairs in the chat.
    Returns a DataFrame with top conversations based on the number of messages exchanged.
    """
    user_pairs = []
    df['prev_user'] = df['user'].shift(1)  # Get the previous message sender

    for i in range(1, len(df)):
        user_pair = tuple(sorted([df.loc[i, 'user'], df.loc[i - 1, 'user']]))
        if df.loc[i, 'user'] != df.loc[i - 1, 'user']:  # Ignore consecutive messages from the same user
            user_pairs.append(user_pair)

    conversation_counts = pd.DataFrame(pd.Series(user_pairs).value_counts().reset_index())
    conversation_counts.columns = ["User Pair", "Message Count"]

    return conversation_counts

def fun_fact_generator(df):
    facts = {}

    # ✅ 1. Longest Message in Chat
    longest_msg = df.loc[df['message'].str.len().idxmax()]
    facts["Longest Message"] = f"{longest_msg['user']} sent the longest message with {len(longest_msg['message'])} characters."

    # ✅ 2. Most Used Emoji
    emoji_df = emoji_helper("Overall", df)  # Call existing emoji analysis function
    if not emoji_df.empty:
        most_used_emoji = emoji_df.iloc[0, 0]  # First emoji
        facts["Most Used Emoji"] = f"'{most_used_emoji}' was the most used emoji."

    # ✅ 3. Max Messages in One Day
    daily_count = df.groupby("only_date")["message"].count()
    max_day = daily_count.idxmax()
    max_msg = daily_count.max()
    facts["Most Active Day"] = f"On {max_day}, {max_msg} messages were sent (highest in chat history)."

    # ✅ 4. Most Common Filler Words (like 'hmm', 'ok', 'acha')
    common_fillers = ["hmm", "ok", "acha", "haan", "lol", "hahaha"]
    filler_counts = {word: df['message'].str.lower().str.count(rf"\b{word}\b").sum() for word in common_fillers}
    most_used_filler = max(filler_counts, key=filler_counts.get)
    facts["Most Used Word"] = f"'{most_used_filler}' was the most used filler word with {filler_counts[most_used_filler]} occurrences."

    return facts

# def deleted_messages_stats(df):
#     deleted_msgs_df = df[df["message"] == "This message was deleted"]  # ✅ Find deleted messages
#     deleted_count = len(deleted_msgs_df)
#
#     if deleted_count == 0:
#         return {"Deleted Messages": "No deleted messages found!"}
#
#     deleted_percentage = (deleted_count / len(df)) * 100
#     deleted_by_user = deleted_msgs_df["user"].value_counts()
#
#     stats = {
#         "Total Deleted Messages": f"{deleted_count} messages were deleted.",
#         "Deleted Messages Percentage": f"{deleted_percentage:.2f}% of total messages were deleted.",
#         "Most Deleted Messages by": f"{deleted_by_user.idxmax()} deleted the most messages ({deleted_by_user.max()} messages)."
#     }
#
#     return stats


def deleted_messages_stats(df):
    deleted_count = df["deleted"].sum()  # ✅ Directly count deleted messages

    if deleted_count == 0:
        return {"Deleted Messages": "No deleted messages found!"}

    deleted_percentage = (deleted_count / len(df)) * 100
    deleted_by_user = df[df["deleted"] == 1]["user"].value_counts()

    stats = {
        "Total Deleted Messages": f"{deleted_count} messages were deleted.",
        "Deleted Messages Percentage": f"{deleted_percentage:.2f}% of total messages were deleted.",
        "Most Deleted Messages by": f"{deleted_by_user.idxmax()} deleted the most messages ({deleted_by_user.max()} messages)."
    }

    return stats





def deleted_messages_stats(df):
    # Ensure the 'deleted' column exists
    df['deleted'] = df['message'].apply(lambda x: 1 if x == "This message was deleted" else 0)

    # Count deleted messages
    num_deleted = df['deleted'].sum()
    return num_deleted


def calculate_streak(df):
    """Calculate the longest chat streak for any user."""

    df['only_date'] = pd.to_datetime(df['only_date'])

    user_streaks = {}

    for user in df['user'].unique():
        user_df = df[df['user'] == user]
        sorted_dates = user_df['only_date'].sort_values().unique()

        max_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i] - sorted_dates[i - 1]).days == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1

        user_streaks[user] = max_streak

    most_consistent_user = max(user_streaks, key=user_streaks.get)
    max_streak = user_streaks[most_consistent_user]

    return most_consistent_user, max_streak








