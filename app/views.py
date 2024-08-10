from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def atletas(request):
    atletas = [
        {"nome": "Caíque", "idade": "17", "posicao": "Goleiro", "nascimento": "Natal - RN", "foto": "CAIQUE.webp", "descricao": "Clubes: Categorias de base do ABC."},
        {"nome": "Vitor Marinho", "idade": "22", "posicao": "Lateral", "nascimento": "Porto Real - RJ", "foto": "VITOR_MARINHO.webp", "descricao": "Clubes: Resende/RJ (2018-2020), Botafogo/RJ (2020-2023) e Resende/RJ (2023)."},
        {"nome": "Bebeto", "idade": "17", "posicao": "Zagueiro", "nascimento": "Natal - RN", "foto": "BEBETO.webp", "descricao": "Clubes: Categorias de base do ABC."},
        {"nome": "Dudu", "idade": "18", "posicao": "Volante", "nascimento": "Natal - RN", "foto": "DUDU.webp", "descricao": "Clubes: Categorias de base do ABC."},
        {"nome": "Luccas Gabriel", "idade": "20", "posicao": "Atacante", "nascimento": "Natal - RN", "foto": "LUCAS.webp", "descricao": "Clubes: Categorias de base do ABC, ABC (2023), Portuguesa Santista/SP (2023) e ABC (2024)."},
        {"nome": "Mike", "idade": "18", "posicao": "Meia", "nascimento": "João Pessoa - PB", "foto": "MIKE.webp", "descricao": "Clubes: Categorias de base do ABC."},
        {"nome": "Oziel", "idade": "17", "posicao": "Volante", "nascimento": "São Pedro - RN", "foto": "OZIEL.webp", "descricao": "Clubes: Categorias de base do ABC."},
        {"nome": "Richardson", "idade": "31", "posicao": "Zagueiro", "nascimento": "Natal - RN", "foto": "RICHAR.webp", "descricao": "Clubes: Desportivo Brasil/SP (2010-2011), Grêmio/RS (2011-2012), Santa Cruz/RN (2013), Grêmio Anápolis/GO (2014), Dom Bosco/MT (2015), Santa Cruz de Natal/RN (2015), América/RN (2016-2018), Alecrim/RN (2018), Campinense/PB (2019), ABC (2019-2020) e Ferroviário/CE (2020-2021), ABC (2022-2023) e Náutico/PE (2023)."},
        {"nome": "Ruan", "idade": "30", "posicao": "Atacante", "nascimento": "Natal - RN", "foto": "RUAN.webp", "descricao": "Clubes: Sport/PE (2009-2011), Grêmio/RS (2011-2012), Sport/PE (2012-2013), Fortaleza/CE (2013), Internacional/RS (2014), Paysandu/PA (2014), Goiás/GO (2015), Ituano/SP (2016), Paysandu/PA (2016), Botafogo/PB (2016), Vila Nova/GO (2017), CRB/AL (2018), Remo/PA (2018), Caxias/RS (2019), São Bento/SP (2020-2021), Atibaia/SP (2021-2022), Amazonas/AM (2022), Laguna/RN (2022) e Amazonas/AM (2023)."},
        {"nome": "Sammuel ", "idade": "22", "posicao": "Meia", "nascimento": "Fortaleza - CE", "foto": "SAMUEL.webp", "descricao": "Clubes: Fortaleza/CE (2017-2020), Guarany de Sobral/CE (2020), Fortaleza/CE (2020-2023) e Atlético/GO (2023)."},
        {"nome": "Walfrido", "idade": "29", "posicao": "Volante", "nascimento": "Fortaleza - CE", "foto": "WALFRIDO.webp", "descricao": "Clubes: Fortaleza/CE (2012-2014), Ituano/SP (2015), Criciúma/SC (2015), Sampaio Corrêa/MA (2016), CSA/AL (2016), Ituano/SP (2017), Botafogo/SP (2017-2018), Bragantino/SP (2018), XV de Piracicaba/SP (2019), Guarany de Sobral/CE (2019), Anápolis/GO (2020), XV de Piracicaba/SP (2020), Portuguesa/SP (2020-2021), Oeste/SP (2022) e ABC (Desde 2022)."},
        {"nome": "Wallyson", "idade": "35", "posicao": "Atacante", "nascimento": "Macaíba - RN", "foto": "WALLYSON.webp", "descricao": "Clubes: ABC (2007), Atlético/PR (2008-2010), Cruzeiro/MG (2010-2012), São Paulo/SP (2013), Bahia/BA (2013), Botafogo/RJ (2014), Coritiba/PR (2015), Santa Cruz/PE (2016), Vila Nova/GO (2017), ABC (2018), Vitória/BA (2018), Maldonado/Uruguai (2019) e ABC (Desde 2019)."},
        {"nome": "Wesley Santos", "idade": "31", "posicao": "Zagueiro", "nascimento": "Paranaguá - PR", "foto": "WESLEY.webp", "descricao": "Clubes: Coritiba/PR (2010-2011), Rio Branco/PR (2012), Marília/SP (2013), Parnahyba/PI (2014), Hercílio Luz/SC (2014), VOCEM/SP (2014), Foz de Iguaçu/PR (2015), Botafogo/PB (2015), Ypiranga/RS (2016), Maringá/PR (2016), União Beltrão/PR (2016), Global/Filipinas (2017-2018), São Bento/SP (2019), Boa Esporte/MG (2020), Nam Dinh/Vietnã (2020-2021), Camboriú/SC (2022), Caxias/RS (2022), Barra/SC (2023), Maringá/PR (2023) e Paysandu/PA (2023)."},
    ]

    context = {
        "atletas": atletas,
    }
    return render(request, "atletas.html", context)

def sobre(request):
    return render(request, "sobre.html")
