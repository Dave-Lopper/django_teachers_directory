from .list_views import index
from .form_views import subject_add, teacher_bulk_add, teacher_add, signup
from .detail_views import teacher, subject

__all__ = [
    "index",
    "subject",
    "subject_add",
    "teacher",
    "teacher_add",
    "teacher_bulk_add",
    "signup"]
