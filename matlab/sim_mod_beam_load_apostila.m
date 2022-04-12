% PROCEDIMENTO PARA ANALISE ESTRUTURAL DE UMA VIGA
% Desenvolvido por Antonio Vinicius G. Campos, 03/04/2020
clc,clear, close all
% propriedades geometricas da viga
l=1;
a1=l/3;
a2=(2*l)/3;
q0=1; % magnitude do carregamento
dx = 0.01;
x=0:dx:l; %dominio estrutural
% inicializacao de vetores
Vy = zeros(1,size(x,2)); 
Mz = zeros(1,size(x,2)); 
% computacao dos valor dentro do dominio
for i=1:size(x,2)
    if x(i)<a1 && x(i)<a2
        Vy(i)=(1/6)*q0*l;
        Mz(i)=(1/6)*q0*l*x(i);
    elseif x(i)<a2
        Vy(i)=-q0*(x(i)-l/3)+(1/6)*q0*l;
        Mz(i)=-(q0/2)*((x(i)-l/3)^2) +(1/6)*q0*l*x(i);
    else
        Vy(i)=-q0*(x(i)-l/3) + q0*(x(i)-(2*l)/3) + (1/6)*q0*l;
        Mz(i)=-(q0/2)*((x(i)-l/3)^2) + (q0/2)*(x(i)-((2*l)/3))^2 + (1/6)*q0*l*x(i);
    end
end
% pos-processamento
figure()
subplot(2,1,1)
plot(x,Vy)
title('Vy(x)')
grid on
subplot(2,1,2)
plot(x,Mz)
title('Mz(x)')
grid on
