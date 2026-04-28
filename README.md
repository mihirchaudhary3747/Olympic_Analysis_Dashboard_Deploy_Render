# 🏅 Olympic Analysis Dashboard

An interactive data visualization dashboard built using **Python and Streamlit** that explores over 120 years of Olympic Games data. This project helps users analyze athlete performance, country-wise medal distribution, and historical trends through an easy-to-use interface.

---

## 📌 Project Overview

The **Olympic Analysis Dashboard** converts raw Olympic datasets into meaningful insights using data analysis and visualization techniques. Users can explore patterns such as:

* Medal distribution across countries and years
* Growth of athletes, sports, and events over time
* Country-wise Olympic performance
* Athlete-level analysis (age, height, weight trends)

The goal of this project is to demonstrate **data analysis + dashboard building skills** in a real-world scenario.

---

## ✨ Features

### 🏅 Medal Tally

* Filter medals by **year and country**
* View total Gold, Silver, and Bronze medals

### 📊 Overall Analysis

* Total editions, sports, events, athletes, and nations
* Trend graphs for:

  * Participating nations
  * Number of events
  * Athlete participation

### 🌍 Country-wise Analysis

* Year-wise medal trend of a selected country
* Heatmap of sports participation
* Most successful athletes of that country

### 👤 Athlete-wise Analysis

* Age distribution of athletes and medalists
* Sport-wise gold medalist analysis
* Height vs Weight comparison
* Male vs Female participation trends

---

## 🛠️ Technologies Used

* **Python** → Core programming
* **Streamlit** → Web app framework
* **Pandas** → Data cleaning and manipulation
* **Plotly** → Interactive visualizations
* **Matplotlib & Seaborn** → Supporting plots
* **HTML & CSS** → Custom UI styling

---

## 📂 Project Structure

```
OlympicAnalysis/
│── app.py                  # Main Streamlit application
│── helper.py              # Functions for analysis
│── preprocessor.py        # Data cleaning logic
│── athlete_events.csv     # Main dataset
│── noc_regions.csv        # Country mapping dataset
│── olympic_logo.png       # Logo used in UI
│── README.md              # Project documentation
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/olympic-analysis-dashboard.git
cd olympic-analysis-dashboard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 📊 Dataset Information

The project uses Olympic historical data which includes:

* Athlete name, age, gender
* Sport and event details
* Medal information
* Country/region mapping

---

## 🎯 Purpose of the Project

This project is created to demonstrate:

* Data analysis and preprocessing
* Interactive visualization
* Dashboard development using Streamlit
* UI/UX customization using CSS

It is ideal for showcasing skills in **data science and analytics portfolios**.

---

## 🚀 Future Improvements

* 🌍 Add world map visualization
* 🔍 Add search functionality for athletes
* 📱 Improve mobile responsiveness
* ☁️ Deploy app online (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Mihir Tomar**

* GitHub: https://github.com/mihirchaudhary3747
* LinkedIn: https://www.linkedin.com/in/mihirtomar3747

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
