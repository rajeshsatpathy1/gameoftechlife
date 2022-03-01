function forestFire
    %Burning Tree - 2; 

    %Allocate grid size
    nx = 100;
    ny = 100;

    %initialise cell
    cells = zeros(nx, ny);

    %Generate random life cells
    n = numel(cells);   %Get the number of elements present in 2d array cells
    treeArray = randsample(n, n/5);
    cells(treeArray) = 1;
    fireTreeArray = randsample(n,n/500);
    if(cells(treeArray) == 1)
        cells(fireTreeArray) = 2
    end
    %showCells(cells);
    %Rules that have to be changed by us
    %main loop that has iterations
    t.StartDelay = 1;
    t.TimerFcn = @(myTimerObj, thisEvent)disp('3 seconds have elapsed');
    while(1)
        %Next generation cell locations
        newCells = findNeighbor(cells);
        cells = newCells;
        %Check out the cell map
        showCells(cells);
        t.TimerFcn = @(myTimerObj, thisEvent)disp('a sec has passed');
    end
end

function cNew = findNeighbor(c)
    % Periodic boundary condition
    cExt = zeros(size(c)+2);
    cExt(2:end-1, 2:end-1) = c;
    cExt(1, 2:end-1) = c(end, :);
    cExt(end, 2:end-1) = c(1, :);
    cExt(2:end-1, 1) = c(:, end);
    cExt(2:end-1, end) = c(:, 1);
    % Four corners
    cExt(1, 1) = c(end, end);
    cExt(1, end) = c(end, 1);
    cExt(end, 1) = c(1, end);
    cExt(end, end) = c(1, 1);
    [nx, ny] = size(c);
    
    cNew = zeros(size(c));
    %Initial loop
    idx = 0;
    
    for ely = 2:ny+1
        for elx = 2:nx+1
            idx = idx + 1;
            count = sum(sum(cExt(elx-1:elx+1, ely-1:ely+1))) - c(idx); %Gives the number of neighbors
            %Rules:
            %Rule 1: Burning cell turns to empty cell
            if(c(idx) == 2)
                cNew(idx) = 0;
            end
            %Rule 2: A tree will burn if at least one neighbor is burning
            if(c(idx) == 1 && count >= 1)
                cNew(idx) = 1;
            end
            %Rule 3: A tree ignites with probability f even if no neighbor
            %        is burning
            %Rule 4: An empty space fills with a probability p
            
        end
    end
            
end



function showCells(cells)
    % Visualization
    imagesc(cells); 
    %caxis([0 1 2]);
    colormap([0.3,0.3,0.3;0,1,0;1,0,0]); 
    axis off; 
    axis equal; 
    drawnow
end
