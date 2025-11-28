"""
Stealth Mode - Avoid detection when downloading from Apple Music
Simulates human-like listening behavior with delays and limits.
"""

import json
import random
import time
from datetime import datetime, date
from pathlib import Path
from .otsconfig import config
from .runtimedata import get_logger

logger = get_logger("stealth")

# Stats file location
STATS_FILE = Path.home() / '.config' / 'onthespot' / 'stealth_stats.json'


def _load_stats():
    """Load daily stats from file."""
    try:
        if STATS_FILE.exists():
            data = json.loads(STATS_FILE.read_text())
            # Reset if it's a new day
            if data.get('date') != str(date.today()):
                return _reset_stats()
            return data
    except Exception as e:
        logger.warning(f"Failed to load stealth stats: {e}")
    return _reset_stats()


def _reset_stats():
    """Reset stats for a new day."""
    return {
        'date': str(date.today()),
        'tracks_today': 0,
        'tracks_this_hour': 0,
        'hour': datetime.now().hour,
        'session_tracks': 0,
        'last_download_time': 0
    }


def _save_stats(stats):
    """Save stats to file."""
    try:
        STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATS_FILE.write_text(json.dumps(stats, indent=2))
    except Exception as e:
        logger.warning(f"Failed to save stealth stats: {e}")


def get_stealth_stats():
    """Get current stealth mode statistics."""
    stats = _load_stats()
    
    # Reset hourly count if hour changed
    current_hour = datetime.now().hour
    if stats.get('hour') != current_hour:
        stats['hour'] = current_hour
        stats['tracks_this_hour'] = 0
        _save_stats(stats)
    
    return stats


def can_download():
    """Check if we can download based on rate limits."""
    if not config.get('stealth_mode_enabled'):
        return True, ""
    
    stats = get_stealth_stats()
    
    # Check hourly limit
    max_per_hour = config.get('stealth_max_tracks_per_hour', 20)
    if stats['tracks_this_hour'] >= max_per_hour:
        minutes_left = 60 - datetime.now().minute
        return False, f"Hourly limit reached ({max_per_hour}/hr). Wait ~{minutes_left} min."
    
    # Check daily limit
    max_per_day = config.get('stealth_max_tracks_per_day', 100)
    if stats['tracks_today'] >= max_per_day:
        return False, f"Daily limit reached ({max_per_day}/day). Try again tomorrow."
    
    return True, ""


def increment_download_count():
    """Increment download counters after successful download."""
    stats = get_stealth_stats()
    stats['tracks_today'] += 1
    stats['tracks_this_hour'] += 1
    stats['session_tracks'] += 1
    stats['last_download_time'] = time.time()
    _save_stats(stats)
    
    logger.debug(f"Stealth stats: {stats['tracks_this_hour']}/hr, {stats['tracks_today']}/day")
    return stats


def calculate_stealth_delay(song_duration_ms, service="apple_music"):
    """
    Calculate human-like delay based on song duration.
    
    Args:
        song_duration_ms: Song duration in milliseconds
        service: The music service (only applies stealth to apple_music)
    
    Returns:
        Delay in seconds, or 0 if stealth mode disabled
    """
    if not config.get('stealth_mode_enabled') or service != "apple_music":
        return config.get('download_delay', 3)
    
    # Get config values
    min_delay = config.get('stealth_min_delay', 30)
    song_ratio = config.get('stealth_song_delay_ratio', 0.5)
    random_var = config.get('stealth_random_variation', 0.3)
    
    # Convert song duration to seconds
    song_duration_sec = (song_duration_ms or 180000) / 1000  # Default 3 min
    
    # Calculate base delay (half of song duration)
    base_delay = song_duration_sec * song_ratio
    
    # Add random variation (±30%)
    variation = base_delay * random_var
    delay = base_delay + random.uniform(-variation, variation)
    
    # Ensure minimum delay
    delay = max(delay, min_delay)
    
    # Occasionally add extra "distraction" time (10% chance)
    if random.random() < 0.1:
        extra = random.uniform(30, 120)  # 30 sec to 2 min extra
        delay += extra
        logger.debug(f"Adding distraction delay: +{extra:.0f}s")
    
    return delay


def check_session_break():
    """
    Check if we need to take a session break.
    
    Returns:
        (needs_break, break_duration_seconds)
    """
    if not config.get('stealth_mode_enabled'):
        return False, 0
    
    stats = get_stealth_stats()
    break_threshold = config.get('stealth_session_break_tracks', 15)
    
    if stats['session_tracks'] >= break_threshold:
        # Reset session counter
        stats['session_tracks'] = 0
        _save_stats(stats)
        
        break_minutes = config.get('stealth_session_break_minutes', 5)
        # Add some randomness to break duration
        break_seconds = break_minutes * 60 * random.uniform(0.8, 1.2)
        
        return True, break_seconds
    
    return False, 0

