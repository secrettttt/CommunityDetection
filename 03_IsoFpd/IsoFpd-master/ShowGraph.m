clear all
clc
close all

%复杂网络的可视化

%导入数据
data=load('LFR_data\\network_mix1.dat');
S=data(:,1);
E=data(:,2);

g=graph(1000);
add(g,data);

% Plot
plot(g);
title('network')
