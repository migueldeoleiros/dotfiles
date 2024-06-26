# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'no-3rdparty', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'no-3rdparty', 'devtools://*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #0a091c'

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'top': 6, 'right': 8, 'bottom': 6, 'left': 8}

# Scaling factor for favicons in the tab bar. The tab size is unchanged,
# so big favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'top': 6, 'right': 8, 'bottom': 6, 'left': 8}

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 1

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#f8f8f2'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#0a091c'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#0a091c'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#f8f8f2'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#0a091c'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#0a091c'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#0a091c'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#f8f8f2'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#141329'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#141329'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#141329'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#ffb86c'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#f8f8f2'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#0a091c'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#0a091c'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#0a091c'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#ff5555'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#0a091c'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#bd93f9'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#0a091c'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#e0e0e0'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#bd93f9'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#141329'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#0a091c'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#ff5555'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#0a091c'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#0a091c'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#ff5555'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#0a091c'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#0a091c'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#6272a4'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#0a091c'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#0a091c'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#8be9fd'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #0a091c'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#0a091c'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#141329'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#f8f8f2'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#0a091c'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#ffffff'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#181920'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#ffb86c'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#0a091c'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#e0e0e0'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#0a091c'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#ff79c6'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#0a091c'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#e0e0e0'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#0a091c'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#ffb86c'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#0a091c'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#ffb86c'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#0a091c'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#0a091c'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#f8f8f2'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#ff5555'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#8be9fd'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#50fa7b'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#50fa7b'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#f1fa8c'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#141329'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#ffb86c'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#50fa7b'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#ff5555'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#f8f8f2'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#141329'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#f8f8f2'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#141329'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#f8f8f2'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#0a091c'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#f8f8f2'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#0a091c'

# Render all web contents using a dark theme. Example configurations
# from Chromium's `chrome://flags`:  - "With simple HSL/CIELAB/RGB-based
 # inversion": Set   `colors.webpage.darkmode.algorithm` accordingly.  -
 # "With selective image inversion": Set
 # `colors.webpage.darkmode.policy.images` to `smart`.  - "With selective
 # inversion of non-image elements": Set
 # `colors.webpage.darkmode.threshold.text` to 150 and
 # `colors.webpage.darkmode.threshold.background` to 205.  - "With
# selective inversion of everything": Combines the two variants   above.
 # Type: Bool

#import theme 
import themes.entropiaMono as theme

# Load existing settings made via :set
config.load_autoconfig()

theme.draw(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

#font
c.fonts.default_family = 'Roboto'
c.fonts.default_size = '10.5pt'

#force darkmode
config.set("colors.webpage.bg", "black")
config.set("colors.webpage.darkmode.enabled", True)
config.set("colors.webpage.darkmode.threshold.background", 100)
config.set("colors.webpage.darkmode.threshold.foreground", 256 - 100)
config.set("colors.webpage.darkmode.policy.images", 'smart')
config.set("colors.webpage.preferred_color_scheme", 'dark')

#stylesheets
# css = '~/.config/qutebrowser/css/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css'
# config.bind(',n', f'config-cycle content.user_stylesheets {css} ""')

# Bindings for normal mode
config.bind('<Ctrl+1>', 'tab-focus 1')
config.bind('<Ctrl+2>', 'tab-focus 2')
config.bind('<Ctrl+3>', 'tab-focus 3')
config.bind('<Ctrl+4>', 'tab-focus 4')
config.bind('<Ctrl+5>', 'tab-focus 5')
config.bind('<Ctrl+6>', 'tab-focus 6')
config.bind('<Ctrl+7>', 'tab-focus 7')
config.bind('<Ctrl+8>', 'tab-focus 8')
config.bind('<Ctrl+9>', 'tab-focus 9')
config.bind('<Shift+j>', 'tab-prev')
config.bind('<Shift+k>', 'tab-next')
#config.bind('<Shift+Escape>', 'clear-keychain ;; search ;; fullscreen --leave')

#download an image
config.bind('I', 'hint images download')

#mpv/vlc video
config.bind('M', 'hint links spawn mpv {hint-url}')
#config.bind('M', 'hint links spawn vlc {hint-url}')

#togle bars
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')

#deafult page
c.url.default_page = 'file:///home/miguel/.config/qutebrowser/homepage/homepage.html' 
c.url.start_pages = 'file:///home/miguel/.config/qutebrowser/homepage/homepage.html' 

#adblock
c.content.blocking.method = "both"

c.content.blocking.adblock.lists = ["https://easylist.to/easylist/easylist.txt", "https://easylist.to/easylist/easyprivacy.txt", "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt"]
