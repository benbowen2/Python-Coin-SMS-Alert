# Python Coin SMS Alert

A small script to check coin prices every 10 seconds(default) on https://www.coinmarketcap.com.

### Install and Run

```bash
pip install -r requirements.txt
cp config-example.py config.py
```

Input your https://twilio.com credentials into the config.py file

``` bash
python alert.py
```

### Twilio Setup

1. Setup a Project with Twilio 
2. Add Programmable SMS to the project
3. Add Phone Numbers(I think...)
2. Get a number, the free one is fine for most cases
3. Add the account info to the config.py file
