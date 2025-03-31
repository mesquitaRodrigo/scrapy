import scrapy
import json  # Import necessário para carregar JSON

class OlxHouses(scrapy.Spider):
    name = 'olx'

    def start_requests(self):
        for page in range(1, 101):
            yield scrapy.Request(
               url=f'https://www.olx.com.br/imoveis/estado-rj?o={page}',
                #headers={'User-Agent': 'Mozilla/5.0'}  # Adicionando User-Agent para evitar bloqueios
            )

    def parse(self, response, **kwargs):
        script_content = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()

        if script_content:
            try:
                data = json.loads(script_content)  # Convertendo string JSON para dicionário
                houses = data.get('props', {}).get('pageProps', {}).get('ads', [])

                for house in houses:
                    yield {
                        'title': house.get('title'),
                        'price': house.get('price'),
                        'locationDetails': house.get('locationDetails'),
                        'category' : house.get('category')
                    }
            except json.JSONDecodeError:
                self.logger.error("Erro ao decodificar JSON da página.")

