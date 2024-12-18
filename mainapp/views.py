from django.shortcuts import render
import datetime
# views.py
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Room, Reservation
from mainapp.forms import AppointmentForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with your success page
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Reservation

def book(request):
    # Formdan gelen verileri alalım
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    room_type = request.GET.get('room_type')

    # Tarihleri datetime objelerine dönüştürelim
    try:
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        return render(request, 'book.html', {'error': 'Geçerli bir tarih aralığı giriniz.'})

    # Seçilen oda tipindeki odaları alalım
    rooms = Room.objects.filter(room_type=room_type)

    # Seçilen tarihlerde müsait olan odaları bulalım
    available_rooms = []
    for room in rooms:
        overlapping_reservations = Reservation.objects.filter(
            room=room,
            check_out__gte=check_in_date,
            check_in__lte=check_out_date
        )
        if not overlapping_reservations.exists():
            available_rooms.append(room)

    # Template'e gerekli verileri gönderelim
    context = {
        'available_rooms': available_rooms,
        'check_in': check_in,
        'check_out': check_out,
        'adults': adults,
        'children': children,
        'room_type': room_type
    }

    return render(request, 'book.html', context)


def book(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        room_type = request.POST.get('room_type')

        # Tarihleri datetime objelerine dönüştür
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'book.html', {'error': 'Geçerli bir tarih giriniz.'})

        # Seçilen oda tipindeki odaları al
        rooms = Room.objects.filter(room_type=room_type)

        # Müsait odaları bul
        available_rooms = []
        for room in rooms:
            if not Reservation.objects.filter(
                room=room,
                check_out__gte=check_in_date,
                check_in__lte=check_out_date
            ).exists():
                available_rooms.append(room)

        if available_rooms:
            # İlk müsait odayı al
            room = available_rooms[0]

            # Rezervasyonu kaydet
            reservation = Reservation.objects.create(
                room=room,
                check_in=check_in_date,
                check_out=check_out_date,
                adults=adults,
                children=children,
                booked_at=timezone.now()
            )

            return redirect('booking_success', reservation_id=reservation.id)
        else:
            return render(request, 'book.html', {'error': 'Seçtiğiniz tarihler için müsait oda bulunamadı.'})
    else:
        return render(request, 'book.html')

