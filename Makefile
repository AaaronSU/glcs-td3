CC=gcc
XMPCC=xmpcc
LIBS=-L/usr/lib -lmpi
INCL=-I /usr/lib/openmpi/include
CCFLAGS=-O3 -funroll-loops


all: histo histo_omp

histo_omp.o: histo_omp.c
	$(CC) -c $(CCFLAGS) histo_omp.c

histo.o: histo.c
	$(XMPCC) -c $(CCFLAGS) histo.c

histo_omp: histo_omp.o
	$(CC) -o histo_omp $(CCFLAGS) histo_omp.o $(LIBS) -lm

histo: histo.o
	$(XMPCC) -o histo $(CCFLAGS) histo.o $(LIBS)

run: histo 
	mpirun --mca orte_base_help_agregate 0 -host mpihead -n 1 /usr/local/var/mpishare/GLCS-CM6-TDXMP/histo

clean:
	rm *.o histo input.txt