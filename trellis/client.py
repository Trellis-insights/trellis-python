# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import TrellisApiEnvironment
from .resources.assets.client import AssetsClient, AsyncAssetsClient
from .resources.assets_extract.client import AssetsExtractClient, AsyncAssetsExtractClient
from .resources.project.client import AsyncProjectClient, ProjectClient
from .resources.transforms.client import AsyncTransformsClient, TransformsClient
from .resources.validation.client import AsyncValidationClient, ValidationClient
from .resources.validation_params.client import AsyncValidationParamsClient, ValidationParamsClient


class TrellisApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: TrellisApiEnvironment = TrellisApiEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.project = ProjectClient(client_wrapper=self._client_wrapper)
        self.assets = AssetsClient(client_wrapper=self._client_wrapper)
        self.assets_extract = AssetsExtractClient(client_wrapper=self._client_wrapper)
        self.transforms = TransformsClient(client_wrapper=self._client_wrapper)
        self.validation = ValidationClient(client_wrapper=self._client_wrapper)
        self.validation_params = ValidationParamsClient(client_wrapper=self._client_wrapper)


class AsyncTrellisApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: TrellisApiEnvironment = TrellisApiEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.project = AsyncProjectClient(client_wrapper=self._client_wrapper)
        self.assets = AsyncAssetsClient(client_wrapper=self._client_wrapper)
        self.assets_extract = AsyncAssetsExtractClient(client_wrapper=self._client_wrapper)
        self.transforms = AsyncTransformsClient(client_wrapper=self._client_wrapper)
        self.validation = AsyncValidationClient(client_wrapper=self._client_wrapper)
        self.validation_params = AsyncValidationParamsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: TrellisApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
