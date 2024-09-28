from abc import ABC, abstractmethod


# 1. Define the Page abstraction
class Page(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self) -> str:
        pass


# 2. Implement concrete page classes
class SimplePage(Page):
    def __init__(self, title: str, content: str, renderer):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return self.renderer.render_simple_page(self.title, self.content)


class Product:
    def __init__(self, product_id: int, name: str, description: str, image: str):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.image = image


class ProductPage(Page):
    def __init__(self, product: Product, renderer):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return self.renderer.render_product_page(self.product)


# 3. Define the Renderer interface
class Renderer(ABC):
    @abstractmethod
    def render_simple_page(self, title: str, content: str) -> str:
        pass

    @abstractmethod
    def render_product_page(self, product: Product) -> str:
        pass


# 4. Implement concrete renderer classes
class HTMLRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> str:
        return f'<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{content}</p></body></html>'

    def render_product_page(self, product: Product) -> str:
        return (
            f'<html><head><title>{product.name}</title></head><body>'
            f'<h1>{product.name}</h1>'
            f"<img src='{product.image}' alt='{product.name}'/>"
            f'<p>ID: {product.product_id}</p>'
            f'<p>{product.description}</p></body></html>'
        )


class JsonRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> str:
        return f'{{"title": "{title}", "content": "{content}"}}'

    def render_product_page(self, product: Product) -> str:
        return (
            f'{{"product_id": {product.product_id}, "name": "{product.name}", '
            f'"description": "{product.description}", "image": "{product.image}"}}'
        )


class XmlRenderer(Renderer):
    def render_simple_page(self, title: str, content: str) -> str:
        return f'<page><title>{title}</title><content>{content}</content></page>'

    def render_product_page(self, product: Product) -> str:
        return (
            f'<product>'
            f'<id>{product.product_id}</id>'
            f'<name>{product.name}</name>'
            f'<description>{product.description}</description>'
            f'<image>{product.image}</image>'
            f'</product>'
        )


if __name__ == '__main__':
    html_renderer = HTMLRenderer()
    json_renderer = JsonRenderer()
    xml_renderer = XmlRenderer()

    simple_page = SimplePage('Welcome', 'This is a simple page.', html_renderer)
    product = Product(1, 'Widget', 'A useful widget.', 'http://example.com/widget.png')
    product_page = ProductPage(product, json_renderer)

    print('HTML Simple Page:')
    print(simple_page.render())

    print('\nJSON Product Page:')
    print(product_page.render())

    product_page.renderer = xml_renderer
    print('\nXML Product Page:')
    print(product_page.render())
