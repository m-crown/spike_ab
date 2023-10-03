import pandas as pd

alpha = pd.read_csv("alpha.csv")
alpha["lineage"] = "alpha"
beta = pd.read_csv("beta.csv")
beta["lineage"] = "beta"
gamma = pd.read_csv("gamma.csv")
gamma["lineage"] = "gamma"
delta = pd.read_csv("delta.csv")
delta["lineage"] = "delta"
omicron = pd.read_csv("omicron.csv")
omicron["lineage"] = "omicron"
ba_1 = pd.read_csv("ba_1.csv")
ba_1["lineage"] = "ba_1"
ba_2 = pd.read_csv("ba_2.csv")
ba_2["lineage"] = "ba_2"
ba_3 = pd.read_csv("ba_3.csv")
ba_3["lineage"] = "ba_3"
ba_4 = pd.read_csv("ba_4.csv")
ba_4["lineage"] = "ba_4"
ba_5 =pd.read_csv("ba_5.csv")
ba_5["lineage"] = "ba_5"

lineages = pd.concat([alpha, beta, gamma, delta, omicron, ba_1, ba_2, ba_3, ba_4, ba_5])

def take_random_sample(group, n):
    if n >= len(group):
        return group
    return group.sample(n=n)

lineages_subset = lineages.groupby("lineage").apply(lambda group: take_random_sample(group, n = 500)).reset_index(drop = True)
lineages_subset.to_csv("lineages_subset_metadata.csv")
lineages_subset.gisaidEpiIsl.to_csv("gisaid_epi_isl.csv", header = None, index = False)