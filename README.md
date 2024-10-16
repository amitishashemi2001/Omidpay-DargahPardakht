# OmidPay API Documentation

## Overview

**Title**: OmidPay API  
**Description**: API documentation for OmidPay integration  
**Version**: v1  

**Host**: 185.243.48.110 
**Base Path**: `/api`  
**Schemes**: 
- HTTP  

## Consumes
- `application/json`

## Produces
- `application/json`

## Security

### Security Definitions

**Basic Authentication**  
- Type: `basic`

## Endpoints

### 1. Generate Token

**POST** `/get-token/`

- **Description**: Generate an OmidPay token.
- **Operation ID**: `get-token_create`
- **Parameters**:
  - **data** (body, required):
    - **amount** (integer, required): Payment amount

- **Responses**:
  - `200`: Token generated successfully.
  - `500`: Internal server error

- **Tags**: `get-token`



### 2. Handle Payment Callback

**POST** `/success/`

- **Description**: Handle OmidPay payment callback.
- **Operation ID**: `success_create`
- **Parameters**:
  - **data** (body, required):
    - **ResNum** (string, required): Reservation number
    - **UserId** (string): User ID
    - **RefNum** (string): Reference number

- **Responses**:
  - `200`: Payment success page rendered.
  - `404`: Token not found

- **Tags**: `success`

### 3. Verify Transaction

**POST** `/verify-transaction/`

- **Description**: Verify an OmidPay transaction.
- **Operation ID**: `verify-transaction_create`
- **Parameters**:
  - **data** (body, required):
    - **RefNum** (string, required): Reference number
    - **token** (string, required): OmidPay token
    - **ResNum** (string, required): Reservation number

- **Responses**:
  - `200`: Verification successful.
  - `500`: Verification failed

- **Tags**: `verify-transaction`

## Definitions
There are no additional definitions for this API.

