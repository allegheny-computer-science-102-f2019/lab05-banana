import networkx as nx
from pyvis.network import Network

def build_network(html_name, template):

    built_network = Network(height="100%", width="100%", bgcolor="#222222", font_color="white", directed = True)

    currentGraph = nx.DiGraph()

    node_list = []

    for dataSet in template:

        if node_list.count(dataSet[0]) == 0:

            currentGraph.add_node(dataSet[0])
            node_list.append(dataSet[0])

        if node_list.count(dataSet[1]) == 0:

            currentGraph.add_node(dataSet[1])

            node_list.append(dataSet[0])

        currentGraph.add_edge(dataSet[0], dataSet[1], weight = dataSet[2])

    built_network.from_nx(currentGraph)

    built_network.prep_notebook(custom_template=True, custom_template_path="../data/html/graph_template.html")

    return built_network

def show_network(html_dir, shownNetwork):

    shownNetwork.show(html_dir)
