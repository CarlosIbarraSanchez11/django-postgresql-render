Backend:
python -m venv venv
source venv/Scripts/activate

cd backend
pip install django
pip install -r requirements.txt
pip install psycopg2
pip install setuptools
python manage.py migrate
python manage.py makemigrations

Frontend:
npm i
npm install -g npm (si no llega a crearse el node_modules)
npm run dev


