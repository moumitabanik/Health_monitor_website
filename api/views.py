# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserHealthData
from .serializers import UserHealthDataSerializer
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage 

@api_view(['POST'])
def health_chatbot_api(request):
    if request.method == 'POST':
        serializer = UserHealthDataSerializer(data=request.data)
        if serializer.is_valid():
            user_input = serializer.validated_data['symptoms']
            chat = ChatAnthropic(temperature=0, api_key="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", model_name="claude-3-opus-20240229")
            try:
                message = HumanMessage(content=user_input)
                response = chat.invoke([message])
                # Save user input and response to the database
                data_to_save = serializer.validated_data
                data_to_save['response'] = response[0].content
                UserHealthData.objects.create(**data_to_save)
                return Response({'response': response[0].content})
            except Exception as e:
                return Response({'error': str(e)}, status=500)
        return Response(serializer.errors, status=400)
