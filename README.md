📊 Day 37 – Pixela Habit Tracker (Reading Graph)

This project uses the Pixela API to track daily reading progress by posting pixels to a graph.
Each pixel represents the number of pages read on a specific date.

🚀 Features

Creates a Pixela graph

Automatically formats today’s date (YYYYMMDD)

Posts daily reading data

Uses environment variables for security

Sends data only to my own Pixela account

🛠️ Technologies Used

Python 3

requests

datetime

Pixela REST API

🔐 Environment Variables (Required)

For security reasons, tokens are NOT hard-coded.

Set variables (Windows PowerShell):
setx PIXELA_TOKEN "your_pixela_token"
setx PIXELA_USERNAME "your_pixela_username"


⚠️ Restart your terminal after running these commands.

📦 Installation

Clone the repository

git clone https://github.com/your-username/Day-37-Pixela-Habit-Tracker.git


Install dependencies

pip install requests

▶️ How It Works

Gets today’s date in YYYYMMDD format

Creates a graph on Pixela

Posts a pixel with the number of pages read

Example pixel data:

{
    "date": "20260104",
    "quantity": "25"
}

📈 Graph Configuration

Graph Name: Reading Graph

Unit: pages

Type: integer

Color: sora

📌 Notes

This script posts data only to my own Pixela account

Environment variables keep credentials safe

Date handling is fully automatic

🧠 Learning Outcome

Working with REST APIs

Authentication using headers

Environment variable management

Date formatting in Python

✅ Status

Completed ✔️
