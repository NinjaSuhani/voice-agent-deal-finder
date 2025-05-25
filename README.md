# voice-agent-deal-finder
# 🎙️ Voice Agent for Finding the Best Deal on High-Demand Drops

This project is a Voice AI Agent that helps users find the **best deal** for limited-edition items like **sneakers** or **concert tickets**. It uses **OmniDimension** to simulate calls to multiple resellers, compare prices and delivery times, and recommend the top 3 options. After the interaction, it sends a **summary email** to the user and **logs the data in Google Sheets**.

---

## 🧠 Features

- 📞 Voice agent built using **OmniDimension**
- 💬 Collects seller offers (price, delivery time, name)
- 📊 Compares offers and recommends top 3
- 📧 Sends deal summary via email
- 🧾 Logs data into **Google Sheets** using Google Sheets API

---

## 🚀 Tech Stack

- 🐍 Python 3.12
- 🔥 Flask
- 🌐 OmniDimension (Voice AI Platform)
- 📋 Google Sheets API via `gspread` and `google-auth`
- 📩 `smtplib` for email automation (optional if email is handled in OmniDimension)

---

## 📁 Project Structure

