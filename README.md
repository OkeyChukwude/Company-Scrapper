# Company Scrapper
Project developed by [Okechukwu Chukwude](https://github.com/OkeyChukwude) and [Habeeb Agbaje](https://github.com/Hab-eeb) for  the Global Data Competition by [Innoscripta](https://www.innoscripta.com/en). The project uses the [SERP API](https://serpapi.com/), [OPENAPI](https://platform.openai.com/overview) and [SERPER API](https://serper.dev/dashboard). 


## Prerequisites
Before you begin, ensure you have the following prerequisites:
-  Python 3.8 or above installed on your machine.
-  SERPAPI API Key
-  OPENAPI API Key
-  SERPER API Key

__NOTE:__ If the free version of the APIs above is used, the number of company searches that can be made is quite limited due to the limited number of API calls on the free version of these APIs. 

## Installation
Follow these steps to set up this project on your local machine:

1. Clone the repository:
 ```shell
   git clone https://github.com/OkeyChukwude/Company-Scrapper.git
```

2. Change to the project directory:
```shell
cd Company-Scrapper
```

3. Create and activate a virtual environment:
```shell
python3 -m venv venv
source venv/bin/activate
```
On Windows Machine try
```shell
python3 -m venv venv
source venv/scripts/activate
```

4. Install the dependencies:
```shell
pip install -r requirements.txt
```
## Configuration
The project uses environment variables for configuration. Create a `.env` file in the project root directory and add the following settings:
```
OPENAI_API_KEY=<YOUR OPEN API KEY>
SERPAPI_API_KEY=<YOUR SERP API KEY>
SECRET_KEY=<YOUR APP SECRET>
SERPER_API_KEY=<YOUR SERPER API KEY>
```
Make sure to replace `<YOUR OPEN API KEY>`, `<YOUR SERP API KE`, `<YOUR APP SECRET>` and `<YOUR SERPER API KEY>` with appropriate values.

## Usage
To start the development server, run the following command:

```bash
flask run
```
Access the UI in your web browser at http://localhost:5000.

To access the endpoint, send a POST request to `http://127.0.0.1:5000/scarpe` with the following payload

```
{
    "name": "<Company Name>",
    "country": "<Company Country>"
    "url": "<Company URL>"
}
```
__NOTE:__ The company url is optional.

You can use `curl` to make a POST request to the API endpoint with the following command:
```
curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Apple Inc.",
    "country": "US"
}' http://localhost:5000/scrape
```

## File Structure
The project has the following file structure:
```
company-scrapper/
├── static/
|   ├── img/
|       ├── loading.gif
|       └── ...
|   ├── js
|       ├── app.js
|       └── ...
├── templates
|   ├── index.html
|   └── ...
├── __init__.py
├── .env
├── .gitignore
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── scrapper.py
└── ...

```

## Contact
For any questions or suggestions, please reach out to [Okechukwu Chukwude](https://github.com/OkeyChukwude) or [Habeeb Agbaje](https://github.com/Hab-eeb)
