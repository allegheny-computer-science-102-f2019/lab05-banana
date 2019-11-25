import csv

def read_csv(name):

    networkTemplate = []
    networkEdge = ()

    csv_dir = "../data/csv/" + name + ".csv"

    with open(csv_dir) as csv_file:

        # csv_reader = csv.reader(csv_file)
        csv_reader = csv.reader(csv_file, delimiter = ',')

        line_count = 0

        for row in csv_reader:

            if row[0] != "Source":
                
                networkEdge = (row[0], row[1], row[2])
                networkTemplate.append(networkEdge)

    return networkTemplate
