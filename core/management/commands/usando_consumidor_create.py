import json

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "i need somebody help"

    def _callback(self, channel, method, properties, body):
        payload = json.loads(body)
        nome = payload.get('nome')
        descricao = payload.get('descricao')
        if descricao is None:
            pass
        else:
            if nome is not None:
                ingrediente = Ingrediente.objects.create(nome=nome, descricao=descricao)
                ingrediente.save()
                print(f'O Ingrediente foi criado!!! {ingrediente}')

    def handle(self, *args, **options):
        consumer.consume(
            exchange='ingredientes',
            queue_name='ingredientes-novos',
            routing_key='ingrediente.novo',
            callback=self._callback,
        )
