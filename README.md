# tradetheta.io

Trading site to provide stock/options trending suggestions from reddit and aggregate real-time stock/options/cryptocurrency information 

<div align="center">
  <img src="https://tradetheta.s3-us-west-1.amazonaws.com/theta1.PNG" height="800">
</div>


## Table of Contents

1. [Usage](#Usage)
2. [Requirements](#requirements)
3. [Development](#development)
4. [Installing Dependencies](#dependencies) 
5. [API Endpoints](#endpoints)

## Usage

• Access the app through app/react-app

## Requirements

- Python 3.8
- Node 6.13.0

## Development

Developed using Python and create-react-app. To start a development bundle and server, navigate to app/react-app and run:

```sh
npm run start
npm run start-flask-api
npm run build
```

## Installing Dependencies

From within the root directory:

```sh
npm install
```

## API Endpoints

API endpoints conform to a RESTful API architecture to retrieve and modify database-hosted information. All responses will include HTTP response codes to indicate status and errors and data will come in JSON. All requests must include a Content-Type of application/json and the body must be valid JSON.

**```GET``` /api**
• ```GET``` request for home page
• No request object is required
• Successful response code: ```200```
• The default stock information will always be Tesla's 30-min chart.
• Response will be a JSON object that contains the following information:

```sh
[ 
  [
   weighted popularity Decimal, 
   comments Integer, 
   upvotes Integer, 
   ticker String, 
   count Integer
  ],
  [
   stockCode (String), 
   timestamp (time object),
   ticker symbol (String),
   historical price [{
   'open': decimal,
   'close': decimal,
   'high': decimal,
   'low': decimal,
   'volume': integer,
   't': time since Unix epoch,
   }]
   priceFactor (Integer),
   timePeriod (String),
   barLength (Number in seconds),
   time period (String)
  ],
  [
   timestamp Date object,
   asset_id_quote String,
   price Decimal
  ]
]
```

**GET /api/v1/quotes/:cryptoid**
• GET request for crypto prices
• Successful response code: ```200```
• Request parameter of :cryptoid from API endpoint will be accepted. No request object is required.
• Response will be a JSON object that contains historical prices information vs USD for the respective crypto:

```sh
  [
   timestamp Date object,
   asset_id_quote String,
   price Decimal
  ]
```

**GET /api/v1/quotes/stocks**
• GET request for landing page
• Successful response code: ```200```
• Request parameter of :listingid from API endpoint will be accepted. No request object is required.
• Response will be a JSON object that contains the following information:
```sh
[
  stockCode (String), 
  timestamp (time object),
  ticker symbol (String),
  historical price [{
  'open': decimal,
  'close': decimal,
  'high': decimal,
  'low': decimal,
  'volume': integer,
  't': time since Unix epoch,
  }]
  priceFactor (Integer),
  timePeriod (String),
  barLength (Number in seconds),
  time period (String)
]
```

**GET /api/v1/quotes/autosuggest**
• GET request for landing page
• Successful response code: ```200```
• Request parameter of :listingid from API endpoint will be accepted. No request object is required.
• Response will be a JSON object that contains an array of available tickers. For example, if the request was for 'AM', results would be:
```sh
[
 'AMAT',
 'AMD',
 'AMGN',
 'AMZN'
]
```

