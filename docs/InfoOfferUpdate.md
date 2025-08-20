# InfoOfferUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_info** | **str** |  | [optional] 
**public_info** | **str** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from infonomy_client.models.info_offer_update import InfoOfferUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InfoOfferUpdate from a JSON string
info_offer_update_instance = InfoOfferUpdate.from_json(json)
# print the JSON string representation of the object
print(InfoOfferUpdate.to_json())

# convert the object into a dict
info_offer_update_dict = info_offer_update_instance.to_dict()
# create an instance of InfoOfferUpdate from a dict
info_offer_update_from_dict = InfoOfferUpdate.from_dict(info_offer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


