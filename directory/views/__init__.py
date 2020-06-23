from .auth_views import login_view, logout_view
from .detail_views import teacher, subject
from .form_views import subject_add, teacher_add, teacher_bulk_add, signup
from .list_views import index

__all__ = [
    "index",
    "login_view",
    "logout_view",
    "subject",
    "subject_add",
    "teacher",
    "teacher_add",
    "teacher_bulk_add",
    "signup"]
