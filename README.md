# Coworking-space-manager
App to help anyone make the most of coworking spaces of all kinds

## Problem solved
Organising and participating at coworking spaces can always be very difficult so we built a platform to streamline organisation and access.

## Solution
A one stop platform for all your coworking needs.

## Common use cases for this platform
- Book seats/rooms
- Be able to see locations with 360 images
- Manage multiple locations
- Allow for booking of extra assets such as screens
- Allow users to bid automatically on seats for maximum utilisation
- See all your transactions for reporting and accounting purposes

## Accessibility
Runs on low powered hardware, that is IOT connected so can be easily setup as long as there is an internet connection

## Tech stack used
- Python & Flask for the backend
- Datta Able design system to make the interface
- Foundry's Anvil for generating mock testnet
- Web3 for test transactions and posting data
- MagTag for Room/Desk booking display with neopixel LEDs for lighting

## Bounties 
The following bounties were targeted

- Build on the Pear Execution API
	- Wanted to generate the dynamic execution pricing based of off the tooling but ran out of time
- Hyperliquid Trade Ledger API
	- Wanted for the transaction history of past bookings to be able to track the transactions this way but also ran out of time

I will be looking to continue with this project going forward

Please note that
- Demo requests are welcome
- It was a 1 person team
- We had little/no experience with the following before the hackathon
	- Building and using the MagTag
	- Using the Datta Able design system
	- Getting started with foundry & Web3.py

## Installation
- Install Rust & foundry
- Install Python
- Change directory to App folder & run with the environment activated

## Environment activation

```
source env/bin/activate
cd App
python app.py
```

[localhost:5000](http://localhost:5000)

## Demo

https://youtu.be/Tn96gUro8tU