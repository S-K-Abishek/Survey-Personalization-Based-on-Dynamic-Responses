
# 🧠 Survey Personalization Based on Dynamic Responses

This project is a Flask web application designed to create **dynamic and personalized survey experiences**. It uses conditional routing to present questions based on user inputs, offering a more intelligent and adaptive survey flow.

## 🚀 Features

- Dynamic question routing based on previous responses.
- Modular structure using Flask.
- SQLite database integration via SQLAlchemy.
- Admin panel to view all survey responses.
- Clean user flow from start to thank-you page.

## 🛠️ Technologies Used

- **Flask** – for routing and web framework
- **SQLAlchemy** – for ORM and database interaction
- **HTML/CSS** – for UI rendering
- **SQLite** – as the database backend

## 🧪 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/S-K-Abishek/Survey-Personalization-Based-on-Dynamic-Responses.git
   ```

2. **Install dependencies**:
   ```bash
   pip install flask flask_sqlalchemy
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧠 Survey Flow Example

- Q1: If answer is "Yes" → continue with Q2 to Q10
- If "No" → skip certain questions
- Based on numerical and text inputs, next questions vary dynamically

## 🎬 Demo Video

📹 [Click here to watch the demo video](./Consice%20Video%20-%20Survey%20Personalization%20Based%20on%20Dynamic%20Responses.mp4
)

Or download it and play it locally.

## 📄 Project Report

📘 You can [view the full project report here](./Report%20-%20Survey%20Personalization%20Based%20on%20Dynamic%20Responses.pdf
)

The report outlines the following key areas:

- Flask setup for web routing and form rendering
- SQLAlchemy for managing dynamic survey responses
- Dynamic question flow using user input
- Recommendations for scalability, UI improvements, and analytics

## 📈 Future Enhancements

- Add user authentication
- Include data analytics dashboard using Pandas/Matplotlib
- Enhance frontend using Bootstrap/React
- Make the survey multilingual and accessible

## 👨‍💻 Author

**Abishek S K**   
**shekabi626210@gmail.com**   
Project:  *Survey Personalization Based on Dynamic Responses*

## 📜 License

This project is licensed under the MIT License.
