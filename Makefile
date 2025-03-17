CC=gcc
XMPCC=xmpcc
LIBS=-L/usr/lib -lmpi
INCL=-I /usr/lib/openmpi/include
CCFLAGS=-O3 -funroll-loops


all: histo histo_omp

histo_omp: histo_omp.c
	$(CC) -fopenmp -o histo_omp $(CCFLAGS) histo_omp.c $(LIBS) -lm 

histo: histo.c
	$(XMPCC) -o histo $(CCFLAGS) histo.c $(LIBS)

# run: histo 
# 	mpirun --mca orte_base_help_agregate 0 -host mpihead -n 1 /usr/local/var/mpishare/GLCS-CM6-TDXMP/histo

clean:
	rm histo histo_omp
