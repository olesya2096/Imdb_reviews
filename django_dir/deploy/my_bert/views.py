from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .apps import WebappConfig

# class call_model(APIView):

def predictor(request):
    if request.method == 'POST':
        text = request.POST['text']
        response = WebappConfig.model.predict(text)
        rate = 'positive'
        if response == 0:
            res = '1'
            rate = 'negative'
        elif response == 1:
            res = '2'
            rate = 'negative'
        elif response == 2:
            res = '3'
            rate = 'negative'
        elif response == 3:
            res = '4'
            rate = 'negative'
        elif response == 4:
            res = '7'
        elif response == 5:
            res = '8'
        elif response == 6:
            res = '9'
        elif response == 7:
            res = '10'
        result = rate + '-' + res
        return render(request, '/Users/o.moiseenko/Desktop/django/deploy/templates/main.html', {'result' : result})
    return render(request, '/Users/o.moiseenko/Desktop/django/deploy/templates/main.html')

# test_input_ids = []
# test_attention_masks = []
# for text in test_data[0]:
#     encoded_dict = tokenizer.encode_plus(
#                         text,
#                         add_special_tokens = True,
#                         max_length = 512,
#                         pad_to_max_length = True,
#                         return_attention_mask = True,
#                         return_tensors = 'pt',
#                    )
#     test_input_ids.append(encoded_dict['input_ids'])
#     test_attention_masks.append(encoded_dict['attention_mask'])
# test_input_ids = torch.cat(test_input_ids, dim=0)
# test_attention_masks = torch.cat(test_attention_masks, dim=0)
# test_labels = torch.tensor(test_data[1])
#
# print('Original: ', test_data[0][0])
# print('Token IDs:', test_input_ids[0])

