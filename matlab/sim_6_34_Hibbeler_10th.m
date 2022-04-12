clc,clear, close all
l=3;
dx = 0.001;
x=0:dx:l; %dominio estrutural

Vy = -2*ones(1,size(x,2));
Mz = -3.*(x-1.5).^0.*(x>=1.5)-2.*x+9;

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