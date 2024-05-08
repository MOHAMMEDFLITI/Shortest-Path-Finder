import osmnx as ox
import networkx as nx
import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static



graph = None

def get_map_data(city_name):
    place_name = city_name + ", Algeria"
    global graph
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph


def get_node_names(graph):
    node_names = {}
    for node in graph.nodes():
        city_name = graph.nodes[node].get('city', None)
        if city_name:
            node_names[node] = city_name
        else:
            node_names[node] = graph.nodes[node].get(
                'name', f"Unnamed Node {node}")
    return node_names


def a_star_search(graph, source, target):
    path = nx.astar_path(graph, source, target, weight='length')
    return path


def plot_shortest_path(graph, shortest_path):
    m = folium.Map(location=(
        graph.nodes[shortest_path[0]]['y'], graph.nodes[shortest_path[0]]['x']), zoom_start=12)
    for i in range(len(shortest_path)-1):
        edge = (shortest_path[i], shortest_path[i+1])
        folium.PolyLine(locations=[(graph.nodes[edge[0]]['y'], graph.nodes[edge[0]]['x']),
                                   (graph.nodes[edge[1]]['y'], graph.nodes[edge[1]]['x'])],
                        color='blue').add_to(m)
    return m


def main():
    st.title("Shortest Path Finder")

    selected_city = st.selectbox("Select City:", cities)
    graph = get_map_data(selected_city)

    node_names = get_node_names(graph)
    selected_source = st.selectbox("Source City:", list(node_names.values()))
    selected_target = st.selectbox(
        "Destination City:", list(node_names.values()))

    if st.button("Find Shortest Path"):
        if selected_source not in node_names.values() or selected_target not in node_names.values():
            st.error("Invalid source or target city.")
        else:
            source_node = next(
                node for node, name in node_names.items() if name == selected_source)
            target_node = next(
                node for node, name in node_names.items() if name == selected_target)
            shortest_path = a_star_search(graph, source_node, target_node)
            m = plot_shortest_path(graph, shortest_path)
            folium_static(m)
            # st_folium(m)


cities = [
    "Adrar", "Ain Defla", "Ain Temouchent", "Alger", "Annaba", "Batna",
    "Bechar", "Bejaia", "Biskra", "Blida", "Bordj Bou Arreridj", "Bouira",
    "Boumerdes", "Chlef", "Constantine", "Djelfa", "El Bayadh", "El Oued",
    "El Tarf", "Ghardaia", "Guelma", "Illizi", "Jijel", "Khenchela",
    "Laghouat", "Muaskar", "Medea", "Mila", "Mostaganem", "Msila", "Naama",
    "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida", "Setif", "Sidi Bel Abbes",
    "Skikda", "Souk Ahras", "Tamanrasset", "Tebessa", "Tiaret", "Tindouf",
    "Tipaza", "Tissemsilt", "Tizi Ouzou", "Tlemcen", "Adrar", "Ain Defla",
    "Ain Temouchent", "Alger", "Annaba", "Batna", "Bechar", "Bejaia", "Biskra",
    "Blida", "Bordj Bou Arreridj", "Bouira", "Boumerdes", "Chlef", "Constantine",
    "Djelfa", "El Bayadh", "El Oued", "El Tarf", "Ghardaia", "Guelma", "Illizi",
    "Jijel", "Khenchela", "Laghouat", "Muaskar", "Medea", "Mila", "Mostaganem",
    "Msila", "Naama", "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida",
    "Setif", "Sidi Bel Abbes", "Skikda", "Souk Ahras", "Tamanrasset", "Tebessa",
    "Tiaret", "Tindouf", "Tipaza", "Tissemsilt", "Tizi Ouzou", "Tlemcen"
]

if __name__ == "__main__":
    main()
