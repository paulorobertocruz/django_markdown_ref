from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from django.core.exceptions import ObjectDoesNotExist

def is_option(full_text):
    full_text = full_text.strip()
    if full_text[0:2] == "@:":
        return full_text[2:]
    else:
        return None

class DjangoRefTreeProcessor(Treeprocessor):

    def run(self, root):
        if self.model is None:
            return
        
        for tag in root.iter("img"):
            if "src" in tag.attrib:
                pk_id = is_option(tag.get("src"))
                if pk_id is not None:
                    try:
                        image = self.model.objects.get(pk = pk_id)
                        tag.set("src", image.get_url())
                    except ObjectDoesNotExist:
                        pass
                    except AttributeError:
                        pass
                    except ValueError:
                        pass
        
        for tag in root.iter("a"):
            if "href" in tag.attrib:
                pk_id = is_option(tag.get("href"))
                if pk_id is not None:
                    try:
                        image = self.model.objects.get(pk = pk_id)
                        tag.set("href", image.get_url())
                    except ObjectDoesNotExist:
                        pass
                    except AttributeError:
                        pass
                    except ValueError:
                        pass



class DjangoMarkdownRef(Extension):
    
    model = None

    def __init__(self, **kwargs):
        self.config = {}
        super(DjangoMarkdownRef, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        django_ref_treeprocessor = DjangoRefTreeProcessor(md)
        django_ref_treeprocessor.config = self.getConfigs()
        django_ref_treeprocessor.model = self.model
        md.treeprocessors.add('django_ref_treeprocessor', django_ref_treeprocessor, '_end' )


def makeExtension(**kwargs):
    return DjangoMarkdownRef(**kwargs)