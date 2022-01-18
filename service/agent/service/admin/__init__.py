from service.abstract import Abstract
from service.exception import IncompleteRequiredHeaderException
from service.exception import HeaderValueViolationException
from service.exception import TypeErrorException


class Admin(Abstract):
    def assign_agent(self, data, headers=None):
        url = "/api/v1/admin/service/assign_agent"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def remove_agent(self, data, headers=None):
        url = "/api/v1/admin/service/remove_agent"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def mark_as_resolved(self, data, headers=None):
        url = "/api/v1/admin/service/mark_as_resolved"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def set_sessional_room(self, data, headers=None):
        url = "/api/v1/admin/service/set_sessional"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def allocate_agent(self, data, headers=None):
        url = "/api/v1/admin/service/allocate_agent"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def allocate_and_assign_agent(self, data, headers=None):
        url = "/api/v1/admin/service/allocate_assign_agent"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            ) from e

        url = self.get_client().get_base_url() + url

        return self.get_client().post(url, data)

    def admin_get_other_agents(
        self,
        room_id,
        limit=None,
        cursor_after=None,
        cursor_before=None,
        search=None,
        headers=None,
    ):
        url = "/api/v2/admin/service/other_agents"
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

        if not isinstance(room_id, int):
            raise TypeErrorException("'room_id' must be an integer.")

        query.append("room_id=%d" % (room_id))

        if isinstance(limit, int):
            query.append("limit=%d" % (limit))

        if isinstance(cursor_after, int):
            query.append("cursor_after=%d" % (cursor_after))

        if isinstance(cursor_before, int):
            query.append("cursor_before=%d" % (cursor_before))

        if isinstance(search, str):
            query.append("search=%s" % (search))

        url = url + "?" + "&".join(query)
        url = self.get_client().get_base_url() + url

        return self.get_client().get(url)

    def admin_get_available_agents(
        self,
        room_id,
        limit=None,
        cursor_after=None,
        cursor_before=None,
        is_available_in_room=None,
        headers=None,
    ):
        url = "/api/v2/admin/service/available_agents"
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

        if not isinstance(room_id, int):
            raise TypeErrorException("'room_id' must be an integer.")

        query.append("room_id=%d" % (room_id))

        if isinstance(limit, int):
            query.append("limit=%d" % (limit))

        if isinstance(cursor_after, int):
            query.append("cursor_after=%d" % (cursor_after))

        if isinstance(cursor_before, int):
            query.append("cursor_before=%d" % (cursor_before))

        if isinstance(is_available_in_room, bool):
            query.append(
                "is_available_in_room=%s"
                % ("true" if is_available_in_room == True else "false")
            )

        url = url + "?" + "&".join(query)
        url = self.get_client().get_base_url() + url

        return self.get_client().get(url)

    def get_total_unserved(self, headers=None):
        url = "/api/v2/admin/service/total_unserved"

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

    def get_sessional_status(self, headers=None):
        url = "/api/v1/admin/service/get_sessional"

        if isinstance(headers, dict):
            self.get_client().set_headers(headers)

        headers = self.get_client().get_headers()

        try:
            headers["Content-Type"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Content-Type' from headers list."
            ) from e

        try:
            headers["Qiscus-App-Id"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-App-Id' from headers list."
            ) from e

        try:
            headers["Qiscus-Secret-Key"]
        except KeyError as e:
            raise IncompleteRequiredHeaderException(
                "Missing header name 'Qiscus-Secret-Key' from headers list."
            )

        url = self.get_client().get_base_url() + url

        return self.get_client().get(url)
