import csvParse
import network

csvFileName = "stormofswords"
htmlFileName = "myNetwork"

csvDir = "../data/csv/" + csvFileName + ".csv"
htmlDir = "../data/html/" + htmlFileName + ".html"

templateNetwork = csvParse.read_csv(csvFileName)

currentNetwork = network.build_network(htmlFileName, templateNetwork)

network.show_network(htmlDir, currentNetwork)
