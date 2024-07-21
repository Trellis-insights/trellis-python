# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.not_found_error import NotFoundError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.delete_project_response import DeleteProjectResponse
from ...types.get_projects_response import GetProjectsResponse
from ...types.http_validation_error import HttpValidationError
from ...types.order_by_enum import OrderByEnum
from ...types.sort_order_enum import SortOrderEnum
from ...types.transfer_project_response import TransferProjectResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_projects(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[OrderByEnum] = None,
        order: typing.Optional[SortOrderEnum] = None,
    ) -> GetProjectsResponse:
        """
        Retrieve a list of projects.

        Parameters:

        - proj_names (list[str], optional): A list of project names. If not provided, all projects will be retrieved.

        Returns:

        - dict: A dict containing the status mesage and the list of project names.

        Parameters:
            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - order_by: typing.Optional[OrderByEnum].

            - order: typing.Optional[SortOrderEnum].
        ---
        from trellis.client import TrellisApi

        client = TrellisApi(
            api_key="YOUR_API_KEY",
        )
        client.project.get_projects()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=remove_none_from_dict({"limit": limit, "offset": offset, "order_by": order_by, "order": order}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetProjectsResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_project(self, proj_name: str) -> DeleteProjectResponse:
        """
        Delete a project.

        Parameters:

        - proj_name (str): The name of the project.

        Parameters:
            - proj_name: str.
        ---
        from trellis.client import TrellisApi

        client = TrellisApi(
            api_key="YOUR_API_KEY",
        )
        client.project.delete_project(
            proj_name="proj_name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{proj_name}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteProjectResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def transfer_project(
        self, proj_name: str, *, to_email: str, copy: typing.Optional[bool] = None
    ) -> TransferProjectResponse:
        """
        Transfer a project to a new owner.

        Parameters:

        - proj_name (str): The name of the project.
        - new_owner (str): The email of the new owner.

        Returns:

        - dict: A dictionary containing the status message and the project name.

        Parameters:
            - proj_name: str.

            - to_email: str.

            - copy: typing.Optional[bool].
        ---
        from trellis.client import TrellisApi

        client = TrellisApi(
            api_key="YOUR_API_KEY",
        )
        client.project.transfer_project(
            proj_name="proj_name",
            to_email="to_email",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{proj_name}/transfer"),
            params=remove_none_from_dict({"to_email": to_email, "copy": copy}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransferProjectResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_projects(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[OrderByEnum] = None,
        order: typing.Optional[SortOrderEnum] = None,
    ) -> GetProjectsResponse:
        """
        Retrieve a list of projects.

        Parameters:

        - proj_names (list[str], optional): A list of project names. If not provided, all projects will be retrieved.

        Returns:

        - dict: A dict containing the status mesage and the list of project names.

        Parameters:
            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - order_by: typing.Optional[OrderByEnum].

            - order: typing.Optional[SortOrderEnum].
        ---
        from trellis.client import AsyncTrellisApi

        client = AsyncTrellisApi(
            api_key="YOUR_API_KEY",
        )
        await client.project.get_projects()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=remove_none_from_dict({"limit": limit, "offset": offset, "order_by": order_by, "order": order}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetProjectsResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_project(self, proj_name: str) -> DeleteProjectResponse:
        """
        Delete a project.

        Parameters:

        - proj_name (str): The name of the project.

        Parameters:
            - proj_name: str.
        ---
        from trellis.client import AsyncTrellisApi

        client = AsyncTrellisApi(
            api_key="YOUR_API_KEY",
        )
        await client.project.delete_project(
            proj_name="proj_name",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{proj_name}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteProjectResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def transfer_project(
        self, proj_name: str, *, to_email: str, copy: typing.Optional[bool] = None
    ) -> TransferProjectResponse:
        """
        Transfer a project to a new owner.

        Parameters:

        - proj_name (str): The name of the project.
        - new_owner (str): The email of the new owner.

        Returns:

        - dict: A dictionary containing the status message and the project name.

        Parameters:
            - proj_name: str.

            - to_email: str.

            - copy: typing.Optional[bool].
        ---
        from trellis.client import AsyncTrellisApi

        client = AsyncTrellisApi(
            api_key="YOUR_API_KEY",
        )
        await client.project.transfer_project(
            proj_name="proj_name",
            to_email="to_email",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{proj_name}/transfer"),
            params=remove_none_from_dict({"to_email": to_email, "copy": copy}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransferProjectResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)