<h1 align="center">
  Unipetros 🎓
</h1>

<div align="center">
   <a href="https://github.com/JohnPetros">
      <img alt="Made by JohnPetros" src="https://img.shields.io/badge/made%20by-JohnPetros-blueviolet">
   </a>
   <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/JohnPetros/unipetros">
   <a href="https://github.com/JohnPetros/unipetros/commits/main">
      <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/JohnPetros/unipetros">
   </a>
  </a>
   </a>
   <a href="https://github.com/JohnPetros/unipetros/blob/main/LICENSE.md">
      <img alt="GitHub License" src="https://img.shields.io/github/license/JohnPetros/unipetros">
   </a>
    <img alt="Stargazers" src="https://img.shields.io/github/stars/JohnPetros/unipetros?style=social">
</div>
<br>

## 🖥️ Sobre o Projeto

**Unipetros** é um **site web** para um universidade fictícia do mesmo nome.

A aplicação possui duas sessões, uma voltada para a apresetação e descrição da universidade e outra para administrar dados pertinentes a uma instiuição de ensino, como cursos, dicisplinas, professores e alunos.

O objetivo ao realizar esse projeto foi aprender de forma avançanda o desensolvimento de aplicações web utilizando [Flask](https://flask.palletsprojects.com/en/3.0.x/), um framework [Python](https://www.python.org/), bem como trabalhar com [Docker containers](https://www.docker.com/resources/what-container/) personalizados utilizando [Docker hub](https://www.docker.com/) durante a disciplina de Sistemas Operacionais e Redes na [FATEC São José dos Santos](https://fatecsjc-prd.azurewebsites.net/).


### ⏹️ Demonstração

<table align="center">
  <tr>
    <td align="center" width="700">
    <span>Página da Urna funcionando<br/></span>
    <img alt="Home page" src=".github/unipetros-funcionando.gif" alt="Demonstração da urna funcionando" />
    </td>
  </tr>
</table>

---

## ✨ Funcionalidades

### Landing Page

- [x] A página inicial deve possuir estilo landing page para captar a atenção do usuário. 
- [x] 

  
#### Seleção de SKU (Tipo de um produto)
- Deve ser possível selecionar um único SKU de um produto antes de adicioná-lo ao carrinho
-  A seleção do SKU deve ser com base nas variações disponíveis para o produto. Ex: Se o usuário escolher Material: Inox e Tamanho: Médio, seleciona o SKU que atende essas características
- Caso o produto não tenha variação, o SKU é o próprio produto em si.

#### Filtragem de produtos

- [x] Deve ser possível filtrar produtos por:
  - nome
  - categoria
    - o filtro deve conter apenas uma categoria
  - marca
    - o filtro pode conter mais de uma marca
- [x] Deve ser possível filtrar utilizando de forma simuntânea os filtros listado acima
- [x] Deve ser possível pesquisar um produto pelo nome em mais de uma tela

#### Ordenação de produtos

- [x] Deve ser possível ordenar produtos por ordem alfabética, seja o inverso (Z-A) ou não (A-Z)


#### Cálculo de Frete

- [x] Deve ser possível calcular cusot de frete de um produto com base no CEP do usuário
- [x] Deve ser possível o usuário calcular o frete antes de ir para o checkout
- [x] Deve ser exibido para o usuário uma tabela de preço para cada transportadora especifica
- [x] Deve ser exibido para o usuário uma tabela de preço para cada transportadora especifica

#### Carrinho

- [x] Deve haver uma tela própria para o carrinho
- [x] Deve ser possível inserir um produto no carrinho
- [x] Deve ser possível alterar a quantidade do produto que está no carrinho
- [x] Deve ser possível remover um produto no carrinho
- [x] Deve ser possível remover todos os produtos do carrinho de uma vez
- [x] Não deve ser posível inserir produtos repetidos no carrinho
- [x] Não deve ser possível alterar a quantidade maior que o estoque permitido
- [x] Não deve ser possível alterar a quantidade menor para menor que 1
- [x] Todos os produtos do carrinho devem ser removidos se o usuário for redirecionado para o checkout
- [x] Os produtos do carrinho devem ser persistidos de modo que o usuário possa acessá-los novamente mesmo que ele feche e abre o aplicativo novamente  
- [x] O produto no carrinho deve dizer a respeito a um do seus SKU, que por sua vez são definidos pelas variações escolhidas pelo usuário. Ex.: variações: material: Inox e tamanho: Médio definem o SKU que contém essas características 

#### Capturador de leads

- [x] Deve ser possível cadastrar o `e-mail` do cliente/lead na tela `Home`
- [x] Não deve ser possível inserir o `e-mail` de um cliente/lead já cadastrado

#### Contato

- [x] Deve ser possível o usuário entrar em contato com alguém da `unipetros` via whatsapp ou e-mail

#### Listagem de pedidos

- [x] Deve ser possível listar todos os pedidos do usuário
- [x] A lista de pedidos deve ser com base no CPF ou CNPJ utilizado para fazer o pedido
- [x] Cada pedido deve exibir:
  - número,
  - status (pago, aguardando pagamento ou cancelado),
  - produtos, onde cada produto exibe:
    - nome
  - total de desconto,
  - total a pagar (considerando o desconto)
  - tipo de pagamento (cartão de crédito, pix ou boleto), sendo que:
    - Se for por pix, permitir o usuário acessar o QR Code gerado pelo pedido
    - Se for por boleto, permitir o usuário acessar o pdf do boleto gerado pelo pedido
- [] Deve ser possível o usuário arquivar o pedido de forma que não seja possível mais acessá-lo no aplicativo

### ☑️ Requisitos não funcionais

#### Informações relevantes

- [x] Deve ser exibido ao usuário informações sobre a empresa unipetros, termos e condições, política de devolução de produto

#### Listagem paginada de produtos

- [x] Todos os produtos não devem ser carregados todos de uma vez mas conforme o usuário desce a tela para visualizar mais produtos

#### Banners

- [x] Devem ser exibidos banners que capturem a atenção do cliente

#### Coleções

- [x] Devem ser exibidos coleções de produtos que compartilham o mesmo tema ou categoria

#### Botão de carrinho

- [x] Deve ser possível adicionar um produto ao carrinho sem o usuário precisar ver a tela de detalhes desse produto
- [x] O botão de carrinho deve seguir as regras da funcionalidade de carrinho

---

## ⚙️ Arquitetura

## 🛠️ Tecnologias, ferramentas e serviços externos

Este projeto foi desenvolvido usando as seguintes tecnologias:

✔️ **[Python](https://www.python.org/)** para programar o backend

✔️ **[Flask](https://flask.palletsprojects.com/en/3.0.x/)** Para servir como framework para construir o servidor web, fazer validação dos formulários e gerenciar a autenticação do usuário

✔️ **[MySQL](https://www.mysql.com/)** para ser banco de dados

✔️ **[HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)** Para fazer a marcação das páginas do site

✔️ **[CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)** - para estilizar os elementos do site

✔️ **[JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)** - Para adicionar interatividade nos elementos do site

✔️ **[ApexCharts.js](https://apexcharts.com/)** - Para renderizar gráficos

✔️ **[Docker](https://www.docker.com/)** - para criar e gerenciar os containers da aplicação

> Para mais detalhes acerca das dependências do projeto, como versões específicas, veja o arquivo [package.json](https://github.com/JohnPetros/unipetros/blob/main/package.json)

---

## 🚀 Como rodar a aplicação?

### 🔧 Pré-requisitos

Antes de baixar o projeto você necessecitará ter instalado na sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com/) para manilupar repostitórios Git
- [Docker](https://docs.docker.com/get-docker/) para manipular Docker containers

> Além disto é bom ter um editor para trabalhar com o código, como o [VSCode](https://code.visualstudio.com/)

> Além disto é crucial configurar as variáveis de ambiente em um arquivo chamado `.env` antes de executar a aplicação. veja o arquivo [.env.example](https://github.com/JohnPetros/unipetros/blob/main/.env.example) para ver quais variáveis devem ser configuradas

### 📟 Rodando a aplicação

```bash

# Clone este repositório
$ git clone https://github.com/JohnPetros/unipetros.git

# Acesse a pasta do projeto
$ cd unipetros

# Rode o container da aplicação
$ docker compose up

```

> Você irá precisar um emulador de android (se não estiver em um ambiente Mac) para ver o aplicativo funcionando. Porém você pode gerar o expo development build do projecto e executá-lo tanto no emulador quanto no seu dispositivo físico.

```bash
# Instale o expo development client
$ npx expo install expo-dev-client

# Gere a build do projeto
$ eas build --profile development --platform android
```

> Veja a [documentação](https://docs.expo.dev/develop/development-builds/create-a-build/) para mais detalhes a respeito do expo development build

### 🧪 Rodando os testes

```bash
# Execute os testes
$ npm run test
# ou
$ yarn test
```

###

---

## 🚚 Deploy

O deploy dessa aplicação foi realizada usando a plataforma da **[Render](https://dashboard.render.com/)**, o que implica dizer que você pode acessar aplicação funcionando acessando esse **[link](https://unipetros-app.onrender.com/)**.

---

## 💪 Como contribuir

```bash

# Fork este repositório
$ git clone https://github.com/JohnPetros/unipetros.git

# Cria uma branch com a sua feature
$ git checkout -b minha-feature

# Commit suas mudanças:
$ git commit -m 'feat: Minha feature'

# Push sua branch:
$ git push origin minha-feature

```

> Você deve substituir 'minha-feature' pelo nome da feature que você está adicionando

> Você também pode abrir um [nova issue](https://github.com/JohnPetros/unipetros/issues) a respeito de algum problema, dúvida ou sugestão para o projeto. Ficarei feliz em poder ajudar, assim como melhorar este projeto

---

## 🎨 Layout

O design do projeto pode ser acessada nesse [link](https://www.figma.com/file/8DRd8OlhogKoCcofQD1QX4/unipetros-Industrial?type=design&t=pbdOp6tdnmj2kTmc-6).

---

## 📝 Licença

Esta aplicação está sob licença do MIT. Consulte o [Arquivo de licença](LICENSE) para obter mais detalhes sobre.

---

<p align="center">
  Feito com 💜 por John Petros 👋🏻
</p>
