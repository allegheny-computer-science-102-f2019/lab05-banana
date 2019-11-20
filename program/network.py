import networkx as nx
from pyvis.network import Network



def build_network(name):
    net = Network(height="100%", width="100%", bgcolor="#222222", font_color="white", directed = True)

    G = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C", "D"])
    G.add_edges_from([("A","B"),
                        ("A","C"),
                        ("B","E"),
                        ("C","B"),
                        ("D","E")])
    elist = [('A', 'B', 5.0), ('B', 'C', 3.0), ('A', 'C', 1.0), ('C', 'D', 7.3)]
    G.add_weighted_edges_from(elist)

    net.from_nx(G)
    # net.show_buttons(filter_=["manipulation"])
    net.set_options('''
    var options = {
      "nodes": {
        "color": {
          "border": "rgba(230,248,255,1)",
          "background": "rgba(0,227,252,1)",
          "highlight": {
            "border": "rgba(233,104,108,1)",
            "background": "rgba(255,222,223,1)"
          },
          "hover": {
            "border": "rgba(233,182,182,1)",
            "background": "rgba(255,219,218,1)"
          }
        },
        "font": {
          "size": 12
        },
        "scaling": {
          "min": 34,
          "max": 54
        },
        "size": 12
      },
      "edges": {
        "arrows": {
          "to": {
            "enabled": true,
            "scaleFactor": 0.5
          }
        },
        "arrowStrikethrough": false,
        "color": {
          "inherit": true
        },
        "smooth": false
      },
      "manipulation": {
        "enabled": false,
        "initiallyActive": false
      },
      "physics": {
        "barnesHut": {
          "avoidOverlap": 0.04
        },
        "minVelocity": 0.75
      }
    }
    ''')

    net.prep_notebook(custom_template=True, custom_template_path="templates/graph_template.html")
    net.show("./running/" + name + ".html")

build_network("this_test")
