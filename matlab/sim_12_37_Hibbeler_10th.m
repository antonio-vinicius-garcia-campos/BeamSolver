clc,clear, close all

% dimensoes da secao
h = 100/1000; 
b = 100/1000;
Izz=(b*h^3)/12;
% propriedades do material
E=200E9; % Aco
l=3;
dx = 0.001;
Mo=100;
x=0:dx:l; %dominio estrutural

Vy = 0*ones(1,size(x,2));
Mz = +Mo.*(x-l/3).^0.*(x>=l/3)-Mo*(x-2*l/3).^0.*(x>=2*l/3);
The = +Mo.*(x-l/3).^1.*(x>=l/3)-Mo.*(x-2*l/3).^1.*(x>=2*l/3)-Mo*l/6;
v = +(Mo/2).*(x-l/3).^2.*(x>=l/3)-(Mo/2)*(x-2*l/3).^2.*(x>=2*l/3)-Mo*l/6.*x;

% pos-processamento
figure()
subplot(4,1,1)
plot(1000.*x,Vy)
ylabel('Vy(x) [N]')
title('Esforco Cortante')
grid on
subplot(4,1,2)
plot(1000.*x,Mz)
ylabel('Mz(x) [N.m]')
title('Momento Fletor')
grid on
subplot(4,1,3)
plot(1000.*x,The./(E*Izz))
ylabel('The(x) [rad]')
title('Inclinacaoo da curvatura da viga')
grid on
subplot(4,1,4)
plot(1000.*x,1000*v./(E*Izz))
xlabel('L [mm]')
ylabel('v(x) [mm]')
title('Deslocamento da curvatura da viga')
grid on