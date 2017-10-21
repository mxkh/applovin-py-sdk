from typing import Dict, List
import requests


class Request:
    URL = 'https://r.applovin.com/report'

    FORMAT_JSON = 'json'

    REPORT_PUBLISHER = 'publisher'
    REPORT_ADVERTISER = 'advertiser'

    def __init__(self, api_key: str, start: str, end: str) -> None:
        self.api_key: str = api_key
        self.start: str = start
        self.end: str = end
        self.columns: List[str] = []
        self.format: str = self.FORMAT_JSON
        self.report_type: str = self.REPORT_PUBLISHER

    def make(self) -> requests.Response:
        return requests.get(self.URL, params=self.__payload())

    def columns_to_string(self) -> str:
        return ','.join(map(str, self.columns))

    def payload(self) -> Dict[str, str]:
        return {
            'api_key': self.api_key,
            'start': self.start,
            'end': self.end,
            'format': self.format,
            'report_type': self.report_type,
            'columns': self.__columns_to_string()
        }
