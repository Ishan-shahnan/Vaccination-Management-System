from rest_framework import viewsets, permissions
from .models import VaccineCampaign, Booking, Review
from .serializers import VaccineCampaignSerializer, BookingSerializer, ReviewSerializer
from .permissions import IsDoctorOrReadOnly, CanReviewCampaign, IsOwnerOrReadOnly


class VaccineCampaignViewSet(viewsets.ModelViewSet):
    queryset = VaccineCampaign.objects.all()
    serializer_class = VaccineCampaignSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsDoctorOrReadOnly]

    def perform_create(self, serializer):
        # currently loged in doctor
        serializer.save(created_by=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # user only see their booking
        return Booking.objects.filter(patient=self.request.user)

    def perform_create(self, serializer):
        # current patient 
        serializer.save(patient=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanReviewCampaign]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
