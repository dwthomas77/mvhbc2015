from django.conf.urls import patterns, url
from competition import views

urlpatterns = patterns('',
    url(r'^$', views.compWelcome, name="compWelcome"),
    url(r'^registration/$', views.registration, name="registration"),
    url(r'^register/$', views.register, name="register"),
    url(r'^judge-register/$', views.judge_register, name="judge_register"),
    url(r'^account/$', views.account, name="account"),
    url(r'^judge-account/', views.j_account, name="j_account"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'competition/competition_login.html'}, name="login"),
    url(r'^login/process/$', views.process_login, name="process_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '../login/'}, name="logout"),
    url(r'^results-2014/$', views.results_2014, name='results_2014'),
    url(r'^results-2013/$', views.results_2013, name='results_2013'),
    url(r'^results-2012/$', views.results_2012, name='results_2012'),
    url(r'^sponsors/$', views.sponsors, name='sponsors'),
    # form submission urls
    #
    # UPDATE
    url(r'^account/address/$', views.update_address, name="update_address"),
    url(r'^account/profile/$', views.update_profile, name="update_profile"),
    url(r'^account/judge/$', views.update_judge, name="update_judge"),
    # DELETE
    # ADD
)