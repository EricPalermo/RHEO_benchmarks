Dump Files Names - README

File name: a_b_c.nc
a : Shifting
	- 0 if off
	- 1 if on
b: Reproducing Kernel
	- 0 if off
	- 1 if on
c: Resolution of the System
	- Inverse of sf in LAMMPS script
	- # of cells per unit of length L
	- e.g. if sf = 0.5, resolution = 2 unit cells per length L
	- sf = 0.005 -> c=200
	- sf = 0.05 -> c=20
	- sf = 0.5 -> c=2


