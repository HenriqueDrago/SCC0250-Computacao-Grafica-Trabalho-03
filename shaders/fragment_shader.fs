#version 330 core

#define MAX_LIGHTS 10

// Use two arrays for the positions and colors
uniform vec3 lightPositions[MAX_LIGHTS];
uniform vec3 lightColors[MAX_LIGHTS];
uniform int numLights;

// parametros da iluminacao
uniform float ka; // coeficiente de reflexao ambiente
uniform float kd; // coeficiente de reflexao difusa
uniform float ks; // coeficiente de reflexao especular
uniform float ns; // expoente de reflexao especular

uniform vec3 viewPos; // define coordenadas com a posicao da camera/observador
uniform vec3 colorAmbience; // define cor ambiente

// parametros recebidos do vertex shader
varying vec2 out_texture; // recebido do vertex shader
varying vec3 out_normal; // recebido do vertex shader
varying vec3 out_fragPos; // recebido do vertex shader
uniform sampler2D samplerTexture;

uniform int lightAmbient[MAX_LIGHTS];
uniform int isBoth;

void main(){
	// Pega a textura e descarta o pixel se for transparente
	vec4 textureColor = texture2D(samplerTexture, out_texture);
	if(textureColor.a < 0.01) {
        discard;
    }

	vec3 norm = normalize(out_normal);
    if (!gl_FrontFacing) {
        norm = -norm;
    }
    
    vec3 viewDir = normalize(viewPos - out_fragPos);
    
    vec3 ambient = ka * colorAmbience; 
    vec3 totalDiffuse = vec3(0.0);
    vec3 totalSpecular = vec3(0.0);

	for(int i = 0; i < MAX_LIGHTS; i++) {
        if(i >= numLights) break; 

        if(isBoth == 1 && lightAmbient[i] == 1 && gl_FrontFacing) {
            continue; // Luz interna é bloqueada se a câmera estiver vendo a face pela frente
        }

        float dist = length(lightPositions[i] - out_fragPos);
        float att = 1.0 / (dist * dist + 1.0);

        // --- Diffuse ---
        vec3 lightDir = normalize(lightPositions[i] - out_fragPos);
        float diff = max(dot(norm, lightDir), 0.0);
        totalDiffuse += kd * diff * lightColors[i] * att;

        // --- Specular ---
        vec3 reflectDir = normalize(reflect(-lightDir, norm));
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), ns);
        totalSpecular += ks * spec * lightColors[i] * att;
    }

    vec3 finalLighting = ambient + totalDiffuse + totalSpecular;
	
	gl_FragColor = vec4(finalLighting, 1.0) * textureColor;
}