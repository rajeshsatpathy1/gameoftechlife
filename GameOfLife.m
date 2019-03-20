function GameOfLife
clear
close all
clc

% Grid size
nelx = 100;
nely = 100;


% Initial cell
cells = zeros(nelx, nely);
% Generate random life cells
idx = randsample(numel(cells), numel(cells)/10);
cells(idx) = 1;
showCells(cells);

% Rules
while (1)
    % Next generation
    cellsNew = findNeighbor(cells);
    % Update
    cells = cellsNew;
    % Visualization
    showCells(cells);
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
[nelx, nely] = size(c);

cNew = zeros(size(c));
% Initial loop
idx = 0;
for ely = 2:nely+1
    for elx = 2:nelx+1
        idx = idx + 1;
        count = sum(sum(cExt(elx-1:elx+1, ely-1:ely+1))) - c(idx);
        % Rule 1: Any live cell with fewer than two live neighbours dies,
        % as if caused by under-population.
        if (c(idx) == 1) && (count < 2)
            cNew(idx) = 0;
        end
        % Rule 2: Any live cell with two or three live
        % neighbours lives on to the next generation.
        if (c(idx) == 1) && ((count == 2) || (count == 3));
            cNew(idx) = 1;
        end
        % Rule 3: Any live cell with more than three live neighbours dies,
        % as if by overcrowding.
        if (c(idx) == 1) && (count > 3);
            cNew(idx) = 0;
        end
        % Rule 4: Any dead cell with exactly three live neighbours
        % becomes a live cell, as if by reproduction.
        if (c(idx) == 0) && (count == 3);
            cNew(idx) = 1;
        end
    end
end

end

function showCells(cells)
% Visualization
imagesc(cells); caxis([0 1]);
colormap(flipud(gray)); axis off; axis equal; drawnow
end