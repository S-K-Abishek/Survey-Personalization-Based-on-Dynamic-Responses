
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
- **HTML/CSS (Jinja templates)** – for UI rendering
- **SQLite** – as the database backend

## 🧪 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/S-K-Abishek/Survey-Personalization-Based-on-Dynamic-Responses.git
   cd dynamic-survey-flask
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

## 🎥 Demo Video

<video width="640" height="360" controls>
  <source src="Consice Video - Survey Personalization Based on Dynamic Responses.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

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
