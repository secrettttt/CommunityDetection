clear
close all

%����
[Clust,Coord,~,~,~,~,~,~]=IsoFdp('network.dat',10,30,'structure',15,50,'community.dat',1);

%������
save Clust.mat Clust
save Coord.mat Coord


