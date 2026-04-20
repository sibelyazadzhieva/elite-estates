from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from .forms import ReviewForm, ReviewSearchForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ReviewSerializer

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        min_rating = self.request.GET.get('min_rating')
        if query:
            queryset = queryset.filter(comment__icontains=query)
        if min_rating:
            queryset = queryset.filter(rating=min_rating)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ReviewSearchForm(self.request.GET)
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.property_id = self.kwargs['property_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('property_detail', kwargs={'pk': self.kwargs['property_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from properties.models import Property
        context['property'] = Property.objects.get(pk=self.kwargs['property_id'])
        return context

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author or self.request.user.is_superuser

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property'] = self.object.property
        return context

    def get_success_url(self):
        return reverse_lazy('review_list')

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]