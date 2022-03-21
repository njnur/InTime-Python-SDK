import json

import requests

from typing import Optional, Dict

from intime_sdk.core import constants
from intime_sdk.core.error_map import in_time_error as _errors


class APIConnector:
    """
    Base class for API connector
    """
    def __init__(self, username: str, secret_key: str):
        if username:
            self.__username = username
        else:
            raise ValueError("Username is missing")

        if secret_key:
            self.__secret_key = secret_key
        else:
            raise ValueError("Secret hash key is missing")

    @staticmethod
    def __get_header() -> dict:
        """
        Method for manipulating API header

        :return: Content type of header
        """
        return {
            'Content-Type': 'text/xml'
        }

    def __get_required_query_params(self) -> dict:
        """
        Method for manipulating API parameter that is required

        :return: Authentication query dict
        """
        return {
            'user': self.__username,
            'hash': self.__secret_key
        }

    def _get(self, api_url: str, params: Optional[Dict] = None) -> dict:
        """
        Base/Main GET method for performing GET requests.

        :param api_url: URI Endpoint
        :param params: (Optional) API request parameters in dictionary format

        :return: API response in dictionary format
        """
        api_response = requests.get(
            url="{base}/{version}/{api_uri}".format(
                base=constants.INTIME_URL,
                version=constants.VERSION,
                api_uri=api_url
            ),
            headers=self.__get_header(),
            params=dict(self.__get_required_query_params().items(), **params)
        )

        if api_response.status_code == 200 and 'ERROR' not in api_response.text:
            return {
                "status": True,
                "data": api_response.json()
            }

        return {
                "status": False,
                "message": 'Error from InTime API. ' + _errors[str(api_response.text)]
                }

    def _post(self, api_url: str, data: Optional[str] = None) -> dict:
        """
        Base/Main POST method for performing POST requests.

        :param api_url: API endpoint
        :param data: (Optional) API request body containing XML in string Format

        :return:
        """
        header = self.__get_header()

        api_response = requests.post(
            url="{base}/{version}/{api_uri}".format(
                base=constants.INTIME_URL,
                version=constants.VERSION,
                api_uri=api_url
            ),
            headers=header,
            params=self.__get_required_query_params(),
            data=data
        )

        if api_response.status_code == 200 and 'ERROR' not in api_response.text:
            if 'Name cannot begin' not in api_response.text:
                return {
                    "status": True,
                    "data": json.dumps(api_response.text)
                }
            return {
                "status": False,
                "data": json.dumps(api_response.text)
            }

        return {
                "status": False,
                "message": 'Error from InTime API. ' + _errors[str(api_response.text)]
                }
