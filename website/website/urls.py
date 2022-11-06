"""website URL Configuration
Below is particularly useful for me
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#send to second arg of path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
