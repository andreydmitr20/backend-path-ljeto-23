from django.db import models


class Band(models.Model):
    """music band"""

    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)
    image = models.URLField(default="")
    description = models.CharField(max_length=500, default="")

    def __str__(self):
        """string representation"""
        return self.name + " " + ("- rocks" if self.can_rock else "")


class Member(models.Model):
    """member of the band"""

    name = models.CharField("member's name", max_length=200)

    instrument_translator = (
        ("g", "Guitar"),
        ("b", "Bass"),
        ("d", "Drum"),
    )
    instruments = models.CharField(
        choices=instrument_translator,
        max_length=1,
    )
    band = models.ForeignKey("Band", on_delete=models.CASCADE)

    def __str__(self):
        """string representation"""

        instrument_name = ""
        for instrument in self.instrument_translator:
            if instrument[0] == self.instruments:
                instrument_name = instrument[1]
                break
        return f"{self.name}, {instrument_name}"
