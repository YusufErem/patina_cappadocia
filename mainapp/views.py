from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

def room_details(request, room_name):
    rooms = {
        'royal_room': 'Royal Oda Bilgileri',
        'exclusive_room': 'Exclusive Oda Bilgileri',
        'luxury_room': 'Luxury Oda Bilgileri',
        'executive_room': 'Executive Oda Bilgileri',
        'superior_room': 'Superior Oda Bilgileri',
    }
    room_info = rooms.get(room_name, 'Oda bilgisi bulunamadı.')
    return render(request, 'room_details.html', {'room_name': room_name, 'room_info': room_info})


def booking(request):
    return render(request, 'booking.html')

