from flask import Flask, render_template_string
import os
from utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def display_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read().strip()
            user_score = content.split('=')[-1].strip()  # Assuming the format is POINTS_OF_WINNING = SCORE
            return render_template_string('''
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>The Score Is:</h1>
                        <div id="score">{{ score }}</div>
                    </body>
                </html>
            ''', score=user_score)
    except Exception as e:
        return render_template_string('''
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>
                    <div id="score" style="color:red">{{ error }}</div>
                </body>
            </html>
        ''', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
