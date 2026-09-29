# 10 Domain-Specific Gemini Flask Chatbots

Each folder is a standalone Flask chatbot.

Model: gemini-3.1-flash-lite

Run any bot:
1. Open a terminal inside that bot folder.
2. Create/activate a virtual environment if desired.
3. Install: pip install -r requirements.txt
4. Put your Gemini API key in .env
5. Run: python app.py
6. Open http://127.0.0.1:5000

Production:
gunicorn app:app

Folders:
01_ECommerceBot
02_TravelBot
03_MedicineBot
04_MovieBot
05_SportsBot
06_StudyBot
07_TechBot
08_VehicleBot
09_FoodBot
10_WatchBot
