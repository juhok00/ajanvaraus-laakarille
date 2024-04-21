python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
psql < schema.sql


export FLASK_APP=app.py
export FLASK_ENV=development

flask run