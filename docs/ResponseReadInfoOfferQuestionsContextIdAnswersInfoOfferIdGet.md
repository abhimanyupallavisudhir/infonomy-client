# ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet


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
from infonomy_client.models.response_read_info_offer_questions_context_id_answers_info_offer_id_get import ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet from a JSON string
response_read_info_offer_questions_context_id_answers_info_offer_id_get_instance = ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet.from_json(json)
# print the JSON string representation of the object
print(ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet.to_json())

# convert the object into a dict
response_read_info_offer_questions_context_id_answers_info_offer_id_get_dict = response_read_info_offer_questions_context_id_answers_info_offer_id_get_instance.to_dict()
# create an instance of ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet from a dict
response_read_info_offer_questions_context_id_answers_info_offer_id_get_from_dict = ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet.from_dict(response_read_info_offer_questions_context_id_answers_info_offer_id_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


