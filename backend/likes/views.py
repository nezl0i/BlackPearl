from django.http import JsonResponse
from django.template.loader import render_to_string
from likes.models import PostLikes
from posts.models import Post
from users.models import User
from django.middleware.csrf import get_token


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_like(request):
    if is_ajax(request=request):
        post_id = int(request.POST.get('post_id'))
        user_id = int(request.user.pk)
        token = get_token(request)
        try:
            post_likes = PostLikes.objects.get(post__id=post_id, liked_by=request.user.id).like
        except (Exception,):
            post_likes = False

        # likes_counter = PostLikes.objects.filter(post__id=post_id, like=True).count()
        data = {
            'post_id': post_id,
            'csrf_token': token,
            'is_liked': not post_likes,
            'user_id': user_id,
            # 'likes_counter': likes_counter,
        }

        if post_likes:
            post_like = PostLikes.objects.get(post_id=post_id, liked_by=user_id)
            post_like.delete()
        else:
            user_inst = User.objects.get(id=user_id)
            post_inst = Post.objects.get(id=post_id)

            post_like = PostLikes(post=post_inst, liked_by=user_inst, like=True)
            post_like.save()

        result = render_to_string('includes/add_like.html', data)

        # return JsonResponse(data, safe=False)
        return JsonResponse({'result': result})
