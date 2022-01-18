from service.abstract import Abstract
from service.exception import IncompleteRequiredHeaderException
from service.exception import HeaderValueViolationException
from service.exception import TypeErrorException


class Division(Abstract):
    def get_all_division(self, page=None, limit=None, headers=None):
        url = "/api/v2/divisions"
        query = []

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        if isinstance(page, int):
            query.append("page=%d" % (page))

        if isinstance(limit, int):
            query.append("limit=%d" % (limit))

        url = url + "?" + "&".join(query)
        url = self.get_client().get_base_url() + url

        return self.get_client().get(url)

    def create_division(self, data, headers=None):
        url = "/api/v2/divisions"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def show_division(self, division_id, headers=None):
        url = "/api/v2/divisions/%d" % (division_id)

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().get(url)

    def set_division_as_default(self, division_id, headers=None):
        url = "/api/v2/divisions/%d/set_default" % (division_id)

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header 'Qiscus-App-Id' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url)

    def update_division(self, division_id, data, headers=None):
        url = "/api/v2/divisions/%d/update" % (division_id)

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header 'Qiscus-App-Id' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def delete_division(self, division_id, headers=None):
        url = "/api/v2/divisions/%d/delete" % (division_id)

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Authorization"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header 'Authorization' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header 'Qiscus-App-Id' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url)
