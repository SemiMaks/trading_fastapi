from fastapi import FastAPI

app = FastAPI(
    title='TradingApp'
)


@app.get('/')
def hello():
    return 'Привет!'


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'}
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.15},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.19},
    {'id': 3, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 120, 'amount': 2.10},
]


@app.get('/users/{user_id}')
def users(user_id: int):
    # return user_id
    return [users for users in fake_users if users.get('id') == user_id]


# @app.get('/trades/')
# def get_trades(limit: int = 10, offset: int = 10):
#     return fake_trades[offset:][:limit]

