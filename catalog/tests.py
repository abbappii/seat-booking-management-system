
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Venue, Seat, SeatType, Booking, Event

class BookingAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create a Venue
        self.venue = Venue.objects.create(name="Test Venue", location="Test Location", capacity=100, total_seats=100)
        self.venue_2 = Venue.objects.create(
            name="Test Venue 2", location="Test Location", capacity=100, total_seats=100
        )
        # Creating a Seat Type
        self.seat_type = SeatType.objects.create(name="VIP", price_multiplier=2.0)
        self.seat_type_2 = SeatType.objects.create(name="Average", price_multiplier=1.2)

        # Creating an Event
        self.event = Event.objects.create(
            name="Test Event",
            venue=self.venue,
            start_time="2024-09-01T10:00:00Z",
            end_time="2024-09-01T10:00:00Z",
        )

        # Creating a Seat
        self.seat = Seat.objects.create(
            venue=self.venue,
            event=self.event,
            seat_type=self.seat_type,
            seat_number="A1",
            price=200.0
        )
        self.seat_2 = Seat.objects.create(
            venue=self.venue_2,
            event=self.event,
            seat_type=self.seat_type_2,
            seat_number="B1",
            price=120.0,
        )
        self.booking = Booking.objects.create(
            user=self.user,
            seat=self.seat_2,
            booking_time="2024-09-01T10:00:00Z",
            payment_status=True,
            payment_amount=self.seat.price,
            payment_method="credit_card",
            transaction_id="123456",
            notes="Test Booking 2",
        )

    def test_create_booking(self):
        url = reverse('booking-list-create')
        data = {
            "seat_id": self.seat.id,
            "booking_time": "2024-09-01T12:00:00Z",
            "payment_status": True,
            "payment_amount": self.seat.price,
            "payment_method": "credit_card",
            "transaction_id": "7891011",
            "notes": "New Booking"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['seat']['id'], self.seat.id)

        # Attempt to create a duplicate booking for the same seat
        duplicate_response = self.client.post(url, data, format="json")
        self.assertEqual(duplicate_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", duplicate_response.data)
        self.assertEqual(
            duplicate_response.data["non_field_errors"][0],
            "This seat is already booked and not available for booking.",
        )

    def test_retrieve_booking(self):
        url = reverse("booking-detail", args=[self.booking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.booking.id)
        self.assertEqual(response.data["seat"]["id"], self.seat_2.id)

    def test_list_bookings(self):
        url = reverse("booking-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_booking(self):
        new_seat = Seat.objects.create(
            venue=self.venue,
            event=self.event,
            seat_type=self.seat_type,
            seat_number="A2",
            price=220.00,
        )
        url = reverse("booking-detail", args=[self.booking.id])
        data = {
            "seat_id": new_seat.id,
            "booking_time": "2024-09-01T12:30:00Z",
            "payment_status": True,
            "payment_amount": new_seat.price,
            "payment_method": "paypal",
            "transaction_id": "123457",
            "notes": "Updated Booking",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["seat"]["id"], new_seat.id)

    def test_delete_booking(self):
        url = reverse("booking-detail", args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())
