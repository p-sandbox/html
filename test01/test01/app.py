from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static_analysis')
def static_analysis_page():
    return render_template('static_analysis.html')

@app.route('/dynamic_analysis')
def dynamic_analysis_page():
    return render_template('dynamic_analysis.html')  # dynamic_analysis.html 파일 로드

@app.route('/api_documentation')
def api_documentation():
    return render_template('api_documentation.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
