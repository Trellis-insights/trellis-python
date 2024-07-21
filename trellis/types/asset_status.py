# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AssetStatus(str, enum.Enum):
    """
    An enumeration.
    """

    UPLOADED = "uploaded"
    FAILED_UPLOAD = "failed_upload"
    PROCESSING = "processing"
    NOT_PROCESSED = "not_processed"
    PROCESSED = "processed"

    def visit(
        self,
        uploaded: typing.Callable[[], T_Result],
        failed_upload: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        not_processed: typing.Callable[[], T_Result],
        processed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetStatus.UPLOADED:
            return uploaded()
        if self is AssetStatus.FAILED_UPLOAD:
            return failed_upload()
        if self is AssetStatus.PROCESSING:
            return processing()
        if self is AssetStatus.NOT_PROCESSED:
            return not_processed()
        if self is AssetStatus.PROCESSED:
            return processed()