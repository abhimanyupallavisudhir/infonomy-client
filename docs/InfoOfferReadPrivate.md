# InfoOfferReadPrivate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**human_seller_id** | **int** |  | 
**bot_seller_id** | **int** |  | 
**seller_type** | **str** |  | 
**context_id** | **int** |  | 
**public_info** | **str** |  | 
**price** | **float** |  | 
**created_at** | **datetime** |  | 
**private_info** | **str** |  | 

## Example

```python
from infonomy_client.models.info_offer_read_private import InfoOfferReadPrivate

# TODO update the JSON string below
json = "{}"
# create an instance of InfoOfferReadPrivate from a JSON string
info_offer_read_private_instance = InfoOfferReadPrivate.from_json(json)
# print the JSON string representation of the object
print(InfoOfferReadPrivate.to_json())

# convert the object into a dict
info_offer_read_private_dict = info_offer_read_private_instance.to_dict()
# create an instance of InfoOfferReadPrivate from a dict
info_offer_read_private_from_dict = InfoOfferReadPrivate.from_dict(info_offer_read_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


