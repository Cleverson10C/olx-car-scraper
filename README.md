# 🚗 Web Scraping OLX - Extração de Anúncios de Veículos

Projeto de web scraping para extrair dados de anúncios de veículos do site OLX utilizando Selenium e Python.

## 📋 Descrição

Este projeto automatiza a extração de informações de anúncios de carros na região de Curitiba e Paranaguá no site OLX. Os dados extraídos incluem título do anúncio e preço, sendo salvos em formato CSV para análise posterior.

## ✨ Funcionalidades

- ✅ Extração automática de anúncios do OLX
- ✅ Coleta de títulos e preços de veículos
- ✅ Filtro inteligente de elementos da página
- ✅ Exportação de dados em formato CSV
- ✅ Feedback visual do progresso da extração
- ✅ Tratamento de erros

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Selenium** - Automação de navegador
- **ChromeDriver** - Driver para Google Chrome

## 📦 Pré-requisitos

Antes de executar o projeto, você precisa ter instalado:

- Python 3.7 ou superior
- Google Chrome
- pip (gerenciador de pacotes do Python)

## 🚀 Instalação

### 1. Clone o repositório ou faça download dos arquivos

```bash
cd "Extracao olx web"
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install selenium
```

### 5. Instale o ChromeDriver

O Selenium precisa do ChromeDriver para controlar o Chrome. Você pode:

**Opção 1 - Instalação automática (recomendado):**
```bash
pip install webdriver-manager
```

**Opção 2 - Download manual:**
- Baixe em: https://chromedriver.chromium.org/
- Coloque o executável no PATH do sistema

## 💻 Como Usar

### Execução Básica

```bash
python app.py
```

### O que o script faz:

1. 🌐 Abre o navegador Chrome
2. 🔍 Acessa a página de anúncios do OLX
3. ⏳ Aguarda o carregamento da página (5 segundos)
4. 📝 Extrai títulos e preços dos anúncios
5. 🔄 Filtra apenas elementos válidos
6. 💾 Salva os dados em `olx_carros.csv`
7. ✅ Exibe resumo da extração

### Resultado

O script gera um arquivo `olx_carros.csv` com o seguinte formato:

```csv
Produto,Preço
"CHEVROLET ONIX 1.0 TURBO FLEX PLUS PREMIER AUTOMÁTICO","R$ 78.000"
"TOYOTA COROLLA 2.0 XEI FLEX AUTOMÁTICO","R$ 125.000"
...
```

## 📂 Estrutura do Projeto

```
Extracao olx web/
│
├── .venv/              # Ambiente virtual (ignorado no git)
├── app.py              # Script principal de extração
├── olx_carros.csv      # Dados extraídos (gerado após execução)
└── README.md           # Este arquivo
```

## 🎯 Funcionalidades do Código

### Extração de Dados

```python
# Busca todos os títulos (h2)
titulos = driver.find_elements(By.TAG_NAME, 'h2')

# Busca todos os preços (h3)
precos = driver.find_elements(By.TAG_NAME, 'h3')
```

### Filtro Inteligente

```python
# Filtra apenas elementos com classe 'adcard'
if 'adcard' in classe.lower() and titulo.text.strip():
    produtos.append(titulo.text.strip())
```

### Salvamento em CSV

```python
with open('olx_carros.csv', 'w', encoding='utf-8') as f:
    f.write('Produto,Preço\n')
    for i in range(total):
        f.write(f'"{produtos[i]}","{valores[i]}"\n')
```

## ⚙️ Configurações

### Modificar a URL de busca

Edite a variável `url` no arquivo `app.py`:

```python
url = 'https://www.olx.com.br/autos-e-pecas/estado-pr/regiao-de-curitiba-e-paranagua'
```

### Ajustar tempo de espera

Modifique o valor de `time.sleep()`:

```python
time.sleep(5)  # Segundos de espera
```

## 🐛 Solução de Problemas

### Erro: "chromedriver not found"
- Instale o ChromeDriver ou use `webdriver-manager`

### Erro: "no such element"
- A página pode ter mudado de estrutura
- Aumente o tempo de espera (`time.sleep`)

### CSV vazio
- Verifique se a página carregou completamente
- O site pode estar bloqueando automação

### Encoding no CSV
- O arquivo usa UTF-8 por padrão
- Para Excel, pode ser necessário abrir como "UTF-8"

## ⚠️ Considerações Importantes

### Ética e Legalidade

- ⚖️ Respeite os **Termos de Serviço** do OLX
- 🤖 Verifique o arquivo `robots.txt` do site
- ⏱️ Não faça requisições excessivas (use delays)
- 📊 Use os dados apenas para fins legais e éticos

### Limitações

- 📄 Extrai apenas a **primeira página** de resultados
- 🔄 Não implementa paginação automática
- 🚫 Pode ser bloqueado por anti-bot do site
- ⏰ Depende da estrutura HTML do OLX

## 🔧 Melhorias Futuras

- [ ] Implementar paginação automática
- [ ] Adicionar extração de mais campos (localização, km, ano)
- [ ] Criar sistema de retry em caso de falha
- [ ] Implementar logging detalhado
- [ ] Adicionar interface gráfica (GUI)
- [ ] Suporte para outras regiões
- [ ] Exportar para outros formatos (JSON, Excel)
- [ ] Implementar anti-detecção mais robusto

## 📚 Recursos Adicionais

### Documentação Oficial

- [Selenium Python](https://selenium-python.readthedocs.io/)
- [Python CSV](https://docs.python.org/3/library/csv.html)

### Tutoriais Recomendados

- Web Scraping com Python
- Selenium para iniciantes
- Ética em Web Scraping

## 📝 Licença

Este projeto é disponibilizado para fins educacionais. Use de forma responsável e ética.

## 👨‍💻 Autor

Desenvolvido como projeto educacional de web scraping.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📞 Suporte

Se tiver dúvidas ou problemas:

1. Verifique a seção de Solução de Problemas
2. Consulte a documentação do Selenium
3. Verifique se o ChromeDriver está atualizado

---

**⚠️ Aviso Legal:** Este projeto é apenas para fins educacionais. O uso de web scraping deve respeitar os termos de serviço dos sites e as leis aplicáveis. O autor não se responsabiliza pelo uso indevido desta ferramenta.

**Desenvolvido com ❤️ usando Python e Selenium**