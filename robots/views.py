from django.http import JsonResponse
from django.views import View
from pydantic import ValidationError
from .models import Robot
from .validators import RobotJSON


class RobotCreateView(View):
    http_method_names = ['post']

    def post(self, request):
        try:
            robot = RobotJSON.model_validate_json(request.body)
        except ValidationError as e:
            return JsonResponse({'error': f'{e}'}, status=400)
        else:
            Robot.objects.create(serial=f'{robot.model}-{robot.version}', model=robot.model,
                                 version=robot.version, created=robot.created)
            return JsonResponse({'Робот создан': dict(robot)})

