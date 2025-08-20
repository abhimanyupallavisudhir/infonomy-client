# InfoOfferCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_info** | **str** |  | 
**public_info** | **str** |  | [optional] 
**price** | **float** |  | [optional] [default to 0.0]

## Example

```python
from infonomy_client.models.info_offer_create import InfoOfferCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InfoOfferCreate from a JSON string
info_offer_create_instance = InfoOfferCreate.from_json(json)
# print the JSON string representation of the object
print(InfoOfferCreate.to_json())

# convert the object into a dict
info_offer_create_dict = info_offer_create_instance.to_dict()
# create an instance of InfoOfferCreate from a dict
info_offer_create_from_dict = InfoOfferCreate.from_dict(info_offer_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


