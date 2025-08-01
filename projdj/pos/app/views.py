

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Customer, Order

# Home Page: Show all entries
def home(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(request, 'home.html', {
        'products': products,
        'customers': customers,
        'orders': orders
    })

# Add Product
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        discount = request.POST.get("discount")
        Product.objects.create(name=name, price=price, quantity=quantity, discount=discount)
        return redirect('home')
    return render(request, 'add_product.html')

# Add Customer
def add_customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("address")
        Customer.objects.create(name=name, mobile=mobile, email=email, address=address)
        return redirect('home')
    return render(request, 'add_customer.html')

# Add Order
def add_order(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer")
        product_id = request.POST.get("product")
        Order.objects.create(customer_id=customer_id, product_id=product_id)
        return redirect('home')

    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'add_order.html', {'customers': customers, 'products': products})

