# Number Classification API

## Description
An API that takes a number as input and returns its mathematical properties along with a fun fact.

## Endpoints
- **GET /api/classify-number?number=<number>**
  - Returns JSON with properties of the number.
  - Example: `/api/classify-number?number=371`

## Response Format
### Success (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error (400 Bad Request)
```
{
  "number": "alphabet",
  "error": true
}
```

