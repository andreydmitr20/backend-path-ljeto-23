from django.shortcuts import render
from .models import Band


def band_listing(request):
    """band listing"""
    bands = Band.objects.all().order_by("name")
    bands_carousel = Band.objects.all()[:3]
    return render(
        request,
        "bands/band_listing.html",
        {"bands": bands, "bands_carousel": bands_carousel},
    )


def home_page(request):
    """home page"""
    return render(request, "bands/index.html", {})


def band_detail(request, band_id: int):
    """band details"""
    band = Band.objects.get(pk=band_id)

    return render(request, "bands/band_detail.html", {"band": band})


def band_search(request):
    """band search"""
    pass
