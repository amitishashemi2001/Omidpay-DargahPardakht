from rest_framework.response import Response
from rest_framework import status


class ValidateOmidPayMixin:
    def validate_omidpay_data(data, required_fields):
        for field in required_fields:
            if not data.get(field):
                return Response(
                    {'status': 'error', 'message': f'{field} is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return None
