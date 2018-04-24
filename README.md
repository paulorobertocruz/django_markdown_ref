# Como Usar

## GIT

### Clone o repositorio 

`git clone https://github.com/paulorobertocruz/django_markdown_ref.git`

### Ou adicione como submodulo

`git submodule add https://github.com/paulorobertocruz/django_markdown_ref.git`

## No Python

### Configuração
```
from django_markdown_ref.django_markdown_ref import DjangoMarkdownRef

ref = DjangoMarkdownRef()

ref.model = Model 

markdown("## Algum Markdown", extensions = [ref])
```

### Model

Defina o metodo abaixo no seu modelo 

```
def get_url(self):
    return "url/para/objeto"
```


## No Markdown
```
[Nome do link](@:id_do_objeto)
![Nome do image](@:id_do_objeto)
```