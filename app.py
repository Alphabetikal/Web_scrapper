from flask import Flask, render_template, request,flash
import requests

app = Flask(__name__, template_folder='./')
app.secret_key='alphabetikal232'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    url = request.form.get('url')

    try:
        if not url.startswith('http'):
            flash('URL must Start with an https://')


        data = requests.get(url).text

        return render_template('index.html', result=data)

    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)