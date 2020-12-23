# The PEP 484 type hints stub file for the QtNetworkAuth module.
#
# Generated by SIP 5.4.0
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

from PyQt5 import sip
from PyQt5 import QtNetwork
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QAbstractOAuth(QtCore.QObject):

    class ContentType(int):
        WwwFormUrlEncoded = ... # type: 'QAbstractOAuth.ContentType'
        Json = ... # type: 'QAbstractOAuth.ContentType'

    class Error(int):
        NoError = ... # type: 'QAbstractOAuth.Error'
        NetworkError = ... # type: 'QAbstractOAuth.Error'
        ServerError = ... # type: 'QAbstractOAuth.Error'
        OAuthTokenNotFoundError = ... # type: 'QAbstractOAuth.Error'
        OAuthTokenSecretNotFoundError = ... # type: 'QAbstractOAuth.Error'
        OAuthCallbackNotVerified = ... # type: 'QAbstractOAuth.Error'

    class Stage(int):
        RequestingTemporaryCredentials = ... # type: 'QAbstractOAuth.Stage'
        RequestingAuthorization = ... # type: 'QAbstractOAuth.Stage'
        RequestingAccessToken = ... # type: 'QAbstractOAuth.Stage'
        RefreshingAccessToken = ... # type: 'QAbstractOAuth.Stage'

    class Status(int):
        NotAuthenticated = ... # type: 'QAbstractOAuth.Status'
        TemporaryCredentialsReceived = ... # type: 'QAbstractOAuth.Status'
        Granted = ... # type: 'QAbstractOAuth.Status'
        RefreshingToken = ... # type: 'QAbstractOAuth.Status'

    @staticmethod
    def generateRandomString(length: int) -> QtCore.QByteArray: ...
    def resourceOwnerAuthorization(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def callback(self) -> str: ...
    def setStatus(self, status: 'QAbstractOAuth.Status') -> None: ...
    def replyDataReceived(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def finished(self, reply: QtNetwork.QNetworkReply) -> None: ...
    def granted(self) -> None: ...
    def authorizeWithBrowser(self, url: QtCore.QUrl) -> None: ...
    def requestFailed(self, error: 'QAbstractOAuth.Error') -> None: ...
    def contentTypeChanged(self, contentType: 'QAbstractOAuth.ContentType') -> None: ...
    def extraTokensChanged(self, tokens: typing.Dict[str, typing.Any]) -> None: ...
    def authorizationUrlChanged(self, url: QtCore.QUrl) -> None: ...
    def statusChanged(self, status: 'QAbstractOAuth.Status') -> None: ...
    def tokenChanged(self, token: str) -> None: ...
    def clientIdentifierChanged(self, clientIdentifier: str) -> None: ...
    def grant(self) -> None: ...
    def prepareRequest(self, request: QtNetwork.QNetworkRequest, verb: typing.Union[QtCore.QByteArray, bytes, bytearray], body: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> None: ...
    def setContentType(self, contentType: 'QAbstractOAuth.ContentType') -> None: ...
    def contentType(self) -> 'QAbstractOAuth.ContentType': ...
    def setModifyParametersFunction(self, modifyParametersFunction: typing.Callable[..., None]) -> None: ...
    def modifyParametersFunction(self) -> typing.Callable[..., None]: ...
    def deleteResource(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def put(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def post(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def get(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def head(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def setReplyHandler(self, handler: 'QAbstractOAuthReplyHandler') -> None: ...
    def replyHandler(self) -> 'QAbstractOAuthReplyHandler': ...
    def extraTokens(self) -> typing.Dict[str, typing.Any]: ...
    def setAuthorizationUrl(self, url: QtCore.QUrl) -> None: ...
    def authorizationUrl(self) -> QtCore.QUrl: ...
    def status(self) -> 'QAbstractOAuth.Status': ...
    def setNetworkAccessManager(self, networkAccessManager: QtNetwork.QNetworkAccessManager) -> None: ...
    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def setToken(self, token: str) -> None: ...
    def token(self) -> str: ...
    def setClientIdentifier(self, clientIdentifier: str) -> None: ...
    def clientIdentifier(self) -> str: ...


class QAbstractOAuth2(QAbstractOAuth):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setResponseType(self, responseType: str) -> None: ...
    def authorizationCallbackReceived(self, data: typing.Dict[str, typing.Any]) -> None: ...
    def error(self, error: str, errorDescription: str, uri: QtCore.QUrl) -> None: ...
    def expirationAtChanged(self, expiration: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    def stateChanged(self, state: str) -> None: ...
    def clientIdentifierSharedKeyChanged(self, clientIdentifierSharedKey: str) -> None: ...
    def responseTypeChanged(self, responseType: str) -> None: ...
    def refreshTokenChanged(self, refreshToken: str) -> None: ...
    def userAgentChanged(self, userAgent: str) -> None: ...
    def scopeChanged(self, scope: str) -> None: ...
    def setRefreshToken(self, refreshToken: str) -> None: ...
    def refreshToken(self) -> str: ...
    def expirationAt(self) -> QtCore.QDateTime: ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...
    def setClientIdentifierSharedKey(self, clientIdentifierSharedKey: str) -> None: ...
    def clientIdentifierSharedKey(self) -> str: ...
    def responseType(self) -> str: ...
    def setUserAgent(self, userAgent: str) -> None: ...
    def userAgent(self) -> str: ...
    def setScope(self, scope: str) -> None: ...
    def scope(self) -> str: ...
    def deleteResource(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def put(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def put(self, url: QtCore.QUrl, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def put(self, url: QtCore.QUrl, multiPart: QtNetwork.QHttpMultiPart) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: QtCore.QUrl, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: QtCore.QUrl, multiPart: QtNetwork.QHttpMultiPart) -> QtNetwork.QNetworkReply: ...
    def get(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def head(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def createAuthenticatedUrl(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtCore.QUrl: ...


class QAbstractOAuthReplyHandler(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def callbackDataReceived(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def replyDataReceived(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def tokensReceived(self, tokens: typing.Dict[str, typing.Any]) -> None: ...
    def callbackReceived(self, values: typing.Dict[str, typing.Any]) -> None: ...
    def networkReplyFinished(self, reply: QtNetwork.QNetworkReply) -> None: ...
    def callback(self) -> str: ...


class QOAuth1(QAbstractOAuth):

    class SignatureMethod(int):
        Hmac_Sha1 = ... # type: 'QOAuth1.SignatureMethod'
        Rsa_Sha1 = ... # type: 'QOAuth1.SignatureMethod'
        PlainText = ... # type: 'QOAuth1.SignatureMethod'

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, clientSharedSecret: str, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    @staticmethod
    def generateAuthorizationHeader(oauthParams: typing.Dict[str, typing.Any]) -> QtCore.QByteArray: ...
    @staticmethod
    def nonce() -> QtCore.QByteArray: ...
    @typing.overload
    def setup(self, request: QtNetwork.QNetworkRequest, signingParameters: typing.Dict[str, typing.Any], operation: QtNetwork.QNetworkAccessManager.Operation) -> None: ...
    @typing.overload
    def setup(self, request: QtNetwork.QNetworkRequest, signingParameters: typing.Dict[str, typing.Any], operationVerb: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def requestTokenCredentials(self, operation: QtNetwork.QNetworkAccessManager.Operation, url: QtCore.QUrl, temporaryToken: typing.Tuple[str, str], parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def requestTemporaryCredentials(self, operation: QtNetwork.QNetworkAccessManager.Operation, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def tokenCredentialsUrlChanged(self, url: QtCore.QUrl) -> None: ...
    def temporaryCredentialsUrlChanged(self, url: QtCore.QUrl) -> None: ...
    def tokenSecretChanged(self, token: str) -> None: ...
    def clientSharedSecretChanged(self, credential: str) -> None: ...
    def signatureMethodChanged(self, method: 'QOAuth1.SignatureMethod') -> None: ...
    def continueGrantWithVerifier(self, verifier: str) -> None: ...
    def grant(self) -> None: ...
    def deleteResource(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def put(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def post(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def get(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def head(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> QtNetwork.QNetworkReply: ...
    def setSignatureMethod(self, value: 'QOAuth1.SignatureMethod') -> None: ...
    def signatureMethod(self) -> 'QOAuth1.SignatureMethod': ...
    def setTokenCredentialsUrl(self, url: QtCore.QUrl) -> None: ...
    def tokenCredentialsUrl(self) -> QtCore.QUrl: ...
    def setTemporaryCredentialsUrl(self, url: QtCore.QUrl) -> None: ...
    def temporaryCredentialsUrl(self) -> QtCore.QUrl: ...
    @typing.overload
    def setTokenCredentials(self, tokenCredentials: typing.Tuple[str, str]) -> None: ...
    @typing.overload
    def setTokenCredentials(self, token: str, tokenSecret: str) -> None: ...
    def tokenCredentials(self) -> typing.Tuple[str, str]: ...
    def setTokenSecret(self, tokenSecret: str) -> None: ...
    def tokenSecret(self) -> str: ...
    @typing.overload
    def setClientCredentials(self, clientCredentials: typing.Tuple[str, str]) -> None: ...
    @typing.overload
    def setClientCredentials(self, clientIdentifier: str, clientSharedSecret: str) -> None: ...
    def clientCredentials(self) -> typing.Tuple[str, str]: ...
    def setClientSharedSecret(self, clientSharedSecret: str) -> None: ...
    def clientSharedSecret(self) -> str: ...


class QOAuth1Signature(sip.simplewrapper):

    class HttpRequestMethod(int):
        Head = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Get = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Put = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Post = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Delete = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Custom = ... # type: 'QOAuth1Signature.HttpRequestMethod'
        Unknown = ... # type: 'QOAuth1Signature.HttpRequestMethod'

    @typing.overload
    def __init__(self, url: QtCore.QUrl = ..., method: 'QOAuth1Signature.HttpRequestMethod' = ..., parameters: typing.Dict[str, typing.Any] = ...) -> None: ...
    @typing.overload
    def __init__(self, url: QtCore.QUrl, clientSharedKey: str, tokenSecret: str, method: 'QOAuth1Signature.HttpRequestMethod' = ..., parameters: typing.Dict[str, typing.Any] = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QOAuth1Signature') -> None: ...

    def setCustomMethodString(self, verb: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def customMethodString(self) -> QtCore.QByteArray: ...
    def swap(self, other: 'QOAuth1Signature') -> None: ...
    @typing.overload  # type: ignore[misc]
    def plainText(self) -> QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def plainText(clientSharedSecret: str, tokenSecret: str) -> QtCore.QByteArray: ...
    def rsaSha1(self) -> QtCore.QByteArray: ...
    def hmacSha1(self) -> QtCore.QByteArray: ...
    def setTokenSecret(self, secret: str) -> None: ...
    def tokenSecret(self) -> str: ...
    def setClientSharedKey(self, secret: str) -> None: ...
    def clientSharedKey(self) -> str: ...
    def value(self, key: str, defaultValue: typing.Any = ...) -> typing.Any: ...
    def take(self, key: str) -> typing.Any: ...
    def keys(self) -> typing.List[str]: ...
    def insert(self, key: str, value: typing.Any) -> None: ...
    def addRequestBody(self, body: QtCore.QUrlQuery) -> None: ...
    def setParameters(self, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def parameters(self) -> typing.Dict[str, typing.Any]: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def setHttpRequestMethod(self, method: 'QOAuth1Signature.HttpRequestMethod') -> None: ...
    def httpRequestMethod(self) -> 'QOAuth1Signature.HttpRequestMethod': ...


class QOAuth2AuthorizationCodeFlow(QAbstractOAuth2):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, authorizationUrl: QtCore.QUrl, accessTokenUrl: QtCore.QUrl, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, authorizationUrl: QtCore.QUrl, accessTokenUrl: QtCore.QUrl, manager: QtNetwork.QNetworkAccessManager, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def resourceOwnerAuthorization(self, url: QtCore.QUrl, parameters: typing.Dict[str, typing.Any] = ...) -> None: ...
    def requestAccessToken(self, code: str) -> None: ...
    def buildAuthenticateUrl(self, parameters: typing.Dict[str, typing.Any] = ...) -> QtCore.QUrl: ...
    def accessTokenUrlChanged(self, accessTokenUrl: QtCore.QUrl) -> None: ...
    def refreshAccessToken(self) -> None: ...
    def grant(self) -> None: ...
    def setAccessTokenUrl(self, accessTokenUrl: QtCore.QUrl) -> None: ...
    def accessTokenUrl(self) -> QtCore.QUrl: ...


class QOAuthOobReplyHandler(QAbstractOAuthReplyHandler):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def networkReplyFinished(self, reply: QtNetwork.QNetworkReply) -> None: ...
    def callback(self) -> str: ...


class QOAuthHttpServerReplyHandler(QOAuthOobReplyHandler):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, port: int, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, address: typing.Union[QtNetwork.QHostAddress, QtNetwork.QHostAddress.SpecialAddress], port: int, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def isListening(self) -> bool: ...
    def close(self) -> None: ...
    def listen(self, address: typing.Union[QtNetwork.QHostAddress, QtNetwork.QHostAddress.SpecialAddress] = ..., port: int = ...) -> bool: ...
    def port(self) -> int: ...
    def setCallbackText(self, text: str) -> None: ...
    def callbackText(self) -> str: ...
    def setCallbackPath(self, path: str) -> None: ...
    def callbackPath(self) -> str: ...
    def callback(self) -> str: ...
