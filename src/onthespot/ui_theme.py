"""
Modern Spotify-inspired UI Theme for OnTheSpot
Features: Dark theme, green accents, rounded corners, smooth animations
"""

# Spotify Color Palette
COLORS = {
    'background': '#121212',
    'background_alt': '#181818',
    'background_elevated': '#282828',
    'background_hover': '#333333',
    'surface': '#1a1a1a',
    'accent': '#1DB954',  # Spotify Green
    'accent_hover': '#1ed760',
    'accent_pressed': '#169c46',
    'text_primary': '#ffffff',
    'text_secondary': '#b3b3b3',
    'text_muted': '#727272',
    'border': '#404040',
    'success': '#1DB954',
    'warning': '#f59e0b',
    'error': '#ef4444',
    'info': '#3b82f6',
    'progress_bg': '#404040',
}

def get_modern_theme():
    """Returns the complete modern Spotify-inspired stylesheet."""
    return f"""
    /* ============================================ */
    /*  GLOBAL STYLES                              */
    /* ============================================ */
    
    QMainWindow, QWidget {{
        background-color: {COLORS['background']};
        color: {COLORS['text_primary']};
        font-family: 'SF Pro Display', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
        font-size: 13px;
    }}
    
    /* ============================================ */
    /*  TABS                                       */
    /* ============================================ */
    
    QTabWidget::pane {{
        border: none;
        background-color: {COLORS['background']};
    }}
    
    QTabBar::tab {{
        background-color: {COLORS['background_alt']};
        color: {COLORS['text_secondary']};
        padding: 10px 20px;
        margin-right: 2px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        border: none;
        font-weight: 500;
    }}
    
    QTabBar::tab:selected {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
    }}
    
    QTabBar::tab:hover:!selected {{
        background-color: {COLORS['background_hover']};
        color: {COLORS['text_primary']};
    }}
    
    /* ============================================ */
    /*  BUTTONS                                    */
    /* ============================================ */
    
    QPushButton {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        min-height: 20px;
    }}
    
    QPushButton:hover {{
        background-color: {COLORS['background_hover']};
    }}
    
    QPushButton:pressed {{
        background-color: {COLORS['border']};
    }}
    
    QPushButton:disabled {{
        background-color: {COLORS['surface']};
        color: {COLORS['text_muted']};
    }}
    
    /* Primary accent buttons */
    QPushButton#btn_search, QPushButton#btn_login_add {{
        background-color: {COLORS['accent']};
        color: #000000;
    }}
    
    QPushButton#btn_search:hover, QPushButton#btn_login_add:hover {{
        background-color: {COLORS['accent_hover']};
    }}
    
    QPushButton#btn_search:pressed, QPushButton#btn_login_add:pressed {{
        background-color: {COLORS['accent_pressed']};
    }}
    
    /* ============================================ */
    /*  INPUT FIELDS                               */
    /* ============================================ */
    
    QLineEdit, QTextEdit, QPlainTextEdit {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 2px solid {COLORS['border']};
        border-radius: 8px;
        padding: 10px 14px;
        selection-background-color: {COLORS['accent']};
        selection-color: #000000;
    }}
    
    QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
        border-color: {COLORS['accent']};
    }}
    
    QLineEdit:hover, QTextEdit:hover, QPlainTextEdit:hover {{
        border-color: {COLORS['text_muted']};
    }}
    
    /* ============================================ */
    /*  COMBO BOX / DROPDOWN                       */
    /* ============================================ */
    
    QComboBox {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 2px solid {COLORS['border']};
        border-radius: 8px;
        padding: 8px 14px;
        min-height: 20px;
    }}
    
    QComboBox:hover {{
        border-color: {COLORS['text_muted']};
    }}
    
    QComboBox:focus {{
        border-color: {COLORS['accent']};
    }}
    
    QComboBox::drop-down {{
        border: none;
        width: 30px;
    }}
    
    QComboBox QAbstractItemView {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 1px solid {COLORS['border']};
        border-radius: 8px;
        selection-background-color: {COLORS['accent']};
        selection-color: #000000;
    }}
"""

def get_modern_theme_part2():
    """Returns part 2 of the theme (split due to size)."""
    return f"""
    /* ============================================ */
    /*  TABLES                                     */
    /* ============================================ */
    
    QTableWidget, QTableView {{
        background-color: {COLORS['background']};
        alternate-background-color: {COLORS['background_alt']};
        color: {COLORS['text_primary']};
        border: none;
        border-radius: 8px;
        gridline-color: {COLORS['surface']};
        selection-background-color: {COLORS['background_hover']};
        selection-color: {COLORS['text_primary']};
    }}
    
    QTableWidget::item, QTableView::item {{
        padding: 8px;
        border: none;
    }}
    
    QTableWidget::item:selected, QTableView::item:selected {{
        background-color: {COLORS['background_hover']};
    }}
    
    QTableWidget::item:hover, QTableView::item:hover {{
        background-color: {COLORS['background_elevated']};
    }}
    
    QHeaderView::section {{
        background-color: {COLORS['surface']};
        color: {COLORS['text_secondary']};
        padding: 10px;
        border: none;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 11px;
    }}
    
    QHeaderView::section:hover {{
        background-color: {COLORS['background_elevated']};
    }}
    
    /* ============================================ */
    /*  SCROLLBARS                                 */
    /* ============================================ */
    
    QScrollBar:vertical {{
        background-color: {COLORS['background']};
        width: 12px;
        border-radius: 6px;
    }}
    
    QScrollBar::handle:vertical {{
        background-color: {COLORS['border']};
        border-radius: 6px;
        min-height: 30px;
    }}
    
    QScrollBar::handle:vertical:hover {{
        background-color: {COLORS['text_muted']};
    }}
    
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        height: 0px;
    }}
    
    QScrollBar:horizontal {{
        background-color: {COLORS['background']};
        height: 12px;
        border-radius: 6px;
    }}
    
    QScrollBar::handle:horizontal {{
        background-color: {COLORS['border']};
        border-radius: 6px;
        min-width: 30px;
    }}
    
    QScrollBar::handle:horizontal:hover {{
        background-color: {COLORS['text_muted']};
    }}
    
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
        width: 0px;
    }}
    
    /* ============================================ */
    /*  PROGRESS BARS                              */
    /* ============================================ */
    
    QProgressBar {{
        background-color: {COLORS['progress_bg']};
        border: none;
        border-radius: 6px;
        text-align: center;
        color: {COLORS['text_primary']};
        font-weight: 600;
        min-height: 24px;
    }}
    
    QProgressBar::chunk {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {COLORS['accent']}, stop:1 {COLORS['accent_hover']});
        border-radius: 6px;
    }}
    
    /* ============================================ */
    /*  CHECKBOXES & RADIO BUTTONS                */
    /* ============================================ */
    
    QCheckBox {{
        color: {COLORS['text_primary']};
        spacing: 8px;
    }}
    
    QCheckBox::indicator {{
        width: 20px;
        height: 20px;
        border-radius: 4px;
        border: 2px solid {COLORS['border']};
        background-color: {COLORS['background_elevated']};
    }}
    
    QCheckBox::indicator:checked {{
        background-color: {COLORS['accent']};
        border-color: {COLORS['accent']};
    }}
    
    QCheckBox::indicator:hover {{
        border-color: {COLORS['text_muted']};
    }}
    
    QRadioButton {{
        color: {COLORS['text_primary']};
        spacing: 8px;
    }}
    
    QRadioButton::indicator {{
        width: 20px;
        height: 20px;
        border-radius: 10px;
        border: 2px solid {COLORS['border']};
        background-color: {COLORS['background_elevated']};
    }}
    
    QRadioButton::indicator:checked {{
        background-color: {COLORS['accent']};
        border-color: {COLORS['accent']};
    }}
"""

def get_modern_theme_part3():
    """Returns part 3 of the theme."""
    return f"""
    /* ============================================ */
    /*  LABELS                                     */
    /* ============================================ */
    
    QLabel {{
        color: {COLORS['text_primary']};
        background-color: transparent;
    }}
    
    /* ============================================ */
    /*  GROUP BOX                                  */
    /* ============================================ */
    
    QGroupBox {{
        background-color: {COLORS['background_alt']};
        border: 1px solid {COLORS['border']};
        border-radius: 10px;
        margin-top: 12px;
        padding-top: 10px;
        font-weight: 600;
    }}
    
    QGroupBox::title {{
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 5px 10px;
        color: {COLORS['text_primary']};
    }}
    
    /* ============================================ */
    /*  SPIN BOX                                   */
    /* ============================================ */
    
    QSpinBox, QDoubleSpinBox {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 2px solid {COLORS['border']};
        border-radius: 8px;
        padding: 6px 10px;
    }}
    
    QSpinBox:focus, QDoubleSpinBox:focus {{
        border-color: {COLORS['accent']};
    }}
    
    QSpinBox::up-button, QSpinBox::down-button,
    QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {{
        background-color: {COLORS['background_hover']};
        border: none;
        width: 20px;
    }}
    
    /* ============================================ */
    /*  SLIDER                                     */
    /* ============================================ */
    
    QSlider::groove:horizontal {{
        background-color: {COLORS['progress_bg']};
        height: 6px;
        border-radius: 3px;
    }}
    
    QSlider::handle:horizontal {{
        background-color: {COLORS['accent']};
        width: 16px;
        height: 16px;
        margin: -5px 0;
        border-radius: 8px;
    }}
    
    QSlider::handle:horizontal:hover {{
        background-color: {COLORS['accent_hover']};
    }}
    
    QSlider::sub-page:horizontal {{
        background-color: {COLORS['accent']};
        border-radius: 3px;
    }}
    
    /* ============================================ */
    /*  SCROLL AREA                                */
    /* ============================================ */
    
    QScrollArea {{
        background-color: {COLORS['background']};
        border: none;
    }}
    
    QScrollArea > QWidget > QWidget {{
        background-color: {COLORS['background']};
    }}
    
    /* ============================================ */
    /*  TOOLTIPS                                   */
    /* ============================================ */
    
    QToolTip {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 1px solid {COLORS['border']};
        border-radius: 6px;
        padding: 6px 10px;
    }}
    
    /* ============================================ */
    /*  STATUS BAR                                 */
    /* ============================================ */
    
    QStatusBar {{
        background-color: {COLORS['surface']};
        color: {COLORS['text_secondary']};
        border-top: 1px solid {COLORS['border']};
        padding: 4px;
    }}
    
    QStatusBar::item {{
        border: none;
    }}
    
    /* ============================================ */
    /*  MENU                                       */
    /* ============================================ */
    
    QMenu {{
        background-color: {COLORS['background_elevated']};
        color: {COLORS['text_primary']};
        border: 1px solid {COLORS['border']};
        border-radius: 8px;
        padding: 4px;
    }}
    
    QMenu::item {{
        padding: 8px 20px;
        border-radius: 4px;
    }}
    
    QMenu::item:selected {{
        background-color: {COLORS['background_hover']};
    }}
    
    /* ============================================ */
    /*  DIALOG                                     */
    /* ============================================ */
    
    QDialog {{
        background-color: {COLORS['background']};
        color: {COLORS['text_primary']};
    }}
"""

def get_complete_theme():
    """Returns the complete stylesheet."""
    return get_modern_theme() + get_modern_theme_part2() + get_modern_theme_part3()


# Status badge styles for download queue
def get_status_style(status):
    """Returns the style for a given download status."""
    styles = {
        'downloading': f'background-color: {COLORS["info"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'completed': f'background-color: {COLORS["success"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'downloaded': f'background-color: {COLORS["success"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'failed': f'background-color: {COLORS["error"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'waiting': f'background-color: {COLORS["warning"]}; color: #000; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'cancelled': f'background-color: {COLORS["text_muted"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'already exists': f'background-color: {COLORS["text_muted"]}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
        'rate limited': f'background-color: {COLORS["warning"]}; color: #000; padding: 4px 12px; border-radius: 12px; font-weight: 600;',
    }
    # Check for partial matches (e.g., "✓ Done · Wait 1m 30s")
    status_lower = status.lower()
    if 'wait' in status_lower or 'done' in status_lower:
        return styles['completed']
    if 'download' in status_lower:
        return styles['downloading']
    return styles.get(status_lower, f'background-color: {COLORS["background_elevated"]}; color: {COLORS["text_primary"]}; padding: 4px 12px; border-radius: 12px;')


def get_progress_bar_style(status='default'):
    """Returns animated progress bar style."""
    if status == 'completed':
        color = COLORS['success']
    elif status == 'failed':
        color = COLORS['error']
    elif status == 'waiting':
        color = COLORS['warning']
    else:
        color = COLORS['accent']

    return f"""
        QProgressBar {{
            background-color: {COLORS['progress_bg']};
            border: none;
            border-radius: 6px;
            text-align: center;
            color: {COLORS['text_primary']};
            font-weight: 600;
            min-height: 26px;
        }}
        QProgressBar::chunk {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {color}, stop:0.5 {COLORS['accent_hover']}, stop:1 {color});
            border-radius: 6px;
        }}
    """


def format_duration(ms):
    """Format duration in milliseconds to MM:SS or HH:MM:SS."""
    if not ms:
        return "--:--"
    try:
        total_seconds = int(ms) // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "--:--"


def format_speed(bytes_per_sec):
    """Format download speed to human readable format."""
    if not bytes_per_sec or bytes_per_sec <= 0:
        return "-- KB/s"
    if bytes_per_sec >= 1024 * 1024:
        return f"{bytes_per_sec / (1024 * 1024):.1f} MB/s"
    elif bytes_per_sec >= 1024:
        return f"{bytes_per_sec / 1024:.1f} KB/s"
    else:
        return f"{bytes_per_sec:.0f} B/s"

