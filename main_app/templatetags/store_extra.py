from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime, timezone, timedelta

register = template.Library()


@register.filter
@stringfilter
def format_vnd(value):
    value = int(value)
    return "{:,}₫".format(value)

@register.filter
@stringfilter
def format_datetime(value):
    # Define the original time with UTC offset
    orig_time = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z')

    # Convert to UTC timezone (assuming original time is in UTC)
    utc_time = orig_time.replace(tzinfo=timezone.utc)

    # Define the target timezone (+07:00)
    target_tz = timezone(timedelta(hours=7))

    # Convert to target timezone (+07:00)
    return utc_time.astimezone(target_tz).strftime('%Y-%m-%d %H:%M:%S')

@register.filter
@stringfilter
def format_date_for_input(value):
    # Define the original time with UTC offset
    orig_time = datetime.strptime(value, '%Y-%m-%d')

    # Convert to UTC timezone (assuming original time is in UTC)
    utc_time = orig_time.replace(tzinfo=timezone.utc)

    # Define the target timezone (+07:00)
    target_tz = timezone(timedelta(hours=7))

    # Convert to target timezone (+07:00)
    return utc_time.astimezone(target_tz).strftime('%Y-%m-%d')
