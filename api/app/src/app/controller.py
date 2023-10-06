import uuid

from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from sqlalchemy.sql import text

from src.base_crud import BaseCRUD
from src.init_database import Session
from src.models import Event


class TestController(viewsets.ViewSet):
    serializer_classes = {
        "get_result": None,
    }

    def get_result(self, request):
        return Response(data={"result": "python-test-api"}, status=status.HTTP_200_OK)


class EventController(APIView):
    def __init__(self):
        self.crud = BaseCRUD(Session)

    def post(self, request):
        try:
            user_ip = request.META.get("REMOTE_ADDR")
            data = {
                "id": uuid.uuid4(),
                "user_ip": user_ip
            }
            self.crud.insert(Event, **data)
            self.crud.commit()
            return Response(data={"result": "new user event was created"}, status=status.HTTP_201_CREATED)
        except Exception:
            raise ParseError(detail="Bad request, for any other error. Error reason in logs.")

    def get(self, request):
        try:
            user_ip = request.META.get("REMOTE_ADDR")
            res = 0  # even/odd digit counter
            for digit in user_ip:
                if digit.isdigit():
                    if int(digit) % 2:
                        res += 1
                    else:
                        res -= 1
            if res != 0:
                raise PermissionDenied(detail="Permission denied. User IP is not valid.")
            stmt = text("SELECT * FROM events ORDER BY date_created DESC LIMIT 5")
            db_data = self.crud.get_many_by_statement(stmt)
            api_data = [
                {
                    "id": row["id"],
                    "eventTime": row["date_created"].isoformat(),
                    "userIpAddress": row["user_ip"]
                }
                for row in db_data
            ]
            return Response(data=api_data, status=status.HTTP_200_OK)
        except PermissionDenied as e:
            raise PermissionDenied(detail=e)
        except Exception:
            raise ParseError(detail=f"Bad request, for any other error. Error reason in logs")
