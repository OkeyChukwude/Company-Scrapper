from flask import Flask, render_template, request, abort, jsonify
from .scrapper import scrape
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"message": 'Bad request. Company name and country are required.', 'status': 'Error'}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def search():
    company_name = request.json.get('name')
    country = request.json.get('country')
    
    company_url = request.json.get('url')

    if not company_name or not country :
        abort(400)

    scrape_response = scrape(company_name, country)

    if scrape_response == 'There was an error. Try again!':
        return jsonify({'message': 'There was an error. Try again!', 'status': 'Error'}), 500
    
    print(scrape_response[0])
    description = scrape_response[0]['Description']
    keywords = scrape_response[0]['Keywords']
    products = scrape_response[0]['Products'] if (scrape_response[0]['Products'] == 'No products') else list(map(lambda item: item.lstrip(), scrape_response[0]['Products'] if (type(scrape_response[0]['Products']) is list) else scrape_response[0]['Products'].split(', ')))
    services = scrape_response[0]['Services'] if (scrape_response[0]['Services'] == 'No services') else list(map(lambda item: item.lstrip(), scrape_response[0]['Services'] if (type(scrape_response[0]['Services']) is list) else scrape_response[0]['Services'].split(', ')))

    sic_specification = [scrape_response[1], scrape_response[4]]
    niac_specification = [scrape_response[2], scrape_response[3]]

    return jsonify({'description': description, 'keywords': keywords, 'products': products, 'services': services, "SIC Specifications": sic_specification, "NIAC Specifications": niac_specification, 'status':'Success'}), 200
