# como usar

## git

### Clone o repositorio 

`git clone https://github.com/paulorobertocruz/django_markdown_ref.git`

### Adicione como submodulo

`git submodule add https://github.com/paulorobertocruz/django_markdown_ref.git`

## No Python

`from django_markdown_ref.django_markdown_ref import DjangoMarkdownRef`

`ref = DjangoMarkdownRef()`

`ref.model = Model` 

`markdown("## Algum Markdown", extensions = [ref])`

## No Markdown
[Nome do link](@:id_do_objeto)
