import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['deleted'] = df['message'].apply(lambda x: 1 if x == "This message was deleted" else 0)

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df











# import re
# import pandas as pd
#
#
# def preprocess(data):
#     # Corrected regex pattern for extracting timestamps and user messages
#     pattern = r"\[\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2} ?[APM]{2}\]"  # Matches timestamps
#
#     # Splitting messages using timestamps
#     messages = re.split(pattern, data)[1:]
#     dates = re.findall(pattern, data)
#
#     # Cleaning timestamps
#     dates = [re.sub(r"[\[\]]", "", date) for date in dates]  # Removing square brackets
#
#     df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#
#     # Convert message_date type
#     df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p')
#
#     df.rename(columns={'message_date': 'date'}, inplace=True)
#
#     users = []
#     messages = []
#
#     for message in df['user_message']:
#         entry = re.split(r"([^:]+):\s", message, maxsplit=1)  # Splitting at first occurrence of ': '
#
#         if len(entry) > 1:  # If it's a user message
#             users.append(entry[1].strip())
#             messages.append(entry[2].strip())
#         else:  # If it's a system message (like group creation, user added, etc.)
#             users.append("group_notification")
#             messages.append(entry[0].strip())
#
#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['user_message'], inplace=True)
#
#     # Extracting date-time components
#     df['only_date'] = df['date'].dt.date
#     df['year'] = df['date'].dt.year
#     df['month_num'] = df['date'].dt.month
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day
#     df['day_name'] = df['date'].dt.day_name()
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute
#
#     # Detect deleted messages
#     df['deleted'] = df['message'].apply(lambda x: 1 if x.strip() == "This message was deleted" else 0)
#
#     # Creating time periods for hourly analysis
#     period = []
#     for hour in df['hour']:
#         if hour == 23:
#             period.append(f"{hour}-00")
#         elif hour == 0:
#             period.append("00-1")
#         else:
#             period.append(f"{hour}-{hour + 1}")
#
#     df['period'] = period
#
#     return df
