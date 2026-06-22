from django.http import HttpResponse


class under_maintaince:
    def __init__(self,get_response):
        self.get_response=get_response

    
    def __call__(self,request):
        
        if request.path.endswith('/loans/'):
            return HttpResponse('Loan Services Apply for personal and business loans easily Visit are under maintaince')
        
        response=self.get_response(request)
        return response