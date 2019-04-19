% demonstration on how to use IsoFdp.
% 
% Note: we cannot be responsible for its use, misuse, 
% or functionality. 
%


clear
close all
%resultnmi(8)=0;

%for i=1:8
%	[~,~,resultnmi(i),~,~,~,~,~]=IsoFdp(sprintf('LFR_data\\network_mix%d.dat',i),10,30,'structure',15,50,sprintf('LFR_data\\community_mix%d.dat',i),1);
%end
[Clust,Coord,resultnmi,~,~,~,adj_square,~]=IsoFdp('LFR_data\\network_mix1.dat',10,30,'structure',15,50,'LFR_data\\community_mix1.dat',1);

save Clust.mat Clust
save resultnmi.mat resultnmi
save Coord.mat Coord
save adj_square.mat adj_square



