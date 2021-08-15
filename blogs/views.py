from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Post, Comment


# Create your views here.
def home_view(request):
    object_list = Post.objects.all()
    return render(request, 'home.html', {
        'object_list': object_list
    })


def about_view(request):
    return render(request, 'about.html')


class DetailPost(DetailView):
    model = Post
    template_name = 'detail_post.html'


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'description', 'image')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Added Post Successfully')
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'description', 'image')


class DeletePost(DeleteView):
    model = Post
    template_name = 'detail_post.html'
    success_url = reverse_lazy('home')


class AddCommentPost(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('name', 'body')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        messages.success(self.request, 'Comment Added')
        return super().form_valid(form)

    def get_success_url(self):
        postid = self.kwargs['pk']
        return reverse_lazy('detailpost', kwargs={'pk': postid})

