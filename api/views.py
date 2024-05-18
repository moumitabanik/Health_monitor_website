# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import UserHealthData
from .serializers import UserHealthDataSerializer
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage 
from django.conf import settings

@api_view(['POST'])
def health_chatbot_api(request):
    if request.method == 'POST':
        print("Request data:", request.data)  # Print incoming request data
        serializer = UserHealthDataSerializer(data=request.data)
        if serializer.is_valid():
            user_input = serializer.validated_data['symptoms']
            print("User input (symptoms):", user_input)  # Print the validated user input
            
            chat = ChatAnthropic(
                temperature=0, 
                api_key=settings.ANTHROPIC_API_KEY,
                model_name="claude-3-opus-20240229"
            )
            try:
                message = HumanMessage(content=user_input)
                response = chat.invoke([message])
                print("Chat response:", response.content)  # Print the response from the chat API
                
                # Save user input and response to the database
                data_to_save = serializer.validated_data
                data_to_save['recommendations'] = response.content
                UserHealthData.objects.create(**data_to_save)
                
                return Response({'response': response.content})
            except Exception as e:
                print("Error:", str(e))  # Print the error if one occurs
                return Response({'error': str(e)}, status=500)
        print("Serializer errors:", serializer.errors)  # Print serializer errors if validation fails
        return Response(serializer.errors, status=400)
    
class UserHealthDataList(generics.ListAPIView):
    queryset = UserHealthData.objects.all()
    serializer_class = UserHealthDataSerializer