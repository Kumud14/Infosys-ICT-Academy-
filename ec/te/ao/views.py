from django.shortcuts import render, redirect
from .models import User, Product, Order

# ---------- AUTH ----------
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_admin = request.POST.get('is_admin') == 'on'  # Checkbox optional

        User.objects.create(
            username=username,
            email=email,
            password=password,
            is_admin=is_admin  # ✅ No error now
        )
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).first()

        if user:
            request.session['user_id'] = user.id
            request.session['is_admin'] = user.is_admin
            return redirect('admin_dashboard' if user.is_admin else 'home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

# ---------- USER SIDE ----------
def home(request):
    if not request.session.get('user_id'):
        return redirect('login')
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    if not request.session.get('user_id'):
        return redirect('login')
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order(request, product_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)

    if product.stock > 0:
        Order.objects.create(user=user, product=product, quantity=1)
        product.stock -= 1
        product.save()
        return redirect('orders')
    else:
        return render(request, 'home.html', {
            'products': Product.objects.all(),
            'error': f'Sorry, {product.name} is out of stock!'
        })

def orders(request):
    if not request.session.get('user_id'):
        return redirect('login')
    user = User.objects.get(id=request.session['user_id'])
    user_orders = Order.objects.filter(user=user).order_by('-order_date')
    return render(request, 'orders.html', {'orders': user_orders})

# ---------- ADMIN SIDE ----------
def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('home')
    return render(request, 'admin_dashboard.html')

def add_product(request):
    if not request.session.get('is_admin'):
        return redirect('home')

    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            description=request.POST['description']
        )
        return redirect('admin_dashboard')
    return render(request, 'add_product.html')

def all_orders(request):
    if not request.session.get('is_admin'):
        return redirect('home')

    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'all_orders.html', {'orders': orders})

def all_users(request):
    if not request.session.get('is_admin'):
        return redirect('home')

    users = User.objects.filter(is_admin=False)
    return render(request, 'all_users.html', {'users': users})


from .models import Message  # Add to imports

def chat(request, user_id):
    if not request.session.get('user_id'):
        return redirect('login')

    current_user = User.objects.get(id=request.session['user_id'])
    other_user = User.objects.get(id=user_id)

    # Fetch messages between the two users
    messages = Message.objects.filter(
        sender__in=[current_user, other_user],
        receiver__in=[current_user, other_user]
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(sender=current_user, receiver=other_user, content=content)
        return redirect('chat', user_id=other_user.id)

    return render(request, 'chat.html', {
        'messages': messages,
        'other_user': other_user
    })
