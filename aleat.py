#!/usr/bin/python

import random


class aleatorio:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 OK", "<html><body><h1>Solicita tu pagina aleatoria</h1>" +
                         "<a href='" + str(random.randrange(1000000)) +
                         "'>Dame otra</a></body></html>")
