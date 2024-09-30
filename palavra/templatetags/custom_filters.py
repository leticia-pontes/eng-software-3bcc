from django import template

register = template.Library()

@register.filter(name='get')
def get(dicionario, chave):
    return dicionario.get(chave)
