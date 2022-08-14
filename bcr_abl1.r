####currently not ready


#a custom imputer if necessary for re-analyzing
imputer <- function(col_vector, method="mean") {
  fillna <- NaN
  if (method == "mean" || method=="average") {
    fillna <- mean(col_vector)
  }
  #probably not the best choice for integer column vector
  else if (method == "median") {
    fillna <- median(col_vector)
  }
  for (ridx in which(is.na(col_vector)) ) {
    col_vector[ridx] <- fillna
  }
  col_vector <- col_vector
}

clin_df <- read.delim("clinvar_result.txt")

#specifically analyze ABL1 genes as cases
genes <- clin_final$Gene.s.
freq <- c()  #entire number of genes summed up
condition_freq <- c()  #also need to record conditions for genes

for (pos in 1:length(genes) ) {
  sample = genes[pos]
  genes_per_samples <- strsplit(sample, split="|", fixed=TRUE)
  
  patient_condition <- clin_final[pos, "Condition.s."]
  if (!( patient_condition %in% names(condition_freq) )) {
    condition_freq[patient_condition] = c()  #another hashmap/dictionary data structure
  }
  
  for (G in genes_per_samples[[1]]) {
    #again, counting number of genes in general
    if (!(G %in% names(freq))) {
      freq[G] = 0
    }
    freq[G] = freq[G]+1
    if ( !(G %in% names(condition_freq[[patient_condition]])) ) {
      condition_freq[[patient_condition]][G] = 0
    }
    condition_freq[[patient_condition]][G] = condition_freq[[patient_condition]][G]+1
  }
}

#extremely clean and efficient pattern/ordinal encoder I programmed
patternEnc <- function(feature, patterns, data=clin_final, LE=0) {
  original <- as.matrix(data[,feature])
  encoded <- rep(0, nrow(data))
  for (mod_ in patterns) {
    for (j in grep(mod_, original)) {
      encoded[j] = LE
    }
    LE = LE + 1
  }
  encoded
}

#retreiving the clinical sig.


###example class
# create a list with required components
movieList <- list(name = "Iron man", leadActor = "Robert Downey Jr")
# give a name to your class
class(movieList) <- "movie"















