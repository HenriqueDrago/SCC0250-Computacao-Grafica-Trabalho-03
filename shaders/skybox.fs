#version 330 core

varying vec3 out_texture;
uniform samplerCube imagem_cube;

void main(){
    vec4 texture = textureCube(imagem_cube, out_texture);
    gl_FragColor = texture;
}