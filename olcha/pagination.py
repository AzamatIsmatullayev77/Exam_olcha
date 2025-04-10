from rest_framework.pagination import PageNumberPagination

# Custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Sahifadagi elementlar soni
    page_size_query_param = 'page_size'  # So‘rovda sahifa hajmini o‘zgartirish imkoniyati
    max_page_size = 100  # Maksimal sahifa hajmi
