"""
Twitter (X) integration service.

This module is SAFE to use even if API credentials are missing.
The application will continue to work without crashing.
"""

import os
import tweepy
from django.conf import settings


def post_tweet(text, image_url=None):
    """
    Post a tweet to X (Twitter).
    If credentials are missing, the tweet is skipped safely.
    """

    # ✅ Check credentials first
    api_key = getattr(settings, "X_API_KEY", None)
    api_secret = getattr(settings, "X_API_SECRET", None)
    access_token = getattr(settings, "X_ACCESS_TOKEN", None)
    access_secret = getattr(settings, "X_ACCESS_SECRET", None)

    if not all([api_key, api_secret, access_token, access_secret]):
        print("⚠️ X API credentials not set — tweet skipped.")
        return

    try:
        # Authenticate
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )

        # Post tweet (text-only)
        client.create_tweet(text=text)

        print("✅ Tweet posted successfully")

    except Exception as e:
        # ❗ Never crash the app
        print(f"❌ Twitter error: {e}")
