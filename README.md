# Go through the following steps to run the application:

1) Create Python Virtual Env from your root directory
python -m venv venv

2) Activate Virtual Env
a) Windows: venv\Scripts\activate.bat
b) Unix: source venv/bin/activate

3) Installing Dependencies
pip install -r requirements.txt

4) Setup OPENAI_API_KEY from terminal
set LANGCHAIN_API_KEY=<your-langsmith-key>
set OPENAI_API_KEY=<your-api-key>

5) Run the DB Files to create DB Locally
python -m db.create_and_write_in_product_db
python -m db.create_memory_db

6) Running the Streamlit Application
streamlit run app.py