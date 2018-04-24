# Como Usar

## GIT

### Clone o repositorio 

`git clone https://github.com/paulorobertocruz/django_markdown_ref.git`

### Ou adicione como submodulo

`git submodule add https://github.com/paulorobertocruz/django_markdown_ref.git`

## No Python
```
from django_markdown_ref.django_markdown_ref import DjangoMarkdownRef

ref = DjangoMarkdownRef()

ref.model = Model 

markdown("## Algum Markdown", extensions = [ref])
```

## No Markdown
```
[Nome do link](@:id_do_objeto)
![Nome do image](@:id_do_objeto)
```