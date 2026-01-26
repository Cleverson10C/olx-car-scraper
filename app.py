from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração básica
url = 'https://www.olx.com.br/autos-e-pecas/estado-pr/regiao-de-curitiba-e-paranagua'
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print('🚗 Acessando OLX...')
    driver.get(url)
    time.sleep(5)
    
    print('📝 Extraindo dados...')
    
    # Busca todos os títulos e preços
    titulos = driver.find_elements(By.TAG_NAME, 'h2')
    precos = driver.find_elements(By.TAG_NAME, 'h3')
    
    # Filtra apenas elementos de anúncios
    produtos = []
    valores = []
    
    for titulo in titulos:
        classe = titulo.get_attribute('class') or ''
        if 'adcard' in classe.lower() and titulo.text.strip():
            produtos.append(titulo.text.strip())
    
    for preco in precos:
        classe = preco.get_attribute('class') or ''
        texto = preco.text.strip()
        if 'adcard' in classe.lower() and 'R$' in texto:
            valores.append(texto)
    
    print(f'✅ Encontrados: {len(produtos)} produtos e {len(valores)} preços')
    
    # Salva no XLSX
    with open('olx_carros.csv', 'w', encoding='utf-8') as f:
        f.write('Produto,Preço\n')
        
        total = min(len(produtos), len(valores))
        for i in range(total):
            f.write(f'"{produtos[i]}","{valores[i]}"\n')
            print(f'{i+1}. {produtos[i][:40]}... | {valores[i]}')
    
    print(f'🎉 {total} produtos salvos em olx_carros.csv!')

except Exception as e:
    print(f'❌ Erro: {e}')

finally:
    input('Pressione Enter para fechar...')
    driver.quit()