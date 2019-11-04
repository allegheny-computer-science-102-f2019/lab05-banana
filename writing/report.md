### Team name: Banana
### Group Member Names: Adam Cook, Danny Ullrich, Caden Koscinski
### Date: 23 Oct 2019

 1. Main Idea where the questions-in-blue from the assignment sheet are generally satisfied.
 From an incredibly broad perspective, the objective of our project is to produce a user-driven experience pertaining to some application of graph theory. To distinguish our lab from the graph theory tutorial present in our previous practical, we are emphasizing the application of directional network graphs. Additionally, data handling will be a much greater factor than our previous experiences in class, where our project will incorporate either file-driven (csv, txt, etc.) or specified user inputs in order to generate relevant and applicable networks. As we are in a very early stage planning our project development and narrowing our objective, more ambitious routes for data entry may be considered as potential alternatives. Excel spreadsheets may be employed in order to simplify computations using Excel’s formula handling before data reaches the code, or other external resources may be referenced to facilitate the accurate representation and interpretation of user-entered data. The reverse process may be considered as well, where a network could be exported in the form of a csv to be displayed through Excel (or other similar means).
Beyond concepts and methods, our general project idea will also be applicable to a variety of logistics issues in some form in order to emphasize our directional network functionality. The flow of traffic, interstate cargo, flight paths, and intercity delivery could all be represented in this fashion. For a lower-scale or more personable consumer, a much simpler application such as school bus routes or tour guides could be used that would also present network data in a much more digestible interface.
Furthermore, to maintain network clarity without losing information density, our project may incorporate a data structure that treats each vertex and edge within the network as its own data point to which files can be assigned to. Not only does this allow for intuitive user interaction, but data can be hidden and displayed individually allowing for only relevant data to be focused on. A potential application using this system, in reference to interstate cargo, may be warehouse inventories on vertices and toll costs on edges. An intercity delivery system may include a functionality that excludes all roads without left turns, optimizing delivery times by referencing the data values stored on vertices and edges. To parallel the smaller, less demanding personal consumer perspective, a school bus route may optimize travel times and fuel costs that save townships expenses. Once again, the benefit of choosing which data to display or exclude simplifies the end user experience while simultaneously emphasizing the importance of the directional networks we intend on dealing with.
To illustrate the above in more simplistic terms, our motivation is centered on several core concepts pertaining to our directional network application. The foremost of which is the user experience, which is composed of several factors including user interaction and data display control. Another factor concerns the comprehendible handling of data, both in terms of the importation and exportation of csv files as well as the integration of vertex and edge focused data files. The last concern is our industry and economic motivation, where the networks we create can be used to optimize real-world (albeit reduced to a CS102 level) problems such as travel times and fuel costs using relatively simplistic formulas.
As far as the technical requirements of this project proposal are concerned, the connections to computer science are implicit in the above applications. Discrete structures are a fundamental component of data science, and data encapsulation from both a security and ease-of-access standpoint is integral to data science as well. Furthermore, when dealing with larger networks, big data and cloud computing become relevant factors as well. Despite these topics being beyond the scope of our lab, efficient memory usage and optimizing the processing speed of data-focused process are important and relevant to discrete structures.
Lastly, our key takeaways from this project will be the experience in the implementation and execution of several libraries and utilities. The list tentatively includes matplotlib, network, Tkinter, and flask. Additionally, with the prior emphasis on user interaction in mind, many UI/UX concepts will be employed in order to create accurate and dependable visuals. Lastly, the handling of csv files in regards to handling data (or referencing Excel for help with simplifying computations) is a relatively foreign concept despite the nature of the course.



 2. The articles (five or so) where the questions-in blue from the assignment sheet are generally satisfied.

APPLICATIONS OF GRAPH THEORY IN COMPUTER SCIENCE AN OVERVIEW
This article talks about how mathematics influences a large number of other subjects. Application of graph theory has allowed for the testing of theoretical concepts. This article can help our project by giving us an understanding of many of the applications that have already been implemented using graph theory, providing ideas and options. This will assist us on our project by giving us a background and further understanding of what graph theory is. By having a better understanding of the background of graph theory, it will allow us to better implement mechanics of in a meaningful way. By giving background to what graph theory is, it walk through the mathematical background and function possible. In class, we have learned about a ways to draw graph theory, but this article dives deeper into more ways to describe and depict graph theory, such as with polygons of the voronai graph, and three dimensional nodes.

Shirinivas, S. G., S. Vetrivel, and N. M. Elango. "Applications of graph theory in computer science an overview." International journal of engineering science and technology 2.9 (2010): 4610-4621.

APPLIED GRAPH THEORY IN COMPUTER VISION AND PATTERN RECOGNITION
Another application of graph theory is pattern recognition, allowing computers to begin to understand images. This plays a large role in being able to compute photos, and is especially important going into the future with self driving cars, facial detection, etc...

Kandel, Abraham, Horst Bunke, and Mark Last, eds. Applied graph theory in computer vision and pattern recognition. Springer Science & Business Media, 2007.

NetworkX Reference PDF

1. As the nature of this source is a reference PDF and not necessarily an academic article, the importance of this source is the documentation regarding the NetworkX package. NetworkX will serve as the foundation for our graph and network generation and manipulation.

2. Using NetworkX for the foundational data structure will enable our group to focus our efforts on using graph theory to solve relevant problems. This is opposed to spending time creating the underlying data structure and necessary code for displaying said structure.

3. NetworkX directly represents an application of graph theory and network structure as well as serving as experience learning from a Python3 library.

4. NetworkX contains a plethora of methods and algorithms involving the manipulation of graphs and networks. This is deliberately vague as there are a variety of applicable algorithms dealing with networks with an equally diverse set of network properties (i.e. determining the order of a graph, sink nodes, Eulerian Trails, etc).

5. NetworkX, as it is the foundation for our graph generation, also contains a multitude of mathematical methods involving the representation, optimization, and manipulation of graph theory applications. A possible example would include a mathematical equation that references vertex data in order to determine the maximum order given a number of vertices.

6. Graph theory in general provides experience and insight pertaining to UI/UX in the case of end users directly interacting with a visual, mutable graph.

7. Graph theory has been a major class focus, which is the main motivation for our team including NetworkX in our project.

NetworkX Developers. “NetworkX.” NetworkX, networkx.github.io/.

Flask Reference PDF

1. Once again, in the same spirit of NetworkX, the Flask documentation provides a web application framework for use with Python3 libraries and code. Having a web-based project greatly enhances and simplifies user interaction.

2. As mentioned above, running our project off a website will encourage more practical application access as well as simplify the user experience (No console or Github knowledge required, input sanitization, etc.).

3. While Flask is generally Python package and library friendly, websites in their own right require a great deal of data structure and proper code development.

4. Web application development is a massive component and mechanism of computer science, and flask enables our team to work with this form of application without extensive knowledge of HTML5, CSS, Javascript, etc.

5. As Flask serves more to enhance our project and less so to construct the code of our project, the majority of the plausible mathematics involved in website development most likely concern the translation of local code to code that functions without console facilitation (i.e. more efficient browser-based calculations). 

6. Again, web application development is more than just a set of mechanisms and algorithms for online code projection. Accessing and utilizing the web itself is a massive part of computer science in general, as well as emphasizing our UI/UX focus.

7. Websites necessitate the proper application of discrete data structures in order to present and transport data in a unified fashion. Adherence to the principles of said discrete data structures will enable our project to function correctly on any system and ideally any browser.

#### (Note: Did you remember to add your names and the team name to this document!?!)
