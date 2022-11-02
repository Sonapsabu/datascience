set.seed(100)
cancer <- read.csv("wisc_bc_data.csv")
cancer2 <- cancer
cancer2$diagnosis <- NULL
cancer_clusters <- kmeans(cancer2,2)
print(cancer_clusters)
table(cancer$diagnosis, cancer_clusters$cluster)