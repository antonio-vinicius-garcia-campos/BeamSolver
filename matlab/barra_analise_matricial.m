% PROCEDIMENTO PARA ANALISE ESTRUTURAL DE UMA BARRA
% Desenvolvido por Antonio Vinicius G. Campos, 30/03/2020
clc,clear, close all
% Discretizacao das propriedades da barra
E=[200E9;200E9;200E9];
a1=0.03^2;
a2=0.02^2;
a3=0.01^2;
A = [a1,a2,a3];
l=1;
f4=2000;
nelm=3; % numero de elementos
ngdls=4; % numero de graus de liberdade
nlivres=[2,3,4]; % lista de graus de liberdade/nos livres
% Matrizes auxiliares
U = zeros(ngdls,1);
F = zeros(ngdls,1);
F(4)=f4;
K = zeros(ngdls,ngdls);
Sigxx = zeros(1,nelm); % Tensao XX
% Montagem da rigidez global
for i=1:nelm
   K(i:i+1,i:i+1)=K(i:i+1,i:i+1)+((A(i)*E(i))/l)*[1,-1;-1,1];
   Sigxx(i) = f4/A(i);
end
% Solucao do problema
U(nlivres)=(K(nlivres,nlivres)^-1)*F(nlivres);
% Pos-processamento
figure()
plot(1000*(0:(3*l/nelm):3*l),(U*1000))
title('Solucao do modelo de barra')
xlabel('Comprimento [mm]')
ylabel('Deslocamento axial [mm]')
grid on
figure()
plot(1000*(0:(3*l/nelm):3*l),[0,Sigxx/(10e6)])
title('Tensao normal xx no modelo de barra')
xlabel('Comprimento [mm]')
ylabel('Tensao [MPa]')
grid on

