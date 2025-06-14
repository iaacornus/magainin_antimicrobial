"""
*
* Instead of utilizing AMBER16/AMBER24, I decided to use
* autodock vina==1.2.5.
*
* Author:   James Aaron Erang <erang.james@clsu2.edu.ph>
*           Biotechnology and Analytical Laboratory
*           Department of Biological Sciences
*           College of Sciences
*           Central Luzon State University
*
"""

from vina import Vina


def compute_score() -> None:
    v = Vina(sf_name='vina')

    v.set_receptor('1iep_receptor.pdbqt')

    v.set_ligand_from_file('1iep_ligand.pdbqt')
    v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])

    # Score the current pose
    energy = v.score()
    print('Score before minimization: %.3f (kcal/mol)' % energy[0])

    # Minimized locally the current pose
    energy_minimized = v.optimize()
    print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
    v.write_pose('1iep_ligand_minimized.pdbqt', overwrite=True)

    # Dock the ligand
    v.dock(exhaustiveness=32, n_poses=20)
    v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=5, overwrite=True)
