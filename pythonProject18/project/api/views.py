from .models import Products, Cart, Order, User
from .serializers import OrderSer, ProductSer, CartSer, LoginSer, Regserializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration(request):
    ser = Regserializer(data=request.data)
    if ser.is_valid():
        user = ser.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user_token': token.key}, status=201)
    return Response({'error': {"code": 422, "message": "Validation error", 'errors:': ser.errors}}, status=422)

@api_view(["POST"])
def login(request):
    ser = LoginSer(data=request.data)
    if ser.is_valid():
        user = User.objects.get(email=ser.validated_data['email'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user_token': token.key}, status=201)
    return Response({'error': {"code": 422, "message": "Validation error", 'errors:': ser.errors}}, status=422)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response('logout from your cabinet')

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def productsView(request):
    if request.method == "GET":
        products = Products.objects.all()
        ser = ProductSer(products, many=True)
        return Response({'data': ser.data})
    elif request.method == 'POST':
        ser = ProductSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'data': ser.data}, status=201)
        return Response({'error': {"code": 422, "message": "Validation error", 'errors:': ser.errors}}, status=422)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def productsView(request, pk):
    try:
        product = Products.objects.all(pk=pk)
    except:
        return Response('Not found')
    if request.method == "GET":
        ser = ProductSer(product,)
        return Response({'data': ser.data})
    elif request.method == 'PUT':
        ser = ProductSer(data=request.data, instance=product)
        if ser.is_valid():
            ser.save()
            return Response({'data': ser.data}, status=201)
        return Response({'error': {"code": 422, "message": "Validation error", 'errors:': ser.errors}}, status=422)
    elif request.method == 'PATCH':
        ser = ProductSer(data=request.data, instance=product, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data': ser.data}, status=201)
        return Response({'error': {"code": 422, "message": "Validation error", 'errors:': ser.errors}}, status=422)
    elif request.method == "DELETE":
        product.delete()
        return Response ('Product deleted')

@api_view(['GET'])
def cartInfo(request):
    cart = Cart.objects.filter(user=request.user)
    ser = CartSer(cart, many=True)
    return  Response({'data': ser.data})

@api_view(["POST", "DELETE"])
def cartChange(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except:
        return Response('Not found')
    if request.method == "POST":
        cart = Cart.objects.create(user=request.user)
        cart.product.add(product)
        return Response('Product add to cart')
    elif request.method == "DELETE":
        cart = Cart.objects.get(user=request.user)
        cart.product.remove(product)
        return Response('Products deleted')