from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('services', views.services, name='services'),
  path('contact', views.contact, name='contact'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('deposit', views.deposit, name='deposit'),
  path('selectcoin', views.selectcoin, name='selectcoin'),
  path('depositbnb', views.depositbnb, name='depositbnb'),
  path('depositeth', views.depositeth, name='depositeth'),
  path('depositbtc', views.depositbtc, name='depositbtc'),
  path('depositsol', views.depositsol, name='depositsol'),
  path('depositusdt', views.depositusdt, name='depositusdt'),
  path('btcwithdraw', views.btcwithdraw, name='btcwithdraw'),
  path('forgot', views.forgot, name='forgot'),
  path('signin', views.signin, name='signin'),
  path('signup', views.signup, name='signup'),
  path('withdraw', views.withdraw, name='withdraw'),
  path('logout', views.logout, name='logout'),
]
