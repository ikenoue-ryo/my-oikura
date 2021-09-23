import time
import jwt
from restapi.settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions

from myapp.models import User


class NormalAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        name = request._request.POST.get('name')
        password = request._request.POST.get('password')
        user_obj = User.objects.filter(name=name).first()
        if not user_obj:
            raise exceptions.AuthenticationFailed('認証失敗')
        elif user_obj.password != password:
            raise exceptions.AuthenticationFailed('パスワードが間違っています')
        token = generate_jwt(user_obj)
        return (token, None)

    def authenticate_header(self, request):
        pass


def generate_jwt(user):
    timestamp = int(time.time()) + 60 * 60 * 24 * 7
    return jwt.encode(
        {"userid": user.pk, "name": user.name, "info": user.info, "exp": timestamp},
        SECRET_KEY).decode("utf-8")


class JWTAuthentication(BaseAuthentication):
    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = "Authorization 無効"
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Authorization 無効 スペースはない"
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, SECRET_KEY)
            userid = jwt_info.get("userid")
            try:
                user = User.objects.get(pk=userid)
                user.is_authenticated = True
                return (user, jwt_token)
            except:
                msg = "ユーザー存在しません"
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = "tokenはタイムアウトしました"
            raise exceptions.AuthenticationFailed(msg)

    def authenticate_header(self, request):
        pass
