# BotSellerUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**llm_model** | **str** |  | [optional] 
**llm_prompt** | **str** |  | [optional] 

## Example

```python
from infonomy_client.models.bot_seller_update import BotSellerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BotSellerUpdate from a JSON string
bot_seller_update_instance = BotSellerUpdate.from_json(json)
# print the JSON string representation of the object
print(BotSellerUpdate.to_json())

# convert the object into a dict
bot_seller_update_dict = bot_seller_update_instance.to_dict()
# create an instance of BotSellerUpdate from a dict
bot_seller_update_from_dict = BotSellerUpdate.from_dict(bot_seller_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


