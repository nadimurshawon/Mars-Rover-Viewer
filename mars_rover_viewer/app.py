from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

NASA_API_KEY = 'UQVvlCZHaFH0KthdcDPOH4YlLh62F7BgjroHRf1n'  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        
        return redirect(url_for('photos', date=date))
    
    return render_template('index.html')

@app.route('/photos')
def photos():
    date = request.args.get('date')
    photos = []
    if date:
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        params = {
            'earth_date': date,
            'api_key': NASA_API_KEY
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            photos = data.get('photos', [])
    return render_template('photos.html', photos=photos, date=date)

if __name__ == '__main__':
    app.run(debug=True)
