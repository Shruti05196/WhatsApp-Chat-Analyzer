# import streamlit as st
# import preprocessor, helper
# import matplotlib.pyplot as plt
# import seaborn as sns
# from helper import calculate_streak
#
# # ✅ Custom CSS for UI Styling
# st.markdown(
#     """
#     <style>
#     /* Main Title (WhatsApp Chat Analyzer) */
#     .main-title {
#         font-size: 40px !important;
#         font-weight: bold !important;
#         text-align: center;
#         color: #4CAF50 !important;
#         margin-top: -60px !important; /* Move title further up */
#     }
#
#     /* File Uploader Title */
#     .file-uploader label {
#         font-size: 30px !important;
#         font-weight: bold !important;
#         color: white !important;
#     }
#
#     /* Sidebar Styling */
#     [data-testid="stSidebar"] {
#         background: #121212 !important;
#         padding: 20px !important;
#         border-right: 2px solid white !important;
#     }
#
#     /* Sidebar Labels */
#     .sidebar-text {
#         font-size: 20px !important;
#         font-weight: bold !important;
#         color: white !important;
#         display: inline-block !important;
#         white-space: nowrap !important;
#     }
#
#     /* Increase Font Size for Radio Button Labels */
#     div[role="radiogroup"] label {
#         font-size: 20px !important;
#         font-weight: bold !important;
#         color: white !important;
#         padding: 5px !important;
#     }
#
#     /* Show Analysis Button */
#     div.stButton > button:first-child {
#         background-color: #4CAF50 !important;
#         color: white !important;
#         font-size: 25px !important;
#         font-weight: bold !important;
#         border-radius: 10px !important;
#         padding: 10px 20px !important;
#     }
#
#     /* Metric Card Styling */
#     .metric-card {
#         background-color: #2A2A2A;
#         padding: 20px;
#         border-radius: 12px;
#         text-align: center;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
#         margin: 10px;
#     }
#     .metric-label {
#         font-size: 22px;
#         font-weight: bold;
#         color: white;
#     }
#     .metric-value {
#         font-size: 30px;
#         font-weight: bold;
#         color: #32CD32;
#     }
#
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # ✅ App Title
# st.markdown('<h1 class="main-title">WhatsApp Chat Analyzer</h1>', unsafe_allow_html=True)
#
# # ✅ File uploader (Updated UI)
# st.sidebar.markdown('<h3 class="file-uploader">📂 Choose a file</h3>', unsafe_allow_html=True)
# uploaded_file = st.sidebar.file_uploader("", type=["txt"])
#
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = bytes_data.decode("utf-8")
#     df = preprocessor.preprocess(data)
#
#     # Unique Users List
#     user_list = df['user'].unique().tolist()
#     if 'group_notification' in user_list:
#         user_list.remove('group_notification')
#     user_list.sort()
#     user_list.insert(0, "Overall")
#
#     # ✅ Updated Sidebar Feature Selection
#     st.sidebar.markdown('<p class="sidebar-text">📊 Show analysis for</p>', unsafe_allow_html=True)
#     selected_user = st.sidebar.selectbox("", user_list)
#
#     st.sidebar.markdown('<p class="sidebar-text">🔍 Select Feature to Analyze</p>', unsafe_allow_html=True)
#
#     features = [
#         "Chat Statistics",
#         "Longest Message in Chat",
#         "Monthly Timeline",
#         "Daily Timeline",
#         "Most Busy Day & Month",
#         "Weekly Heatmap",
#         "Most Active Users",
#         "WordCloud",
#         "Most Common Words",
#         "Emoji Analysis",
#         "Sentiment Analysis",
#         "Active Time Analysis",
#         "Most Engaging Conversations",
#         "Fun Fact Generator",
#         "Deleted Messages Recovery Stats",
#         "Chat Streak Analysis"
#     ]
#     selected_feature = st.sidebar.radio("", features)
#
#     if st.sidebar.button("Show Analysis"):
#         st.title(selected_feature)
#
#         if selected_feature == "Chat Statistics":
#             num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
#
#             col1, col2, col3, col4 = st.columns(4)
#
#             with col1:
#                 st.metric(label="📩 Total Messages", value=num_messages)
#
#             with col2:
#                 st.metric(label="📝 Total Words", value=words)
#
#             with col3:
#                 st.metric(label="📸 Media Shared", value=num_media_messages)
#
#             with col4:
#                 st.metric(label="🔗 Links Shared", value=num_links)
#
#         elif selected_feature == "Chat Streak Analysis":
#             st.subheader("🔥 Chat Streak Analysis")
#             most_consistent_user, max_streak = calculate_streak(df)
#             st.write(f"🏆 *Most Consistent User:* {most_consistent_user}")
#             st.write(f"🔥 *Longest Chat Streak:* {max_streak} days")
#
#         # ✅ Adding Back Other Features
#         elif selected_feature == "Longest Message in Chat":
#             longest_msg = helper.longest_message(selected_user, df)
#             st.write(f"📝 *Longest Message:* {longest_msg}")
#
#         elif selected_feature == "WordCloud":
#             st.subheader("☁️ WordCloud")
#             wordcloud = helper.create_wordcloud(selected_user, df)
#             st.image(wordcloud.to_array())
#
#         elif selected_feature == "Most Common Words":
#             st.subheader("📌 Most Common Words")
#             most_common_df = helper.most_common_words(selected_user, df)
#             st.dataframe(most_common_df)
#
#         elif selected_feature == "Sentiment Analysis":
#             st.subheader("📈 Sentiment Trend Over Time")
#             sentiment_trend = helper.sentiment_trend(selected_user, df)
#             st.line_chart(sentiment_trend)
#
#         elif selected_feature == "Deleted Messages Recovery Stats":
#             st.subheader("🚨 Deleted Messages Stats")
#             deleted_stats = helper.deleted_messages_stats(selected_user, df)
#             st.write(deleted_stats)
#
#         elif selected_feature == "Auto Chat Summary":
#             st.subheader("📝 Auto Chat Summary")
#             summary = helper.generate_chat_summary(selected_user, df)
#             st.write(summary)
#
#
#
#
#
#
#
#


import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
from helper import calculate_streak

# ✅ Custom CSS for UI Styling
st.markdown(
    """
    <style>
    /* Main Title (WhatsApp Chat Analyzer) */
    .main-title {
        font-size: 40px !important;
        font-weight: bold !important;
        text-align: center;
        color: #4CAF50 !important;
        margin-top: -60px !important; /* Move title further up */
    }

    /* File Uploader Title */
    .file-uploader label {
        font-size: 30px !important;
        font-weight: bold !important;
        color: white !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #121212 !important;
        padding: 20px !important;
        border-right: 2px solid white !important;
    }

    /* Sidebar Labels */
    .sidebar-text {
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        display: inline-block !important;
        white-space: nowrap !important;
    }

    /* Increase Font Size for Radio Button Labels */
    div[role="radiogroup"] label {
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        padding: 5px !important;
    }

    /* Show Analysis Button */
    div.stButton > button:first-child {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 25px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
    }

    /* Metric Card Styling */
    .metric-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    .metric-card {
        background-color: #2A2A2A;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        margin: 10px;
        width: 22%;
    }
    .metric-label {
        font-size: 22px;
        font-weight: bold;
        color: white;
    }
    .metric-value {
        font-size: 30px;
        font-weight: bold;
        color: #32CD32;
    }
    

    </style>
    """,
    unsafe_allow_html=True
)

# ✅ App Title
st.markdown('<h1 class="main-title">WhatsApp Chat Analyzer</h1>', unsafe_allow_html=True)

# ✅ File uploader (Updated UI)
st.sidebar.markdown('<h3 class="file-uploader">📂 Choose a file</h3>', unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("", type=["txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Unique Users List
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    # ✅ Updated Sidebar Feature Selection
    st.sidebar.markdown('<p class="sidebar-text">📊 Show analysis for</p>', unsafe_allow_html=True)
    selected_user = st.sidebar.selectbox("", user_list)

    st.sidebar.markdown('<p class="sidebar-text">🔍 Select Feature to Analyze</p>', unsafe_allow_html=True)

    features = [
        "Chat Statistics",
        "Longest Message in Chat",
        "Monthly Timeline",
        "Daily Timeline",
        "Most Busy Day & Month",
        "Weekly Heatmap",
        "Most Active Users",
        "WordCloud",
        "Most Common Words",
        "Emoji Analysis",
        "Sentiment Analysis",
        "Active Time Analysis",
        "Most Engaging Conversations",
        "Fun Fact Generator",
        "Deleted Messages",
        "Chat Streak Analysis"
    ]
    selected_feature = st.sidebar.radio("", features)

    if st.sidebar.button("Show Analysis"):
        st.title(selected_feature)

        if selected_feature == "Chat Statistics":
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

            st.markdown("""
            <div class='metric-container'>
                <div class='metric-card'>
                    <div class='metric-label'>📩 Total Messages</div>
                    <div class='metric-value'>{}</div>
                </div>
                <div class='metric-card'>
                    <div class='metric-label'>📝 Total Words</div>
                    <div class='metric-value'>{}</div>
                </div>
                <div class='metric-card'>
                    <div class='metric-label'>📸 Media Shared</div>
                    <div class='metric-value'>{}</div>
                </div>
                <div class='metric-card'>
                    <div class='metric-label'>🔗 Links Shared</div>
                    <div class='metric-value'>{}</div>
                </div>
            </div>
            """.format(num_messages, words, num_media_messages, num_links), unsafe_allow_html=True)

        elif selected_feature == "Longest Message in Chat":
            user, message, length = helper.longest_message(selected_user,df)
            st.write(f"📢 User: {user}")
            st.write(f"📝 Message: {message}")
            st.write(f"🔢 Length: {length} characters")


        elif selected_feature == "Monthly Timeline":
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='green')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        elif selected_feature == "Daily Timeline":
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        elif selected_feature == "Most Busy Day & Month":
            col1, col2 = st.columns(2)
            with col1:
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                sns.barplot(x=busy_day.index, y=busy_day.values, ax=ax, palette="viridis")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                sns.barplot(x=busy_month.index, y=busy_month.values, ax=ax, palette="coolwarm")
                plt.xticks(rotation=45)
                st.pyplot(fig)

        elif selected_feature == "Weekly Heatmap":
            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            ax = sns.heatmap(user_heatmap)
            st.pyplot(fig)

        # elif selected_feature == "Most Active Users":
        #     if selected_user == 'Overall':
        #         x, new_df = helper.most_busy_users(df)
        #
        #         col1, col2 = st.columns(2)
        #         with col1:
        #             fig, ax = plt.subplots()
        #             sns.barplot(x=x.index, y=x.values, ax=ax, palette="rocket")
        #             plt.xticks(rotation=45)
        #             st.pyplot(fig)
        #         with col2:
        #             # ✅ Table me "count" column bhi show karein
        #             st.dataframe(new_df[["user", "count", "percent"]])
        #
        #             # st.dataframe(new_df)

        elif selected_feature == "Most Active Users":
            if selected_user == 'Overall':
                x, new_df = helper.most_busy_users(df)

                # 🔍 Debugging: Check column names

                col1, col2 = st.columns(2)
                with col1:
                    fig, ax = plt.subplots()
                    sns.barplot(x=x.index, y=x.values, ax=ax, palette="rocket")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

                with col2:
                    # 🛠 Fix: Ensure correct column names
                    correct_columns = ["user", "count", "percent"]
                    available_columns = new_df.columns.tolist()

                    if all(col in available_columns for col in correct_columns):
                        st.dataframe(new_df[correct_columns])
                    else:
                        st.write("⚠️ Error: Columns not found. Available columns:", available_columns)
                        st.dataframe(new_df)  # Pura DataFrame show karega error debug karne ke liye



        elif selected_feature == "Most Active Users":
            if selected_user == 'Overall':
                new_df = helper.most_busy_users(df)  # ✅ Ek hi value return ho rahi hai
                col1, col2 = st.columns(2)
                with col1:
                    fig, ax = plt.subplots()
                    sns.barplot(x=new_df["User"], y=new_df["Message Count"], ax=ax, palette="rocket")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)
                with col2:
                    st.dataframe(new_df)


        elif selected_feature == "WordCloud":
            df_wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots()
            0
            ax.imshow(df_wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)

        elif selected_feature == "Most Common Words":
            most_common_df = helper.most_common_words(selected_user, df)
            fig, ax = plt.subplots()
            most_common_df.columns = ["word", "count"]
            sns.barplot(y=most_common_df["word"], x=most_common_df["count"], ax=ax, palette="magma")
            st.pyplot(fig)

        # elif selected_feature == "Emoji Analysis":
        #     emoji_df = helper.emoji_helper(selected_user, df)
        #
        #     col1, col2 = st.columns(2)
        #
        #     with col1:
        #         st.dataframe(emoji_df)
        #
        #     with col2:
        #         fig, ax = plt.subplots()
        #         ax.pie(emoji_df["Count"].head(), labels=emoji_df["Emoji"].head(), autopct="%0.2f",
        #                colors=sns.color_palette("pastel"), textprops={'fontsize': 14})
        #         st.pyplot(fig)

        elif selected_feature == "Emoji Analysis":
            emoji_df = helper.emoji_helper(selected_user, df)

            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)

            with col2:
                if not emoji_df.empty:  # Check if DataFrame is not empty
                    fig, ax = plt.subplots()
                    ax.pie(emoji_df["Count"].head(), labels=emoji_df["Emoji"].head(), autopct="%0.2f",
                           colors=sns.color_palette("pastel"), textprops={'fontsize': 14})
                    st.pyplot(fig)
                else:
                    st.warning("No emojis found in the selected chat!")




        elif selected_feature == "Sentiment Analysis":
            df['sentiment'] = df['message'].apply(helper.get_sentiment)
            sentiment_counts = df['sentiment'].value_counts()
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Sentiment Distribution Table")
                st.dataframe(sentiment_counts)
            with col2:
                fig, ax = plt.subplots()
                ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%0.2f%%",
                       colors=['#66BB6A', '#FA8072', 'gray'], textprops={'fontsize': 14})
                st.pyplot(fig)



        elif selected_feature == "Active Time Analysis":
            active_hours = helper.active_time_analysis(selected_user, df)
            fig, ax = plt.subplots()
            sns.barplot(x=active_hours.index, y=active_hours.values, palette="coolwarm", ax=ax)
            ax.set_xlabel("Hour of the Day")
            ax.set_ylabel("Message Count")
            ax.set_title("Active Hours Analysis")
            st.pyplot(fig)

        elif selected_feature == "Most Engaging Conversations":
            conversation_df = helper.most_engaging_conversations(df)
            st.dataframe(conversation_df.head(10))  # Show top 10 engaging conversations

            # ✅ Visualizing Most Engaging Conversations
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(y=conversation_df["User Pair"].head(10).astype(str),
                        x=conversation_df["Message Count"].head(10),
                        palette="magma", ax=ax)
            ax.set_xlabel("Message Count")
            ax.set_ylabel("User Pair")
            ax.set_title("Most Engaging Conversations")
            st.pyplot(fig)

        elif selected_feature == "Fun Fact Generator":
            fun_facts = helper.fun_fact_generator(df)
            st.subheader("📢 Fun Facts About This Chat")
            for fact, value in fun_facts.items():
                st.write(f"✅ {fact}: {value}")

        elif selected_feature == "Deleted Messages":
            # ✅ Count deleted messages
            num_deleted = df['deleted'].sum()

            # ✅ Convert to dictionary
            deleted_stats = {"Deleted Messages": num_deleted}

            # ✅ Display the stats
            for stat, value in deleted_stats.items():
                st.write(f"{stat}:** {value}")

        elif selected_feature == "Chat Streak Analysis":
            st.subheader("🔥 Chat Streak Analysis")

            most_consistent_user, max_streak = calculate_streak(df)

            st.write(f"🏆 Most Consistent User: {most_consistent_user}")
            st.write(f"🔥 Longest Chat Streak: {max_streak}days")
