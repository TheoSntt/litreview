from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from follows.forms import FollowUsersForm
from django.contrib.auth import get_user_model
from follows.models import UserFollows

@login_required
def follow_users(request):
    User = get_user_model()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            Follows = UserFollows.objects.create(user=request.user, followed_user=user)
            return redirect('follow-users')
    followed_users = request.user.follows.all()
    users_to_follow = User.objects.exclude(id=request.user.id).exclude(id__in=followed_users)
    context = {
        'users_to_follow' : users_to_follow,
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

    return render(request,
                    'follows/unfollow_user.html',
                    {'user': user})