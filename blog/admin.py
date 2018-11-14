from django.contrib import admin

from .models import Blog
from .models import Author
from .models import Entry
from .models import Categoria
from .models import Produto


admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Categoria)
admin.site.register(Produto)