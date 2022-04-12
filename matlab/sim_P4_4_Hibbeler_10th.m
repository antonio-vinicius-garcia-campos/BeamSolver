% PROCEDIMENTO PARA ANALISE ESTRUTURAL DE UMA VIGA
% Desenvolvido por Antonio Vinicius G. Campos, 03/04/2020
clc,clear, close all
% propriedades geometricas da viga
l=2;
dx = 0.001;
x=0:dx:l; %dominio estrutural
% inicializacao de vetores
Nx = zeros(1,size(x,2)); 
u = zeros(1,size(x,2)); 
% computacao dos valor dentro do dominio

Nx=100*(x).^-1 - 800*(x-2).^0.*(x>=2) + 600;
u=50*(x).^2 - 800*(x-2).^1.*(x>=2) + 600.*x;

% for ii=1:size(x,2)
%     if x(ii)<2
%         Nx(ii) = 100*x(ii)+600;
%         u(ii) = 50*x(ii)^2 + 600*x(ii);
%     else
%         Nx(ii) = 100*x(ii) - 800*(x(ii)-2)^0 + 600;
%         u(ii) = 50*x(ii)^2 - 800*(x(ii)-2)^1 + 600*x(ii);
%     end
% end
% pos-processamento
figure()
subplot(2,1,1)
plot(x,Nx)
title('Nx(x)')
grid on
subplot(2,1,2)
plot(x,u)
title('u(x)')
grid on
