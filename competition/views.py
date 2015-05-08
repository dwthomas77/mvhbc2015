from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from competition.forms import UserForm, JudgeUserForm, ProfileForm, AddressForm, ProfileJudgeForm, SubmissionForm
from competition.models import UserProfile, Address, Submission

def process_login(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        return redirect('account')

def compWelcome(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],      
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        if userForm.is_valid():
            addressForm = AddressForm()
            userProfileForm = ProfileForm()
            u = userForm.save()
            up = UserProfile(user=u)
            up.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    return render(request, "competition/registration.html", {'userForm': userForm})
            else:
                return render(request, "competition/registration-error.html", {'userForm': userForm})
        else:
            return render(request, 'competition/comp-welcome.html', {
                'userForm' : userForm
            })
    else:
        userForm = UserForm()
        return render(request, "competition/comp-welcome.html", {'userForm': userForm})

def registration(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],      
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        # set and validate user form data
        myUserForm = UserForm(userData)
        if myUserForm.is_valid():
            return render(request, "competition/registration.html", {})
        else:
            return render(request, "competition/registration-error.html", {})
    else:
        return render(request, "competition/registration-error.html", {})

# User Registration
def register(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],      
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        addressData = {
            'street_1' : request.POST['street_1'], 
            'street_2' : request.POST['street_2'], 
            'city' : request.POST['city'],
            'state' : request.POST['state'],
            'zipcode' : request.POST['zipcode']
        }
        profileData = {
            'club' : request.POST['club'],
            'aha_id' : request.POST['aha_id']
        }
        profileJudgeData = {
            'judge_preference' : request.POST['judge_preference'], 
            'qualification' : request.POST['qualification'],
            'bjcp_registration' : request.POST['bjcp_registration'],
            'judge_comments' : request.POST['judge_comments']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        addressForm = AddressForm(addressData)
        profileForm = ProfileForm(profileData)
        pJudgeForm = ProfileJudgeForm(profileJudgeData)
        if userForm.is_valid():
            u = userForm.save()
            a = addressForm.save()
            profile = UserProfile(
                user=u,
                address=a,
                judge_preference = request.POST['judge_preference'], 
                qualification = request.POST['qualification'], 
                bjcp_registration = request.POST['bjcp_registration'],
                judge_comments = request.POST['judge_comments'],
                club = request.POST['club'],
                aha_id = request.POST['aha_id']
            )
            profile.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    return render(request, "competition/registration.html", {'userForm': userForm, 'judgeForm': profileForm})
            else:
                return redirect('register')
        else:
            return render(request, 'competition/registration.html', {
                'userForm' : userForm,
                'addressForm' : addressForm,
                'profileForm' : profileForm,
                'pJudgeForm' : pJudgeForm
            })
    else:
        myUserForm = UserForm()
        addressForm = AddressForm()
        profileForm = ProfileForm()
        pJudgeForm = ProfileJudgeForm()
        return render(request, "competition/registration.html", {
            'userForm' : myUserForm,
            'addressForm' : addressForm,
            'profileForm' : profileForm,
            'pJudgeForm' : pJudgeForm
        })

# Judge Registration
def judge_register(request):
    if request.method == 'POST':
        userData = {
            'username':  request.POST['username'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],      
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        profileData = {
            'judge_preference' : request.POST['judge_preference'], 
            'qualification' : request.POST['qualification'], 
            'bjcp_registration' : request.POST['bjcp_registration'],
            'judge_comments' : request.POST['judge_comments'],
            'phone_number' : request.POST['phone_number'],
            'club' : request.POST['club'],
            'aha_id' : request.POST['aha_id']
        }
        # set and validate user form data
        userForm = UserForm(userData)
        profileForm = JudgeUserForm(profileData)
        if userForm.is_valid():
            u = userForm.save()
            profile = UserProfile(
                user=u,
                judge_preference = request.POST['judge_preference'], 
                qualification = request.POST['qualification'], 
                bjcp_registration = request.POST['bjcp_registration'],
                judge_comments = request.POST['judge_comments'],
                phone_number = request.POST['phone_number'],
                club = request.POST['club'],
                aha_id = request.POST['aha_id']
            )
            profile.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('j_account')
                else:
                    return render(request, "competition/judge-registration.html", {'userForm': userForm, 'judgeForm': profileForm})
            else:
                return redirect('judge_register')
        else:
            return render(request, 'competition/judge-registration.html', {
                'userForm' : userForm,
                'judgeForm' : profileForm
            })
    else:
        myUserForm = UserForm()
        judgeForm = JudgeUserForm()
        return render(request, "competition/judge-registration.html", {
            'userForm' : myUserForm,
            'judgeForm' : judgeForm
        })

# Account Page
def account(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        profile = request.user.userprofile
        # build forms
        userForm = UserForm(instance=request.user)
        addressForm = AddressForm(instance=profile.address)
        submissionForm = SubmissionForm()
        judgeForm = ProfileJudgeForm({
             'judge_preference' : profile.judge_preference,
             'qualification' : profile.qualification,
             'judge_comments' : profile.judge_comments,
             'bjcp_registration' : profile.bjcp_registration,

        })
        # query user submissions
        submission_query = Submission.objects.filter(brewer = profile)
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'submissionForm': submissionForm,
            'entries': submission_query
        })

# Account Page
def j_account(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        if request.method == 'POST':
            # retrieve user profile
            profile = request.user.userprofile
            # set fields
            profile.judge_preference = request.POST['judge_preference']
            profile.qualification = request.POST['qualification']
            profile.judge_comments = request.POST['judge_comments']
            profile.bjcp_registration = request.POST['bjcp_registration']
            profile.phone_number = request.POST['phone_number']
            profile.club = request.POST['club']
            profile.aha_id = request.POST['aha_id']
            # save changes
            profile.save();
            # return updated model form
            judgeForm = JudgeUserForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration,
                'phone_number' : profile.phone_number,
                'club' : profile.club,
                'aha_id' : profile.aha_id
            })
            return render(request, "competition/j_account.html", {
                'judgeForm': judgeForm
            })
        else:
            userForm = UserForm(request.user)
            profile = request.user.userprofile
            judgeForm = JudgeUserForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration,
                'phone_number' : profile.phone_number,
                'club' : profile.club,
                'aha_id' : profile.aha_id
            })
            return render(request, "competition/j_account.html", {
                'judgeForm': judgeForm
            })

## UPDATES

def update_address(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        msg = "nothing happened"
        # build address form
        addressData = {
            'street_1': request.POST['street_1'],
            'street_2': request.POST['street_2'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'zipcode': request.POST['zipcode']
        }
        addressForm = AddressForm(addressData)
        if addressForm.is_valid():
            # save address
            a = profile.address
            a.street_1 = request.POST['street_1']
            a.street_2 = request.POST['street_2']
            a.city = request.POST['city']
            a.state = request.POST['state']
            a.zipcode = request.POST['zipcode']
            a.save()
            msg = "Address Successfully Updated"
        # build other forms
        userForm = UserForm(instance=request.user)
        judgeForm = ProfileJudgeForm({
            'judge_preference' : profile.judge_preference,
            'qualification' : profile.qualification,
            'judge_comments' : profile.judge_comments,
            'bjcp_registration' : profile.bjcp_registration
        })
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'infoMsg'   : msg
        })
    else:
        return redirect('account')

def update_profile(request):
    return redirect('account')

def update_judge(request):
    if not request.user.is_authenticated():
        return redirect('login')
    elif request.method == 'POST' and request.user.userprofile:
        profile = request.user.userprofile
        msg = "Judge Preferences have been updated"
        # set fields
        profile.judge_preference = request.POST['judge_preference']
        profile.qualification = request.POST['qualification']
        profile.judge_comments = request.POST['judge_comments']
        profile.bjcp_registration = request.POST['bjcp_registration']
        # save changes
        profile.save();
        # build other forms
        userForm = UserForm(instance=request.user)
        addressForm = AddressForm(instance=profile.address)
        judgeForm = ProfileJudgeForm({
            'judge_preference' : profile.judge_preference,
            'qualification' : profile.qualification,
            'judge_comments' : profile.judge_comments,
            'bjcp_registration' : profile.bjcp_registration
        })
        return render(request, "competition/account.html", {
            'userForm': userForm,
            'addressForm': addressForm,
            'judgeForm': judgeForm,
            'infoMsg'   : msg
        })
    else:
        return redirect('account')

## Add
def add_submission(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        if request.method == 'POST' and request.user.userprofile:
            profile = request.user.userprofile
            submission_data = {
                'style': request.POST['style'],
                'name': request.POST['name'],
                'comments': request.POST['comments']
            }
            submissionForm = SubmissionForm(submission_data)
            if submissionForm.is_valid():
                s = submissionForm.save(commit=False)
                s.brewer = profile
                s.save()
                styleId = str(s.style.style_id)
                submissionId = str(s.pk)
                s.competition_id = styleId + submissionId
                s.save()
                submissionForm = SubmissionForm()
                msg = "Submission successfully saved"
            else:
                msg = "There was a problem with your submission entry"
            #build forms
            userForm = UserForm(instance=request.user)
            addressForm = AddressForm(instance=profile.address)
            judgeForm = ProfileJudgeForm({
                'judge_preference' : profile.judge_preference,
                'qualification' : profile.qualification,
                'judge_comments' : profile.judge_comments,
                'bjcp_registration' : profile.bjcp_registration
            })
            # query user submissions
            submission_query = Submission.objects.filter(brewer = profile)
            return render(request, "competition/account.html", {
                'userForm': userForm,
                'addressForm': addressForm,
                'judgeForm': judgeForm,
                'submissionForm': submissionForm,
                'entries': submission_query,
                'infoMsg'   : msg
            })
        else:
            return redirect('login')

## Delete
def delete_submission(request, s_pk):
    if not request.user.is_authenticated():
        return redirect('register')
    else:
        # identify submission object and current user
        submission = get_object_or_404(Submission, pk=s_pk)
        profile = UserProfile.objects.get(pk=submission.brewer.pk)

        ## redirect if user is not owner of this submission or submission is not valid
        if (submission) and (request.user.userprofile != profile):
            return redirect('account')
        else:
            if request.method == 'POST':
                # delete submission
                submission.delete()
                #build forms
                userForm = UserForm(instance=request.user)
                addressForm = AddressForm(instance=profile.address)
                submissionForm = SubmissionForm()
                judgeForm = ProfileJudgeForm({
                    'judge_preference' : profile.judge_preference,
                    'qualification' : profile.qualification,
                    'judge_comments' : profile.judge_comments,
                    'bjcp_registration' : profile.bjcp_registration
                })
                # query user submissions
                submission_query = Submission.objects.filter(brewer = profile)
                return render(request, "competition/account.html", {
                    'userForm': userForm,
                    'addressForm': addressForm,
                    'judgeForm': judgeForm,
                    'submissionForm': submissionForm,
                    'entries': submission_query,
                    'infoMsg'   : "Submission successfully deleted."
            })
            else:
                redirect('account')

def results_2014(request):
    return render(request, "competition/results_2014.html")

def results_2013(request):
    return render(request, "competition/results_2013.html")

def results_2012(request):
    return render(request, "competition/results_2012.html")

def sponsors(request):
    return render(request, "competition/sponsors.html")










