import typing

import httpx
from httpx.auth import AuthTypes
from httpx.config import (
    UNSET,
    TimeoutTypes,
    UnsetType,
)
from httpx.models import (
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestData,
    RequestFiles,
    Response,
    URLTypes,
)

from . import model


class GPACalculationException(Exception):
    pass


class SessionException(Exception):
    pass


class ServiceUnavailable(Exception):
    pass


class Session:
    _client: httpx.Client
    _retry: list

    def _secure_req(self, ref):
        pass

    @staticmethod
    def _http_error_handler(response: httpx.Response):
        pass

    def __init__(self, retry=None):
        pass

    def get(
            self,
            url: URLTypes,
            *,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def options(
            self,
            url: URLTypes,
            *,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def head(
            self,
            url: URLTypes,
            *,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = False,  # NOTE: Differs to usual default.
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def post(
            self,
            url: URLTypes,
            *,
            data: RequestData = None,
            files: RequestFiles = None,
            json: typing.Any = None,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def put(
            self,
            url: URLTypes,
            *,
            data: RequestData = None,
            files: RequestFiles = None,
            json: typing.Any = None,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def patch(
            self,
            url: URLTypes,
            *,
            data: RequestData = None,
            files: RequestFiles = None,
            json: typing.Any = None,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def delete(
            self,
            url: URLTypes,
            *,
            params: QueryParamTypes = None,
            headers: HeaderTypes = None,
            cookies: CookieTypes = None,
            auth: AuthTypes = None,
            allow_redirects: bool = True,
            timeout: typing.Union[TimeoutTypes, UnsetType] = UNSET,
    ) -> Response:
        pass

    def login(self, username, password):
        pass

    def load(self, fn):
        pass

    def dump(self, fn):
        pass

    @property
    def proxies(self):
        pass

    @proxies.setter
    def proxies(self, new_proxy: list):
        pass

    @property
    def cookies(self):
        pass

    @cookies.setter
    def cookies(self, new_cookie):
        pass

    @property
    def timeout(self):
        pass

    @timeout.setter
    def timeout(self, new_timeout):
        pass

    @property
    def term_start_date(self):
        pass

    @property
    def student_id(self):
        pass

    @property
    def default_gpa_query_params(self) -> model.GPAQueryParams:
        pass

    def schedule(self, year, term, timeout=UNSET) -> model.Schedule:
        pass

    def _get_score_detail(self, year, term, class_id, timeout=UNSET) -> typing.List[model.ScoreFactor]:
        pass

    def score(self, year, term, timeout=UNSET) -> model.Scores:
        pass

    def exam(self, year, term, timeout=UNSET) -> model.Exams:
        pass

    def query_courses(self, year, term, name=None, teacher=None, day_of_week=None, week=None, time_of_day=None,
                      timeout=UNSET):
        pass

    def query_gpa(self, query_params: model.GPAQueryParams, timeout=UNSET):
        pass

    def _elect(self, params):
        pass