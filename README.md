1. Explique a diferença entre Selenium IDE e Selenium WebDriver.

O selenium IDE é como um gravador de testes para resgistrar as interações em um navegador web.
Já o selenium WebDriver é uma ferramenta usada juntamente com programação para criar testes.

2. Quais são os principais tipos de localizadores (locators) usados no Selenium WebDriver para encontrar elementos na página? Explique dois deles. (2 pontos)
O “ID” é um tipo de localizador simples que localiza itens em uma página web.
Outro bastante usado é o “XPATH” que permite uma busca melhorada de quaisquer elementos na estrutura da página web.

3. O que é um WebElement no Selenium? Dê um exemplo de como interagir com um WebElement usando Python. (2 pontos)
É uma forma que o selenium usa para interagir com itens da página que está sendo testada. Exemplo: “nome = driver.find_element(By.ID, "nome") nome.send_keys("Seu Nome") ” => neste código  a função send.keys é usada para preencher os campos de texto.

4. No Selenium WebDriver, o que acontece se você tentar interagir com um elemento que ainda não está visível ou carregado na página? Qual comando você usaria para resolver isso? (2 pontos)
A automação para e reporta que ocorreu uma restrição por conta do erro. Uma forma seria utilizar o comando: WebDriverWait para determinar uma condição para que a automação prossiga.

5. Cite duas limitações do Selenium IDE que podem levar à escolha do Selenium WebDriver em projetos maiores. (2 pontos)
O selenium IDE não tem uma boa integração com múltiplas ferramentas de desenvolvimento, portanto pode ser um atraso para projetos mais complexos que utilizam abordagens variadas. Outro ponto é a falta de estrutura para organizar os testes de forma ordenada, o que em projetos grandes pode ser um problema por conta da demanda alta de testes(gravações) que serão necessárias.
