class Request:
    def __init__(self, format):
        self.format = format


class Handler:
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request):
        self.next_handler.handle(request)


class ErrorHandler(Handler):

    def handle(self, request):
        print("invalid request")


class PdfHandler(Handler):

    def handle(self, request):
        if request.format == "pdf":
            print("PDF handler is handling the request.")
        else:
            super(PdfHandler, self).handle(request=request)


class TextHandler(Handler):

    def handle(self, request):
        if request.format == "txt":
            print("TEXT handler is handling the request.")
        else:
            super(TextHandler, self).handle(request=request)


error_handler = ErrorHandler(next_handler=None)
text_handler = TextHandler(next_handler=error_handler)
pdf_handler = PdfHandler(next_handler=text_handler)

request = Request(format="pdf")

pdf_handler.handle(request=request)
