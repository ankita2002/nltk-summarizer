# nltk-summarizer

Keywords: Flask, NLTK, Sumy, Extractive Text Summarization.

### Installation
1. Create a virtual environment.
```
python -m venv env
```
2. Run Environment (Activate)
```
env\Scripts\activate.bat 
```
3. Install dependencies from `requirements.txt`.
```
pip install -r requirements.txt
```

### Usage
Run the project
```
python app/main.py
```
The project should open on [127.0.0.1:8000](http://127.0.0.1:8000).
![image](https://user-images.githubusercontent.com/65420449/182130205-4e7fcd9f-08fd-43bf-8f73-a96e3cb15954.png)


#### A live version of the project is hosted at <https://nltk-summarizer.herokuapp.com/>

### Approach
The application accepts a text input and a `length` parameter between 0 and 1. It uses the `sumy` library to get Parser, Tokenizer and Stemmer classes. After extracting the sentences from the text, it only returns a percentage of the text which depends on `length`. 
To host the application, Flask framework is used.
