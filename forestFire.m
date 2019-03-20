function forestFire

%Allocate grid size
nx = 50;
ny = 50;

%initialise cell
cells = zeros(nx, ny);

%Generate random life cells
n = numel(cells);   %Get the number of elements present in 2d array cells
indexArray = randSample(n, n/10);
cells(indexArray) = 1;

%Rules that have to be changed by us