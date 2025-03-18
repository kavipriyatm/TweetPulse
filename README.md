# TweetPulse
A Python-based Twitter Sentiment Analysis project that fetches live tweets using the Twitter API, analyzes sentiments (positive, negative, neutral), and visualizes results with word clouds and bar graphs. Secure API handling via .env file. Easy to run and interpret!
Got you! Here's a **ready-to-paste** `README.md` file that clearly tells people to add their API keys in a `.env` file, with no extra changes needed on your side. Just copy and paste this into GitHub!

---

```markdown
# Twitter Sentiment Analysis and Word Cloud Generation

## 📌 Project Description

This project performs **Sentiment Analysis** on tweets related to trending topics. It fetches live data from Twitter, analyzes sentiment (positive, neutral, negative), and visualizes the results using:
- **Word Clouds**
- **Bar Graphs**
- **Tabular outputs**

The analysis provides insights into public opinion on the given keywords or hashtags.

---

## 🔧 Features
- Real-time Twitter data fetching
- Sentiment classification (Positive, Neutral, Negative)
- Cleaned and pre-processed tweet text
- Word cloud generation for frequently used terms
- Sentiment distribution shown as a bar chart
- Results displayed in a pandas DataFrame

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Tweepy** (Twitter API)
- **TextBlob** (Sentiment Analysis)
- **WordCloud** (Word cloud generation)
- **Matplotlib** (Visualization)
- **Pandas** (Data manipulation)

---

## 📁 Project Structure

```
.
├── src
│   ├── sentiment.py
├── README.md
├── .env  # Contains your Twitter API keys
```

---

## ✅ Prerequisites

1. **Python 3.x** installed
2. Install the required Python libraries:
   ```bash
   pip install tweepy textblob pandas matplotlib wordcloud python-dotenv
   ```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kavipriyatm/TweetPulse.git

```

### 2️⃣ Navigate to the Project Folder
```bash
cd TweetPulse/src

```

### 3️⃣ Create a `.env` File in the Root Directory
Create a file named `.env` (next to `sentiment.py`).

### 4️⃣ Add Your Twitter API Keys to the `.env` File
Paste your Twitter API keys in this format:

```
TWITTER_API_KEY="YOUR TWITTER_API_SECRET"
TWITTER_API_SECRET="YOUR TWITTER_API_SECRET"
ACCESS_TOKEN="YOUR ACCESS_TOKEN"
ACCESS_TOKEN_SECRET="YOUR ACCESS_TOKEN"
BEARER_TOKEN="YOUR BEARER_TOKEN"
CLIENT_ID = "YOUR CLIENT_ID"
CLIENT_SECRET = "YOUR CLIENT_SECRET"

```

> ⚠️ **Note:** Get these keys from your [Twitter Developer Portal](https://developer.twitter.com/).

### 5️⃣ Run the Sentiment Analysis Script
```bash
python sentiment.py
```

---

## 📊 Expected Output

### 1. **Tabular Output in Terminal**
| Username | Text | Created At | Cleaned Text | Sentiment |
| -------- | ---- | ---------- | ------------ | --------- |
| NaN | RT @Sissyai88: NO. 94 Robin - Honkai: Star Rail 50P... | 2025-03-17 04:59:41+00:00 | rt sissyai88 94 robin honkai star rail 50p nsfw | Positive |
| NaN | @Ammo_AI #AI #ammo | 2025-03-17 04:59:40+00:00 | ammoai ai ammo | Neutral |
| ... | ... | ... | ... | ... |

### 2. **Word Cloud Image**
A visualization displaying the most common words in the tweets.

### 3. **Sentiment Bar Graph**
A bar chart showing the count of Positive, Neutral, and Negative tweets.

---

## ⚙️ Project Flow (Backend)

- Connects to Twitter API using Tweepy.
- Fetches the latest tweets based on a hashtag/keyword.
- Cleans the tweet text (removes links, mentions, hashtags, emojis).
- Uses TextBlob for sentiment analysis.
- Displays data in terminal and generates:
  - **Word Cloud**
  - **Sentiment Bar Graph**

---

## 🔐 API Keys Handling (IMPORTANT)

- Your API keys should **NOT** be hardcoded in the script.
- They should be placed in the `.env` file (as shown above).
- The script automatically loads these keys using `python-dotenv`.

> ✅ `.env` file is already listed in `.gitignore` to keep your keys safe and private.

---

## 📂 Output Files
- `wordcloud.png` : Word cloud image
- `sentiment_bargraph.png` : Sentiment distribution chart
- Tabular output: Displayed in terminal

---

## 🔗 API Integration
- Backend script only. No front-end client included.
- Twitter API is integrated via Tweepy library.

---

## ✍️ Author

👤 **Kavipriya TM**  
GitHub: [@kavipriyatm](https://github.com/kavipriyatm)

---

## 📄 License
[MIT](LICENSE)
```

---

### ✅ Notes:
- This README tells them where to create `.env` and exactly how to format it.
- `.env` is assumed to be next to `sentiment.py` inside `src/`.
- You don't need to edit anything. Just drop this into your GitHub project as `README.md`.

If you want, I can help you make a sample `.env` and `.gitignore` too!
