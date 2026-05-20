rndvalue=1;
npoints=200;
nbinomial=100;

countfile=0;
degrado='d0';

for rndvalue=1:500:1001
    for npoints=[5,10,20,500]
        for nbinomial=[20]
            myf = @(beta,x) beta(1)*x./(beta(2) + x);

            mymodelfun = @(beta,x) 1./(1 + exp(-myf(beta,(x-1))));

            rng(rndvalue,'twister');
            x    = linspace(0,4,npoints)';
            beta = [10;2];

            mu = mymodelfun(beta,x);

            mu = mu./max(mu);

            z = binornd(nbinomial,mu);

            y = z./nbinomial;

%             figure
%             plot(x,y,'g','LineWidth',1)
%             hold on
%             plot(x,mu ,'b'  ,'LineWidth',1)

            [filepath,name,ext] = fileparts(mfilename('fullpath'));
            
			countfile=countfile+1;
			countfilestring=num2str(countfile,'%05.f');
			writematrix([x,y,mu],['01_csv/' degrado '_' countfilestring ... 
				'_' name ...            
                '_rndvalue.' num2str(rndvalue) ...
                '_npoints.' num2str(npoints) ...
                '_nbinomial.' num2str(nbinomial) '.csv'])

			countfile=countfile+1;
			countfilestring=num2str(countfile,'%05.f');
			writematrix([x,y,mu],['01_csv/' degrado '_' countfilestring ... 
				'_' name ...
                '_flip_rndvalue.' num2str(rndvalue) ...
                '_npoints.' num2str(npoints) ...
                '_nbinomial.' num2str(nbinomial) '.csv'])


        end
    end
end


