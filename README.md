# Knowledge-Sharing-App

To create a virtual environment

py -3 -m venv <venv name>

Select the Virtual Environment in your CMD
<Venv name>\Scripts\activate.bat

Run the App
uvicorn main:app --reload --port 3000

After shifting main.py to app directory
uvicorn app.main:app --reload --port 3000
