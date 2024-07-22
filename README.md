# trellis-python

## Installing the SDK
```
pip install trellis-python

```

## Initiate client
```
from trellis.client import TrellisApi
from trellis import TransformationOperation, TransformParams

client = TrellisApi(
    api_key="YOUR_API_KEY",
)

```
## Quick start workflow, TODO: transform need to wait for extract on server
```
proj_name = "sample_project"
client.assets.upload_assets(
            proj_name=proj_name,folder="sample_folder" # or pass in files = ["file_1", "file_2"] 
)
client.assets_extract.extract_files(proj_name=proj_name)
operations = client.transforms.generate_autoschema(
            proj_name=proj_name,
        ).data
transform_id = client.transforms.create_transform(
            proj_name=proj_name,
            transform_params=TransformParams(
                model="trellis-enterprise",
                operations= operations,
            ),
        ).data.transform_id
results = client.transforms.get_transform_results(
            transform_id=transform_id,
        )
```
