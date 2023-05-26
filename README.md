# Company Scrapper
Project developed by [Okechukwu Chukwude](https://github.com/OkeyChukwude) amd [Habeeb Agbaje](https://github.com/Hab-eeb) for  the Global Data Competition by [Innoscripta](https://www.innoscripta.com/en). The project uses the [SERP API](https://serpapi.com/) and [OPENAPI](https://platform.openai.com/overview). 

__NOTE:__ You''ll need to obtain API KEYs for SERPAPI and OPENAPI. If the free version is used, the number of company searches that can be made is quite limited due to the limited number of API calls on the free version of these APIs. 

# Installation
Create a `.env` file in the root directory of the project, input the followng into it and save.
```
OPENAI_API_KEY=<YOUR OPEN API KEY>
SERPAPI_API_KEY=<YOUR SERP API KEY>
SECRET_KEY=<YOUR APP SECRET>
```
Create and activate a virtual environment and run the command below.
```bash
pip install -r requirements.txt
```

# Usage

Run the command
```bash
flask run
```

## Access the UI
Visit `http://127.0.0.1:5000/` in a browser.

## API Endpoint
Send a POST request to `http://127.0.0.1:5000/scarpe` with the following payload

```
{
    "name": "<Company Name>",
    "country": "<Company Country>"
    "url": "<Company URL>"
}
```

__NOTE:__ The company url is optional.