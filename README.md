# tradetheta.io

Trading site to provide stock/options trending suggestions from reddit and aggregate real-time stock/options/cryptocurrency information 

## Table of Contents

1. [Usage](#Usage)
2. [Requirements](#requirements)
3. [Development](#development)
4. [Installing Dependencies](#dependencies) 
5. [API Endpoints](#endpoints)

## Usage


## Requirements

An `nvmrc` file is included if using [nvm](https://github.com/creationix/nvm).

- Python 3.8
- Node 6.13.0

## Development

## Installing Dependencies

From within the root directory:

```sh
npm install
npm run start
npm run build
```

## API Endpoints

API endpoints conform to a RESTful API architecture to retrieve and modify database-hosted information. All responses will include HTTP response codes to indicate status and errors and data will come in JSON pretty format. All requests must include a Content-Type of application/json and the body must be valid JSON.

**GET /api/listings/:listingid**
- GET request for a single listing
- Request parameter of :listingid from API endpoint will be accepted. No request object is required.
- Response will be HTTP status code 200 and a JSON object that contains property at the given ID with respective fees and all booked reservation dates
``
