# Mapa do Projeto

Projeto de Computacao Grafica em Python/OpenGL para a cena "Iluminacao em Casa no Meio do Nada".

## Pontos de entrada

- `Trabalho_3.ipynb`: notebook principal. Inicializa GLFW/OpenGL, carrega shaders, modelos, texturas, cena, callbacks e loop de renderizacao.
- `shader_s.py`: classe `Shader`, responsavel por ler, compilar e linkar vertex/fragment shaders a partir da pasta `shaders/`.
- `README.md`: instrucoes curtas de instalacao e execucao.
- `remove_entries.py`: script utilitario para editar JSONs de cena. No estado atual referencia tambem `storage/road.json`, `storage/chao.json` e `storage/cubo.json`, que nao aparecem no repositorio.

## Estrutura de dados

- `storage/scene.json`: cena principal, com 24 objetos.
  - Campos recorrentes: `name`, `obj_file`, `texture_file`, `mtl_texture_overrides`, `translacao`, `escala`, `rotacao`, `visible`, `polygon`, `scene_file`, `illum_specs`, `ambient`, `uv_mult_u`, `uv_mult_v`.
  - Ambientes dos objetos: `external`, `internal`, `both` e `none`.
- `storage/light.json`: luzes da cena.
  - Campos: `name`, `pos`, `color`, `active`, `ambient`.
  - Atualmente ha uma luz externa branca e uma luz interna amarela.
- `objetos/`: modelos `.obj`, materiais `.mtl` e texturas usados pela cena.

## Shaders

- `shaders/vertex_shader.vs`: transforma vertices por `projection * view * model`, repassa UV, posicao do fragmento e normal corrigida pela matriz inversa transposta do modelo.
- `shaders/fragment_shader.fs`: faz iluminacao ambiente, difusa e especular para ate `MAX_LIGHTS = 10`, aplica textura 2D e descarta fragmentos quase transparentes.
- `shaders/skybox.vs` e `shaders/skybox.fs`: renderizam cubemap da skybox.

## Funcoes principais no notebook

- Carregamento de assets: `load_model_from_file`, `load_texture_from_file`, `load_obj_and_texture`, `load_mtl`, `load_obj_with_mtl`, `load_cubemap`.
- Persistencia/configuracao: `load_and_merge_scenes`, `load_lights`, `save_lights`, `save_scene`, `add_to_scene`, `add_new_light`.
- Cena e GPU: `carregar_objs`, `object_shader_config`, `light_gpu_config`, `skybox_shader_config`, `desenha_obj`, `desenha_luzes`.
- Interacao: `key_event`, `mouse_callback`, `scroll_callback`, `framebuffer_size_callback`.
- Matrizes: `model`, `view`, `projection`.
- Animacao/regras especificas: `special_object_transform`, principalmente para movimento do onibus e luz associada.

## Controles observados

- `ESC`: fecha a janela.
- `P`: alterna modo poligonal.
- `R`: recarrega/reset da cena a partir dos JSONs.
- `K`: alterna modo restrito.
- `H`, `N`, `B`, `M`: movimentacao da camera.
- Mouse: controla orientacao da camera.
- Scroll: altera FOV/zoom.
- `UP`/`DOWN`: no modo de grupo, controla aceleracao/desaceleracao do onibus.
- `1`, `2`, `3`: alternam luzes especificas.
- `Y`: troca objeto ou luz selecionada, dependendo do modo.
- `V`: alterna visibilidade do objeto selecionado.
- `C`: alterna escala uniforme.
- `Q`: troca eixo de manipulacao.
- `A`/`D`: rotacao.
- `W`/`S`: escala.
- Setas, `Z`, `X`: translacao.

## Observacoes

- O README parece estar salvo com texto UTF-8 sendo exibido como CP1252 em alguns terminais, mas o conteudo e legivel no arquivo.
- `__pycache__/shader_s.cpython-314.pyc` esta modificado no git, provavelmente por execucao local. Nao e fonte do projeto.
- O notebook concentra praticamente toda a logica. Se o projeto crescer, um bom proximo passo seria extrair carregadores, cena, controles e renderizacao para modulos `.py`.
