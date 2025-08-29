# Currency Converter API Service
This service was tested for follow currencies:

* **USD** 
* **GBP** 
* **EUR**
* **PLN**


## Functional requirements
* User should be able to send GET requests to the Currency Converter REST API

## Non-functional requirements
* assume that FX rates are changing once an hour.

## Requirements
* Python 3.12
* python packages from `requirements.txt`

## How to run
1. Re-create and activate python environment.
2. go to `src/` and run `python main.py`
3. Open in browser `http://127.0.0.1:8000/docs#`

## example
```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/currency/converter?ccy_from=USD&ccy_to=GBP&quantity=1000' \
  -H 'accept: application/json'
```

Output:
```json
{
  "quantity": 742.26,
  "ccy": "GBP"
}
```