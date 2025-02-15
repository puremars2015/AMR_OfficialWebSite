from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 新增六個頁面的路由
@app.route('/core-values')
def core_values():
    return render_template('core-values.html')

@app.route('/company-story')
def company_story():
    return render_template('company-story.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)