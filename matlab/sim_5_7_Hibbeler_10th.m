% PROCEDIMENTO PARA ANALISE ESTRUTURAL DE UMA VIGA
% Desenvolvido por Antonio Vinicius G. Campos, 03/04/2020
clc,clear, close all
% propriedades geometricas da viga
l=0.2;
dx = 0.0001;
x=0:dx:l; %dominio estrutural
% inicializacao de vetores
% Mx = zeros(1,size(x,2)); 
% the = zeros(1,size(x,2)); 
% computacao dos valor dentro do dominio

Mx=-300*(x-0.05).^0.*(x>=0.05)-600*(x-0.1).^0.*(x>=0.1)+2000*(x-0.15).^0.*(x>=0.15)-200;
the=-300*(x-0.05).^1.*(x>=0.05)-600*(x-0.1).^1.*(x>=0.1)+2000*(x-0.15).^1.*(x>=0.15)-200.*x;

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
plot(x,Mx)
title('Nx(x)')
grid on
subplot(2,1,2)
plot(x,the)
title('u(x)')
grid on
