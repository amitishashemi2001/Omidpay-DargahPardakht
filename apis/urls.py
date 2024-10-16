import apis.views
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="OmidPay API",
        default_version='v1',
        description="API documentation for OmidPay integration.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@omidpay.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('get-token/', apis.views .OmidPayTokenView.as_view(), name='get_token'),
    path('success/', apis.views. OmidPayCallbackView.as_view(), name='payment_success_callback'),
    path('verify-transaction/',  apis.views .VerifyTransactionView.as_view(), name='verify_transaction'),
]
