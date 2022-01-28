import logging

from particle_simulation import *

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    map_size = MapSize(t_size=50,
                       x_size=30,
                       number_of_particles=15,
                       dim=4
                       )
    init_radius = 0
    max_radius = 10
    name = 'no_move_4d'
    number_of_xpcs_plots = 50
    randow_walk_speed = 0.
    save_animation = True
    no_init_touch = True
    min_distance = 40
    radius_distribution = (0.2, 0.7)
    config_dict = dict(randow_walk_speed=randow_walk_speed,
                       max_radius=max_radius,
                       radius_distribution=radius_distribution,
                       no_init_touch=no_init_touch,
                       min_distance=min_distance,
                       init_radius=init_radius)

    config_dict.update(map_size.asdict())

    # c = Concentrations(map_size).destroy_diff_speeds(share=1,
    #                                                  speed_rate=10,
    #                                                  value_rate=10,
    #                                                  distribution=(0.001, 0.002))
    # c = Concentrations(map_size).born_again(share=0.5,
    #                                         speed_rate=10,
    #                                         value_rate=10,
    #                                         distribution=(0.001, 0.002))
    # c = Concentrations(map_size).linear(-1)
    c = Concentrations(map_size).constant()
    # radius = Radius(
    #     map_size, max_radius=max_radius).destroy_twice(
    #     speed_rate=10, value_rate=10, distribution=(0.2, 0.5))
    # radius = Radius(map_size, max_radius=max_radius).destroy_diff_speeds(
    #     init_value=0,
    #     share=1,
    #     speed_rate=4, value_rate=5, distribution=(0.2, 0.5))
    # radius = Radius(map_size, max_radius=max_radius).linear(
    #     0,
    #     distribution=(1, 0.5))
    # radius = Radius(map_size, max_radius=max_radius).saturation_and_destroy(
    #     init_value=init_radius, saturation_time=0.5,
    #     destroy_time=0.25, distribution=radius_distribution)
    radius = Radius(map_size, max_radius=max_radius).linear()
    # radius = Radius(map_size, max_radius=max_radius).destroy_part(
    #     init_value=init_radius, distribution=radius_distribution)
    # radius = Radius(map_size, max_radius=max_radius).constant(max_radius)
    # centers = Centers(map_size).random_walk(
    #     randow_walk_speed, no_init_touch=no_init_touch,
    #     radius=radius, min_distance=min_distance)
    # centers = Centers(map_size).brownian_motion(radius, 10)
    centers = Centers(map_size).constant_uniform()

    simulation = Simulation(radius=radius,
                            centers=centers,
                            c=c,
                            map_size=map_size)

    simulation.run()
    save = SaveSimulation(name, simulation)
    save.save(number_of_xpcs_plots, save_animation)
    save.save_config(config_dict)
