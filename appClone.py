from flask import Flask
from selenium import webdriver

# Initialize Flask
app = Flask(__name__)

# Initialize Seleniun
try:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
except:
    pass


@app.route('/')
def hello():
    return 'Hello, its working'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)