from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail




def post_share(request, slug):
    # Retrieve post by id
    post = get_object_or_404(Post, slug=slug, status='published')
    sent=False
    if request.method == 'POST':
# Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
# Form fields passed validation
            cd = form.cleaned_data
# ... send email
            post_url=request.build.absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'. format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message,'bgaire2053@gmail.com',[cd['to']])
            sent=True
    else:
        form = EmailPostForm()
    print(sent)
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent':sent})


def post_list(request):

     #posts=Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        ###exceptiom is reaming to read......
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #return render(request,'blog/post/blog.html',{'posts':posts,'page':page})
    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})





def post_detail(request,year,month,day,slug):
    post=get_object_or_404(Post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           slug=slug)
    comments=post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    return render(request,'blog/post/index.html',{'post':post,'comments':comments,'comment_form':comment_form,'slug':slug})
              # List of active comments for this post
#     comments = post.comments.filter(active=True)
#      if request.method == 'POST':
#          #  A comment was posted
#           comment_form = CommentForm(data=request.POST)
#          if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#              # Assign the current post to the comment
#             new_comment.post = post
#                 # Save the comment to the database
#             new_comment.save()
#     else:
# comment_form = CommentForm()
#
#    #0comment_form =CommentForm()
    #return render(request,'blog/post/detail.html',{'post':post})
        # a=year
        # b=month
        # c=day
        # d=slug
        # print(a,b,c,d)


# Create your views here.
