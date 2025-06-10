"""
*
* Author:   James Aaron Erang <erang.james@clsu2.edu.ph>
*           Biotechnology and Analytical Laboratory
*           Department of Biological Sciences
*           College of Sciences
*           Central Luzon State University
*
"""

import matplotlib.pyplot as plt

from IPython.display import SVG

import pandas as pd
from chembl_webresource_client.new_client import new_client


class Visualize:
    """  """

    def __init__(self, mol_arr: list) -> None:
        self.mol_arr = mol_arr
        self.AXES: list = []
        self.fig = plt.figure(figsize=(8,8))

        self.ulimit: int = len(self.mol_arr)
        while self.ulimit%3 != 0:
            self.ulimit += 1

        self.COLS: int = 3
        self.ROWS: int = round(self.ulimit/3)


    def chembl_config(self) -> None:
        mol_target = new_client.molecule
        mol_image = new_client.image
        mol_image.set_format("svg")

        mol_query = mol_target.search("magainin")
        mol_targets: pd.DataFrame = pd.DataFrame.from_dict(mol_query)

    def visualize(self) -> None:
        for i in range(self.ROWS*self.COLS):
            self.AXES.append(
                self.fig.add_subplot(
                    self.ROWS,
                    self.COLS,
                    index=i+1
                )
            )
            fig_title: str = self.mol_arr[i]
            self.AXES[-1].set_title(fig_title)
            plt.axis("off")
            plt.imshow(Image.open(SVG()))



