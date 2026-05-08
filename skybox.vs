#version 330 core

attribute vec3 position;
varying vec3 out_texture;

uniform mat4 view;
uniform mat4 projection;        

void main(){
    // For a cubemap, these are the same
    out_texture = position;
    
    // Calculate the position (no model)
    vec4 pos = projection * view * vec4(position, 1.0);
    
    // z = w so the depth is always the highest
    gl_Position = pos.xyww;
}