"""
Twitter (X) integration service.

This module is SAFE to use even if API credentials are missing.
The application will continue to work without crashing,
but API usage and errors will always be visible.
"""

import tweepy
from django.conf import settings


def post_tweet(text, image_url=None):
    """
    Post a tweet to X (Twitter).

    This function is intentionally verbose so that:
    - API usage is visible
    - HTTP errors can be inspected
    - The app never crashes
    """

    api_key = getattr(settings, "X_API_KEY", None)
    api_secret = getattr(settings, "X_API_SECRET", None)
    access_token = getattr(settings, "X_ACCESS_TOKEN", None)
    access_secret = getattr(settings, "X_ACCESS_SECRET", None)

    # ❗ Do NOT silently skip — log clearly
    if not all([api_key, api_secret, access_token, access_secret]):
        print(
            "⚠️ X API credentials are missing. "
            "Tweet attempt made but cannot be sent."
        )
        return

    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )

        response = client.create_tweet(text=text)

        # ✅ Log HTTP response details
        print("✅ Tweet request sent to X")
        print("📡 X API response:", response)

    except tweepy.TweepyException as e:
        # 🔍 Explicit API error (mentor wants this)
        print("❌ X API request failed")
        print("📡 X API error response:", e)

    except Exception:
        # ❗ Safety net
        print("❌ Unexpected Twitter error occurred")

