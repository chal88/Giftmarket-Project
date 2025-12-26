"""Custom template filters for the shop app."""
from django import template

register = template.Library()


@register.filter
def average_rating(reviews):
    if not reviews:
        return 0
    return sum([r.rating for r in reviews]) / len(reviews)


@register.filter
def review_count(reviews):
    """Return the number of reviews."""
    return len(reviews)
