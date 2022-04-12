% -------------------------------------------------
%       Codigo Matlab para implementacao
%           de modelo de viga
% -------------------------------------------------
%       Modelo de Viga: Exemplo 01 da apostila
% -------------------------------------------------
clc, clear, close all
l=1; % comprimento da viga [m]
P=1; % carregamento distribuido [N/m]

% dimensoes da secao
Izz=1;
% propriedades do material
E=1; % Aco

% dominio estrutural
dx=0.001;
dy=0.001;
x=0:dx:l;
% y=-h:dy:h;
% Vy = zeros(1,size(x,2)); 
% Mz = zeros(1,size(x,2)); 

% v = zeros(1,size(x,2));

v = -P/6.*(x-l/2).^3.*(x>=l/2) + 11*P/96.*x.^3 - 3*P*l/32.*x.^2;
The = -P/2.*(x-l/2).^2.*(x>=l/2) + 11*P/32.*x.^2 - 3*P*l/16.*x;
Mz= -P.*(x-l/2).^1.*(x>=l/2) + 11*P/16.*x - 3*P*l/16;
Vy= -P.*(x-l/2).^0.*(x>=l/2) + 11*P/16;

figure()
subplot(4,1,1)
% plot(x,Vy)
% ylabel('Vy(x) [N]')
% title('Esforco Cortante')
% grid on
% subplot(4,1,2)
% plot(x,Mz)
% ylabel('Mz(x) [N.m]')
% title('Momento Fletor')
% grid on
subplot(2,1,1)
plot(x,The)
ylabel('The(x) [rad]')
title('Inclinacaoo da curvatura da viga')
grid on
subplot(2,1,2)
plot(x,v)
xlabel('L [mm]')
ylabel('v(x) [mm]')
title('Deslocamento da curvatura da viga')
grid on

% figure()
% % [X,Y]=meshgrid(x,y);
% % Mz_xy = Mz.*(ones(size(y,2),size(x,2)));
% % Sigxx=-((Y./Izz).*Mz_xy);
% % contour(X,Y,Sigxx./1E6,8,'ShowText','on')
% % title('Tensao Normal [MPa]')
% xlabel('L')
% ylabel('h')
% grid on