% PROCEDIMENTO PARA ANALISE ESTRUTURAL DE UMA BARRA
% Desenvolvido por Antonio Vinicius G. Campos, 25/04/2020
clc,clear, close all
% propriedades geometricas da viga
l=2;
F=1000; % magnitude do carregamento
E=70E9;
A=0.02^2;
dx = 0.01;
x=0:dx:l; %dominio estrutural
% inicializacao de vetores
Nx = zeros(1,size(x,2)); 
ux = zeros(1,size(x,2));
Sigx = zeros(1,size(x,2));
Epsx = zeros(1,size(x,2));
% computacao dos valor dentro do dominio
for i=1:size(x,2)
   ux(i) = (1/(E*A))*(-(F/2)*x(i)^2 + F*l*x(i));
   Nx(i) = -F*x(i)+F*l;
   Sigx(i) = (1/A)*(Nx(i));
   Epsx(i) = (1/(E*A))*(-F*x(i)+F*l);
end
% pos-processamento
figure()
subplot(4,1,1)
plot(x,1000*ux)
ylabel('u(x) [mm]')
grid on
subplot(4,1,2)
plot(x,Nx)
ylabel('Nx(x) [N]')
grid on
subplot(4,1,3)
plot(x,Sigx/10E6)
ylabel('Sig(x) [MPa]')
grid on
subplot(4,1,4)
plot(x,1000*Epsx)
xlabel('L')
ylabel('Eps(x) [mm/mm]')
grid on
