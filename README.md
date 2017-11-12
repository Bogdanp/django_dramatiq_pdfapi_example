# django_dramatiq_pdfapi_example

This is the full code listing from my "Building a PDF API with Django
and Dramatiq" post which you can find [here][post].

## Setup

1. Clone the repo, then run `pipenv install`.
1. Run [RabbitMQ].
1. Run the web server: `python manage.py runserver`
1. Run the workers: `python manage.py rundramatiq`

## License

django_dramatiq_pdfapi_example is licensed under Apache 2.0.  Please
see [LICENSE][license] for licensing details.


[RabbitMQ]: https://rabbitmq.com
[license]: https://github.com/Bogdanp/django_dramatiq_pdfapi_example/blob/master/LICENSE
[post]: https://defn.io/2017/11/12/django-pdf-api/
