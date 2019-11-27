import networkx as nx
from pyvis.network import Network
import csvParse


def build_network(html_name, csv):

    built_network = Network(height="100%", width="100%", bgcolor="#19232D", font_color="#F0F0F0", directed = True)

    currentGraph = nx.DiGraph()

    node_list = []

    importedCSV = csvParse.read_csv(csv)

    for dataSet in importedCSV:
        if node_list.count(dataSet[0]) == 0:
            currentGraph.add_node(dataSet[0])
            node_list.append(dataSet[0])

        if node_list.count(dataSet[1]) == 0:
            currentGraph.add_node(dataSet[1])
            node_list.append(dataSet[0])

        currentGraph.add_edge(dataSet[0], dataSet[1], weight = dataSet[2])

    built_network.from_nx(currentGraph)
    neighbor_map = built_network.get_adj_list()

    for node in built_network.nodes:
        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
        node["value"] = len(neighbor_map[node["id"]])


    built_network.barnes_hut()
    #built_network.show_buttons()
    built_network.prep_notebook(custom_template=True, custom_template_path="templates/graph_template.html")
    built_network.show("./running/" + html_name + ".html")


def show_network(html_dir, shownNetwork):

    shownNetwork.show(html_dir)
