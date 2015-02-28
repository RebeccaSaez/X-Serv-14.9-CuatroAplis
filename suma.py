#!/usr/bin/python


class suma:
    def parse(self, request, rest):
            try:
                num1 = int(rest.split("/")[1])
                num2 = int(rest.split("/")[2])
            except ValueError:
                return None
            return (num1, num2)

    def process(self, parsedRequest):
        if not parsedRequest:
            return("400 Bad Request", "<html>" +
                   "<body><h1>Error: introduce un numero</h1>" +
                   "</body></html>")

        resultado = (str(parsedRequest[0]) + " + " +
                         str(parsedRequest[1]) + " = " +
                         str(parsedRequest[0] + parsedRequest[1]))

        return("200 OK", "<html>" +
               "<body><h1>" + resultado + "</h1></body></html>")
