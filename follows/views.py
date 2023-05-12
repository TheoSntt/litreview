from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from follows.forms import FollowUserForm
from django.contrib.auth import get_user_model


@login_required
def follow_users(request):
    User = get_user_model()

    if request.method == 'POST':
        form = FollowUserForm(request.user, request.POST)
        if form.is_valid():

            following = form.save(commit=False)
            following.user = request.user
            following.save()
            return redirect('follow-users')
    else:
        form = FollowUserForm(request.user)

    followed_users = request.user.follows.all()
    users_to_follow = User.objects.exclude(id=request.user.id).exclude(id__in=followed_users)
    context = {
        'form': form,
        'users_to_follow': users_to_follow,
        'followed_users': followed_users,
        'followers': request.user.followers.all()
    }
    return render(request, 'follows/follow_users.html', context=context)


@login_required
def unfollow_user(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    if request.method == 'POST':
        request.user.follows.remove(user)
        return redirect('follow-users')

    return render(request, 'follows/unfollow_user.html', {'user': user})
