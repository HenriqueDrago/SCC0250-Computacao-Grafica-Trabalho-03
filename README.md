# Projeto 3 - Computação Gráfica (SCC0250): "Iluminação em Casa no Meio do Nada"

## Descrição

Este projeto expande a cena desenvolvida no Projeto 2, incorporando modelos de iluminação ambiente, difusa e especular. O cenário é dividido entre ambientes interno e externo, com fontes de luz independentes que afetam apenas seus respectivos escopos. A implementação atende a todos os requisitos propostos utilizando exclusivamente o pipeline moderno do OpenGL.

## Integrantes

* Henrique Drago, NUSP: 14675441
* Henrique Yukio Sekido, NUSP: 14614564

## Como Executar

1. Instale as dependências: `pip install glfw PyOpenGL pyglm numpy pillow`.
2. Execute o arquivo `Trabalho_3.ipynb` em um ambiente Jupyter ou VSCode.

---

## Controles e Interação

### 1. Controles Gerais e de Câmera

Estes comandos controlam o estado da janela, modos globais de renderização e a navegação da câmera pelo cenário.

* **Mouse**: Controla a direção do visualizador (olhar ao redor).
* **H**: Move a câmera para **frente**.
* **N**: Move a câmera para **trás**.
* **B**: Move a câmera para a **esquerda**.
* **M**: Move a câmera para a **direita**.
* **Shift (Segurar)**: Reduz a velocidade base de movimento da câmera para ajustes finos.
* **Esc**: Fecha a janela do programa.
* **F**: Alterna entre o modo tela cheia (maximizado) e o modo janela padrão.
* **P**: Alterna o Modo Polígono entre preenchido e malha de linhas (**Wireframe**).
* **L**: Alterna a visibilidade dos cubos indicadores que representam as posições das fontes de luz.
* **Ctrl + R**: Reseta completamente a cena (recarrega os arquivos JSON originais de objetos e luzes, reinicia as velocidades/acelerações do ônibus e reativa a iluminação ambiente).
* **K**: Alterna o estado do **Modo Restrito** (`restrictMode`), usado para alternar entre a demonstração dos requisitos e a edição livre.

---

### 2. Modo Restrito (`restrictMode = True`)

O programa inicia neste modo por padrão. Ele é focado nos requisitos obrigatórios de iluminação e controle global de reflexão da cena.

#### Controle das Luzes e Translação

* **Seta para Cima**: Acelera o ônibus (objeto com translação que contém a fonte de luz externa) para a **frente**.
* **Seta para Baixo**: Acelera o ônibus para **trás**.
* **1**: Interruptor para ligar/desligar os faróis do ônibus (Luz Externa).
* **2**: Interruptor para ligar/desligar a luz interna 1 (Vela).
* **3**: Interruptor para ligar/desligar a luz interna 2 (Gnomo).
* **4**: Interruptor para ligar/desligar a iluminação ambiente global do shader.

#### Parâmetros de Reflexão (Propriedades de Iluminação)

* **I / O**: Incrementa / Decrementa a constante de iluminação ambiente global ($K_a$).
* **U / J**: Incrementa / Decrementa a reflexão difusa global ($K_d$).
* **T / G**: Incrementa / Decrementa a reflexão especular global ($K_s$).
* **E / D**: Incrementa / Decrementa o multiplicador do brilho especular ($N_s$).

---

### 3. Modo Livre / Customização (`restrictMode = False`)

Ativado ao pressionar a tecla **K**. Este modo desativa as restrições e permite a edição e montagem manual das luzes e dos modelos 3D do cenário.

Para transitar entre a edição de luzes e a edição de objetos, utiliza-se o atalho **Shift + L**.

#### A. Submodo de Edição de Luzes (`lightMode = True`)

Ativado alternando com **Shift + L** dentro do Modo Livre. Permite alterar a posição espacial e o estado das fontes de luz.

* **Y**: Alterna e seleciona qual fonte de luz da lista será manipulada.
* **Seta para Esquerda / Seta para Direita**: Translada a luz selecionada ao longo do **Eixo X**.
* **Seta para Baixo / Seta para Cima**: Translada a luz selecionada ao longo do **Eixo Y**.
* **Z / X**: Translada a luz selecionada ao longo do **Eixo Z**.
* **A**: Liga/desliga a luz selecionada.

#### B. Submodo de Edição de Objetos (`lightMode = False`)

Ativado alternando com **Shift + L** dentro do Modo Livre. Permite aplicar as transformações geométricas e configurações individuais nos modelos 3D.

* **Y**: Alterna e seleciona qual objeto da cena será manipulado.
* **V**: Alterna a visibilidade (ligado/desligado) do objeto selecionado na renderização.
* **C**: Alterna o modo de escala entre **Escala Uniforme** (afeta X, Y e Z simultaneamente) e **Escala no Eixo Ativo**.
* **Q**: Altera o **Eixo Ativo** de manipulação (cicla sequencialmente entre os eixos X, Y e Z) para rotações e escalas não-uniformes.
* **A / D**: Rotaciona o objeto selecionado em torno do Eixo Ativo.
* **W / S**: Incrementa / Decrementa a escala do objeto (ajusta todos os eixos se a escala uniforme estiver ativa, ou apenas o Eixo Ativo caso esteja desativada).
* **Seta para Esquerda / Seta para Direita**: Translada o objeto selecionado ao longo do **Eixo X**.
* **Seta para Baixo / Seta para Cima**: Translada o objeto selecionado ao longo do **Eixo Y**.
* **Z / X**: Translada o objeto selecionado ao longo do **Eixo Z**.