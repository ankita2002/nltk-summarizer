#Create Environment
python -m venv env
#Run Environment (Activate)
(Open CMD) env\Scripts\activate.bat 

(Download req in virtual Env) pip install -r req.txt
#Remove Environmet

pip freeze - req.txt

heroku create extracsum-app
