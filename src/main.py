import uvicorn

from currency_converter_rest_api.app import app

if __name__ == "__main__":
    uvicorn.run(app, log_level="trace")
