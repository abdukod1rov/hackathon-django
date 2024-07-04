from django.shortcuts import render
from events.models import Event
from django.utils import timezone


def index(request):
    now = timezone.now()
    active_hackathons = Event.objects.filter(is_approved=True,
                                             start_date__lt=now,
                                             end_date__gt=now)
    past_hackathons = Event.objects.filter(is_approved=True,
                                           end_date__lt=now)
    upcoming_hackathons = Event.objects.filter(is_approved=True,
                                               start_date__gt=now)
    context = {
        'active_hackathons': active_hackathons,
        'past_hackathons': past_hackathons,
        'upcoming_hackathons': upcoming_hackathons
    }
    return render(request, 'home.html', context)
