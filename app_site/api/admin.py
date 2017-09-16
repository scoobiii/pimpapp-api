from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db import models

from .models import UserProfile

from .models import Catador
from .models import Material
from .models import MobileCatador
from .models import MobileCooperative
from .models import Mobile
from .models import LatitudeLongitude
from .models import Collect
from .models import PhotoCollectUser
from .models import PhotoCollectCatador
from .models import Residue
from .models import PhotoResidue
from .models import GeorefResidue
from .models import RatingCatador
from .models import RatingCooperative
from .models import PhotoCooperative
from .models import Partner
from .models import Cooperative
from .models import PhotoBase
from .models import PhotoCatador
from .models import GeorefCatador
from .models import Rating


from .forms import DaysWeekWorkAdminForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True
    verbose_name_plural = 'Profiles'


class CatadorAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name')
    search_fields = ['id', 'name']
    form = DaysWeekWorkAdminForm
    list_display = ('pk', 'name', 'catador_type', 'city', 'country')
    filter_vertical = ['materials_collected']


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name', 'get_avatar')

    def get_avatar(self, x):
        up = UserProfile.objects.get(user=x)
        return True if up.avatar else False

    get_avatar.short_description = 'Possui foto?'
    get_avatar.boolean = True
    get_avatar.admin_order_field = 'userprofile__avatar'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Catador, CatadorAdmin)
admin.site.register(Material, SimpleHistoryAdmin)
admin.site.register(LatitudeLongitude, SimpleHistoryAdmin)
admin.site.register(Collect)
admin.site.register(PhotoCollectUser)
admin.site.register(PhotoCollectCatador)
admin.site.register(Residue)
admin.site.register(PhotoResidue)
admin.site.register(GeorefResidue)
admin.site.register(RatingCatador)
admin.site.register(RatingCooperative)
admin.site.register(PhotoCooperative)
admin.site.register(Partner)
admin.site.register(Cooperative)
admin.site.register(MobileCatador)
admin.site.register(MobileCooperative)
admin.site.register(PhotoBase)
admin.site.register(PhotoCatador)
admin.site.register(Mobile)
admin.site.register(GeorefCatador)
admin.site.register(Rating)
