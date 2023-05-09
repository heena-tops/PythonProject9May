from django.shortcuts import render,redirect
from .models import User,Category,Product,Wishlist,Cart
from django.conf import settings
from django.core.mail import send_mail
import random
import razorpay

# Create your views here.

def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		carts=Cart.objects.filter(user=user,payment=False)
		request.session['cart_count']=len(carts)
		return render(request,'index.html',{'cat':carts})
	except:
		return render(request,'index.html')

def seller_index(request):
	return render(request,'seller_index.html')

def shop(request):
	return render(request,'shop.html')

def signup(request):
	if request.method=="POST":

		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Exist"
			return render(request,'signup.html',{'msg':msg})

		except:
			if request.POST['pswd'] == request.POST['cpswd']:
				User.objects.create(
				fname=request.POST['fname'],
				lname=request.POST['lname'],
				DOB=request.POST['dob'],
				email=request.POST['email'],
				contact=request.POST['contact'],
				password=request.POST['pswd'],
				address=request.POST['address'],
				usertype=request.POST['usertype'],
				)
				return render(request,'signup.html')

			else:
				msg="Password and Confirm Password Doesn't Matched!!!"
				return render(request,'signup.html',{'msg':msg})
		
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":

		try:
			user=User.objects.get(email=request.POST['email'],password=request.POST['pswd'])
			wishlists=Wishlist.objects.filter(user=user)
			carts=Cart.objects.filter(user=user,payment=False)
			if user.usertype=="seller":
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'seller_index.html')
			else:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['wishlist_count']=len(wishlists)
				request.session['cart_count']=len(carts)
				return render(request,'index.html')

		except:
			msg="Email or Password Does Nor Matched !!!";
			return render(request,'login.html',{'msg':msg})

	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['wishlist_count']
		del request.session['cart_count']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if request.POST['pswd']==user.password:
			if request.POST['new_pswd']==request.POST['cnew_pswd']:
				user.password=request.POST['new_pswd']
				user.save()
				return redirect('login')
			else:
				msg="New Password & Confirm New Password Doesn't Matched!!!"
				return render(request,'change_password.html',{'msg':msg})				

		else:
			msg="Old Password is Wrong !!!"
			return render(request,'change_password.html',{'msg':msg})

	else:
		return render(request,'change_password.html')

def forgot_pswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP'
			message = 'Hello '+user.fname+" Your OTP : "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'email':user.email,'otp':otp})

		except:
			msg="User Not Exist !!"
			return render(request,'forgot_pswd.html',{'msg':msg})
	else:
		return render(request,'forgot_pswd.html')

def otp(request):
	if request.method=="POST":
		email=request.POST['email']
		otp=request.POST['otp']
		uotp=request.POST['uotp']

		if uotp==otp:
			return render(request,'new_pswd.html',{'email':email})		

		else:
			msg="OTP Doesn't Matched !!!"
			return render(request,'otp.html',{'msg':msg})

	else:
		return render(request,'otp.html')

def new_pswd(request):
	if request.method=="POST":
		email=request.POST['email']
		npswd=request.POST['npswd']
		cnpswd=request.POST['cnpswd']

		user=User.objects.get(email=email)
		if npswd==cnpswd:
			user.password=npswd
			user.save()
			return redirect('login')
		else:
			msg="New & Confirm New Password Not Matched !!!"
			return render(request,'new_pswd.html',{'msg':msg})

	else:
		return render(request,'new_pswd.html')

def seller_change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if request.POST['pswd']==user.password:
			if request.POST['new_pswd']==request.POST['cnew_pswd']:
				user.password=request.POST['new_pswd']
				user.save()
				return redirect('login')
			else:
				msg="New Password & Confirm New Password Doesn't Matched!!!"
				return render(request,'seller_change_password.html',{'msg':msg})				

		else:
			msg="Old Password is Wrong !!!"
			return render(request,'seller_change_password.html',{'msg':msg})

	else:
		return render(request,'seller_change_password.html')

def seller_add_product(request):
	seller=User.objects.get(email=request.session['email'])
	category=Category.objects.all()

	if request.method=="POST":
		print(">>>>>>>>>>>>>>>POST REQUEST")
		Product.objects.create(
			seller=seller,
			category=Category.objects.get(name = request.POST['category']), #need to get user choice 
			product_name=request.POST['product_name'],
			product_price=request.POST['product_price'],
			product_qty=request.POST['product_qty'],
			product_desc=request.POST['product_desc'],
			product_image=request.FILES['product_image'],
			)

		msg="Added.........."
		return render(request,'seller_add_product.html',{'cat':category,'msg':msg})

	else:
		return render(request,'seller_add_product.html',{'cat':category})


def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	product=Product.objects.filter(seller=seller)
	return render(request,'seller_view_product.html',{'product':product})

def seller_product_details(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,'seller_product_details.html',{'product':product})

def seller_edit_product(request,pk):
	seller=User.objects.get(email=request.session['email'])
	category=Category.objects.all()
	product=Product.objects.get(pk=pk)

	if request.method=="POST":
		product.product_name=request.POST['product_name']
		product.product_price=request.POST['product_price']
		product.product_qty=request.POST['product_qty']
		product.product_desc=request.POST['product_desc']
		try:
			product.product_image=request.FILES['product_image']
		except:
			pass
		product.save()
		return render(request,'seller_edit_product.html',{'product':product,'cat':category})
	else:
		return render(request,'seller_edit_product.html',{'product':product,'cat':category})

def seller_delete_product(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('seller_view_product')

def view_product(request):
	product=Product.objects.all()
	return render(request,'view_product.html',{'product':product})

def product_details(request,pk):
	wishlist_obj=False
	cart_obj=False
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	try:
		wishlists=Wishlist.objects.get(user=user,product=product)
		wishlist_obj=True

		return render(request,'product_details.html',{'product':product,'wishlist_obj':wishlist_obj})

	except:
		pass

	try:
		carts=Cart.objects.get(user=user,product=product,payment=False)
		cart_obj=True
		return render(request,'product_details.html',{'product':product,'cart_obj':cart_obj})
	except:
		pass

	return render(request,'product_details.html',{'product':product})

def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	return render(request,'wishlist.html',{'wishlists':wishlists})

def add_to_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	Wishlist.objects.create(
		user=user,
		product=product,
		)
	return redirect('wishlist')

def remove_from_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	wishlists=Wishlist.objects.get(user=user,product=product)
	wishlists.delete()
	return redirect('wishlist')

def cart(request):
	net_price=10
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment=False)
	for i in carts:
		net_price+=i.total

	carts.net_price=net_price
	client = razorpay.Client(auth = (settings.KEY_ID,settings.KEY_SECRET))
	payments=client.order.create({'amount':carts.net_price*100, 'currency':'INR','payment_capture':1})
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print(payments)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	carts.razorpay_order_id=payments['id']
	for i in carts:
		i.save()
	return render(request,'cart.html',{'carts':carts,'payments':payments,'net_price':net_price})

def success(request):
	order_id=request.GET.get('order_id')
	carts=Cart.objects.filter(razorpay_order_id=order_id)
	for i in carts:
		i.payment=True
		i.save()
	carts.delete()
	return render(request,'callback.html')

def add_to_cart(request,pk):
	try:
		user=User.objects.get(email=request.session['email'])
		product=Product.objects.get(pk=pk)
		carts=Cart.objects.get(user=user,product=product,payment=False)
		msg="product Already Exist!!!"
		return render(request,'product_details.html',{'msg':msg})
	except:
		user=User.objects.get(email=request.session['email'])
		product=Product.objects.get(pk=pk)
		carts=Cart.objects.create(
			user=user,
			product=product,
			product_qty=1,
			product_price=product.product_price,
			total=product.product_price,
			net_price=0,
			)
		return redirect('cart')

def remove_from_cart(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	carts=Cart.objects.get(user=user,product=product)
	carts.delete()
	return redirect('cart')

def change_qty(request,pk):
	pk=pk
	product_qty=int(request.POST['product_qty'])
	carts=Cart.objects.get(pk=pk)
	carts.total=product_qty*carts.product_price
	carts.product_qty=product_qty
	carts.save()
	return redirect('cart')

def category(request,pk):
	cat=Category.objects.get(pk=pk)
	product=Product.objects.filter(category=cat)

	print(">>>>>>>>>>>>>>>>>>>>>>IN Category : ",cat)
	print(">>>>>>>>>>>>>>>>>>>>>>IN Category : ",product)
	return render(request,'category.html',{'product':product})

def search(request):
	if request.method=="POST":
		if request.POST['name_search'].__contains__('Camera'):
			product=Product.objects.get(product_name=request.POST['name_search'])
			print(">>>>>>>>>>>>>>>>>>>>",product)
			return render(request,'product_details.html',{'product':product})

		else:
			return render(request,'view_product.html')

	else:
		return render(request,'index.html')

# .create() : use to add data into the table 
# 	Syntax : model_name.objects.create()

# .all() : use to fetch all the data from the table (It will return QuerySet)
# Syntax: model_name.objects.all() 

# .get(): use to fetch data from the data table with the condition (It will return Single Object)
# 	Syntax : model_name.objects.get()

#.filter() : use to get QuerySet with condition 
# Syntax : model_name.objects.filter(condition)