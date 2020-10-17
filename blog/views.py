from django.shortcuts import render
from django.views.generic import ListView, DetailView #  создавать и выводить посты , DetailView для вывода конкретной одной записи
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        ctx = super(HomeListView,self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3 #  какое число постов можно менять на странице

    def get_queryset(self):
        return Post.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(BlogListView,self).get_context_data(**kwargs)
        ctx['title'] = 'Страница блога!'
        return ctx

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(BlogDetailView,self).get_context_data(**kwargs)
        ctx['title'] = f'Запись - {Post.title}'
        return ctx
'''
details = [
    {
        'title': 'Контактные данные',
        'telephone_number': '880045612378',
        'additional_number': '89994567258',
        'email': 'adminblog@mail.ru',
        'name': 'Андрей',
        'surname': 'Иванов',
        'color': 'blue'
    }
]

data = {
        'posts': Post.objects.all(), 
        'title': 'Главная страница блога'
    }
contact_details = {
    'details': details,
    'title': 'Страница контактов'
}

def home(request):
    return render(request, 'blog/home.html', data)

### def contacts(request):
#    return render(request, 'blog/contacts.html', contact_details) 

def about_us(request):
    return HttpResponse('<h2 style="color:grey">О нас</h2>\n<p>Какой-то текст</p>')

def photos(request):
    return HttpResponse('<h2 style="color:blue">Страница фотографий</h2>\n<img src="https://i.pinimg.com/474x/33/8b/12/338b12ec51cc9ae2c25995f449c406ee.jpg" alt="Бабочка">')
'''



