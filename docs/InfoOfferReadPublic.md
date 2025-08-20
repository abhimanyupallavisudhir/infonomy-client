# InfoOfferReadPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**seller_id** | **int** |  | 
**public_info** | **str** |  | 
**price** | **float** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from infonomy_client.models.info_offer_read_public import InfoOfferReadPublic

# TODO update the JSON string below
json = "{}"
# create an instance of InfoOfferReadPublic from a JSON string
info_offer_read_public_instance = InfoOfferReadPublic.from_json(json)
# print the JSON string representation of the object
print(InfoOfferReadPublic.to_json())

# convert the object into a dict
info_offer_read_public_dict = info_offer_read_public_instance.to_dict()
# create an instance of InfoOfferReadPublic from a dict
info_offer_read_public_from_dict = InfoOfferReadPublic.from_dict(info_offer_read_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


