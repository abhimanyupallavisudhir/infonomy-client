# ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner


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
from infonomy_client.models.read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner import ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner from a JSON string
read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner_instance = ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner.to_json())

# convert the object into a dict
read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner_dict = read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner_instance.to_dict()
# create an instance of ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner from a dict
read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner_from_dict = ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner.from_dict(read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


