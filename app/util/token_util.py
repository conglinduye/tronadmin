# !/usr/bin/env python
# *-* coding:utf-8 *-*

from functools import wraps
from M2Crypto.EVP import Cipher
from app.model.tr_admin_user_token import TRAdminToken

KEY = '95225931737254654643090323667081'
IV = '61818371293345548725265487958900'
COOKIE_NAME = 'dapp_accounts_token'
TLL = 30*60


def encode(s, key, iv):
    cipher = Cipher(alg='aes_128_cbc', key=key, iv=iv, op=1)
    cipher.set_padding(padding=1)
    v = cipher.update(s)
    v += cipher.final()
    return v

def generate(user):
    seed = str(random.randint(10**31, 10**32))
    token = encode(seed, KEY, IV)
    token = token.encode('hex')
    expires = int(time.time()) + TTL
    token = TRAdminToken(token=token, expires=expires, admin_uid=user.id)
    db.session.add(token)
    db.session.commit()
    return token
 
def token_required(func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get(COOKIE_NAME)
        token = TRAdminToken.query.filter_by(token=token).first()
        if token is None:
            return jsonify({'status': 'fail', 'msg': 'useless token'}), 403
        elif token.expires < time.time():
            return jsonify({'status': 'fail', 'msg': 'expired token'}), 403
    return wrapper
