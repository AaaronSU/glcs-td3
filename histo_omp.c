#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

float *data_in;

#define WARMUP 5
#define NUMBERRUN 31

int *data_out;

void calcule_histo(float *data, int rows) {
#pragma omp parallel for
  for (int i = 0; i < rows; i++) {
    int j = (int)data[i];
    if ((j >= 0) && (j < 20)) {
      data_out[j]++;
    }
  }
}


int main(int argc, char **argv) {
  if (argc < 2){
    fprintf(stderr, "Usage: %s <nom_du_fichier>\n", argv[0]);
    return -1;
  }

  FILE *file = fopen(argv[1], "r");
  if (file == NULL) {
    fprintf(stderr, "Erreur : impossible d'ouvrir le fichier d'entree\n");
    return 1;
  }
  // Lecture du nombre d'observations
  int rows;
  fscanf(file, "%d", &rows);
  fprintf(stderr, "rows %d\n", rows);
  data_in = malloc(rows * sizeof(int));

  data_out = (int *)malloc(20 * sizeof(int));
  if (data_in == NULL) {
    fprintf(stderr, "Erreur : impossible d'allouer la memoire pour le vecteur "
                    "de donnees\n");
    return 1;
  }

  // Lecture des données du fichier
  for (int i = 0; i < rows; i++) {
    float a;
    fscanf(file, "%f,", &a);
    data_in[i] = a;
  }
  fclose(file);

// Warm-up (5 exécutions sans mesure)
  for (int i = 0; i < 5; i++) {
    calcule_histo(data_in, rows);
  }

  // Mesures des temps d'exécution sur 31 répétitions
  double times[31], mean = 0.0, stddev = 0.0;
  for (int i = 0; i < 31; i++) {
    for (int j = 0; j < 20; j++){
      data_out[j] = 0;
    }
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    
    calcule_histo(data_in, rows);
    end = clock();

    times[i]= ((double) (end - start)) / CLOCKS_PER_SEC;

    mean += times[i];
  }
  
  mean /= 31;
  for (int i = 0; i < 31; i++) {
    stddev += (times[i] - mean) * (times[i] - mean);
  }
  stddev = sqrt(stddev / 31);
  
  double stddev_percent = (stddev / mean) * 100.0;

  // Affichage des résultats uniquement sur le processus 0

  fprintf(stderr, "Temps moyen : %.6f sec\n", mean);
  fprintf(stderr, "Ecart type : %.6f sec (%.2f%%)\n", stddev, stddev_percent);

  // Écriture de l'histogramme
  // Ouverture du fichier de sortie
  char buffer[100];
  sprintf(buffer, "output_omp.txt");
  FILE *output_file = fopen(buffer, "w");
  if (output_file == NULL) {
    fprintf(stderr, "Erreur : impossible d'ouvrir le fichier de sortie\n");
    return 1;
  }

  for (int i = 0; i < 20; i++) {
  fprintf(output_file, "%u ", i);
  }
  fprintf(output_file, "\n");
  for (int i = 0; i < 20; i++) {
    fprintf(output_file, "%u ", data_out[i]);
  }
  fprintf(output_file, "\n");
  fclose(output_file);
  

  free(data_in);
  free(data_out);

  return 0;
}
