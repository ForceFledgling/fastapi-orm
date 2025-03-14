from cotlette.middleware.csrf import get_token
from cotlette.utils.functional import lazy
from cotlette.utils.html import format_html
from cotlette.utils.safestring import SafeString


def csrf_input(request):
    return format_html(
        '<input type="hidden" name="csrfmiddlewaretoken" value="{}">',
        get_token(request),
    )


csrf_input_lazy = lazy(csrf_input, SafeString, str)
csrf_token_lazy = lazy(get_token, str)
