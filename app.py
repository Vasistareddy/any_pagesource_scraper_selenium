import os
from flask import Flask, jsonify, make_response, request
from selenium import webdriver

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def get_html(url):
    status = True
    html = ''
    fp = webdriver.FirefoxProfile()
    # fp.set_preference("network.proxy.http", "<proxy ip>")
    # fp.set_preference("network.proxy.http_port", "<proxy port")
    driver = webdriver.Firefox(firefox_profile=fp)
    try:
        driver.set_page_load_timeout(15)
        driver.get(url)
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        if len(html.split(' '))<100:
            status = False
        driver.quit()
    except:
        status = False
        driver.quit()
    return status, html

# Give proper 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# html API
@app.route('/pagesource', methods=['GET'])
def page_source():
    if request.method == 'GET':
        url = request.args.get('url')  
        status, html = get_html(url)
        if html and status:
            return jsonify({'status_code': 200, 'pageSource': html})
    return make_response(jsonify({'error':'unable to parse the url, try using proxy', 'status_code':500}), 500)
