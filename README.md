# hng-devops-stage1
This API takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Technology Stack

- Python (Django)
- Deployed to an Azure App Service
- Handles CORS (Cross-Origin Resource Sharing)
- Returns responses in JSON format

## API Specification

### Endpoint: **GET** /api/classify-number?number=371

#### Required JSON Response Format (200 OK):

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Required JSON Response Format (400 Bad Request):
{
    "number": "alphabet",
    "error": true
}
 
