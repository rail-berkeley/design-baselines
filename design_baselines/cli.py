from ray import tune
import click
import ray
import os


@click.group()
def cli():
    """A group of potential sub methods that are available for use through
    a command line interface
    """


#############


@cli.command()
@click.option('--local-dir', type=str, default='conservative-ensemble-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def conservative_ensemble_dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "target_conservative_gap": 0.0,
        "initial_alpha": 0.0,
        "alpha_lr": 0.0,
        "perturbation_lr": 0.00005,
        "perturbation_steps": 0,
        "perturbation_backprop": False,
        "solver_samples": 128,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_steps": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='conservative-ensemble-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def conservative_ensemble_ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "AntMorphology-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "target_conservative_gap": 0.0,
        "initial_alpha": 0.0,
        "alpha_lr": 0.0,
        "perturbation_lr": 0.00005,
        "perturbation_steps": 0,
        "perturbation_backprop": False,
        "solver_samples": 128,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_steps": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='perturbation-backprop-policy')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def perturbation_backprop_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "HopperController-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "target_conservative_gap": 0.0,
        "initial_alpha": 100.0,
        "alpha_lr": 0.0,
        "perturbation_lr": 0.0005,
        "perturbation_steps": tune.grid_search([0, 10, 25, 50, 75, 100]),
        "perturbation_backprop": True,
        "solver_samples": 128,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_steps": 1000},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='conservative-ensemble-policy')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def conservative_ensemble_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "HopperController-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "target_conservative_gap": 0.0,
        "initial_alpha": 100.0,
        "alpha_lr": 0.0,
        "perturbation_lr": 0.0005,
        "perturbation_steps": 100,
        "perturbation_backprop": False,
        "solver_samples": 128,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='perturbation-backprop-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def perturbation_backprop_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {"seed": tune.randint(1000)},
        "is_discrete": True,
        "activations": [["leaky_relu", "leaky_relu"]],
        "alpha_lr": 0.0,
        "batch_size": 128,
        "epochs": 200,
        "forward_model_lr": 0.001,
        "hidden_size": 50,
        "initial_alpha": 0.1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "keep": 0.5,
        "perturbation_backprop": True,
        "perturbation_lr": 18.0,
        "perturbation_steps": 50,
        "solver_lr": 18.0,
        "solver_samples": 128,
        "solver_steps": 200,
        "target_conservative_gap": 0.0,
        "temp": 100.0,
        "val_size": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='conservative-ensemble-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def conservative_ensemble_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {"seed": tune.randint(1000)},
        "is_discrete": True,
        "activations": [["leaky_relu", "leaky_relu"]],
        "alpha_lr": 0.0,
        "batch_size": 128,
        "epochs": 200,
        "forward_model_lr": 0.001,
        "hidden_size": 50,
        "initial_alpha": 0.002,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "keep": 0.5,
        "perturbation_backprop": False,
        "perturbation_lr": 18.0,
        "perturbation_steps": 50,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_samples": 128,
        "solver_steps": 500,
        "target_conservative_gap": 0.0,
        "temp": 100.0,
        "val_size": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='conservative-ensemble-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def conservative_ensemble_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.conservative_ensemble import conservative_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(conservative_ensemble, config={
        "logging_dir": "data",
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "noise_std": 0.1,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 50,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "target_conservative_gap": 0.0,
        "initial_alpha": tune.grid_search([0.0, 0.0001, 0.001, 0.01, 0.1]),
        "alpha_lr": 0.0,
        "perturbation_lr": tune.grid_search([0.1, 0.5, 1.0, 2.0, 5.0]),
        "perturbation_steps": tune.grid_search([0, 10, 50, 100, 500, 1000]),
        "perturbation_backprop": False,
        "solver_samples": 128,
        "solver_lr": tune.sample_from(lambda c: c['config']['perturbation_lr']),
        "solver_steps": 1000},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "bootstraps": 1,
        "noise_std": 0.,
        "val_size": 500,
        "batch_size": 128,
        "epochs": 500,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.00001,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "AntMorphology-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "bootstraps": 1,
        "noise_std": 0.,
        "val_size": 500,
        "batch_size": 128,
        "epochs": 50,
        "hidden_size": 128,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.00005,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-molecule')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_molecule(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "MoleculeActivity600885-v0",
        "task_kwargs": {},
        "is_discrete": True,
        "bootstraps": 5,
        "keep": 0.7,
        "temp": 1.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": tune.grid_search([10.0, 7.5, 5.0, 2.5, 1.0, 0.5]),
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-policy')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "HopperController-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "bootstraps": 1,
        "noise_std": 0.1,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 128,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.0005,
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "is_discrete": True,
        "bootstraps": 5,
        "keep": 0.5,
        "temp": 100.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 50,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 10.0,
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='forward-ensemble-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def forward_ensemble_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.forward_ensemble import forward_ensemble
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(forward_ensemble, config={
        "logging_dir": "data",
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "bootstraps": 5,
        "noise_std": 0.1,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 256,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='vary-architecture-policy')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def vary_architecture_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.vary_architecture import vary_architecture
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(vary_architecture, config={
        "logging_dir": "data",
        "task": "HopperController-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "activations": [['swish', 'swish'],
                        ['swish', 'tanh'],
                        ['tanh', 'swish'],
                        ['tanh', 'tanh']],
        "noise_std": 0.1,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 128,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='vary-architecture-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def vary_architecture_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.vary_architecture import vary_architecture
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(vary_architecture, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "is_discrete": True,
        "activations": [['leaky_relu', 'leaky_relu'],
                        ['leaky_relu', 'tanh'],
                        ['tanh', 'leaky_relu'],
                        ['tanh', 'tanh']],
        "keep": 0.5,
        "temp": 100.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 50,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": tune.grid_search([50.0, 60.0, 70.0, 80.0, 90.0, 100.0]),
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='vary-architecture-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def vary_architecture_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.vary_architecture import vary_architecture
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(vary_architecture, config={
        "logging_dir": "data",
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "is_discrete": False,
        "activations": [['swish', 'swish'],
                        ['swish', 'tanh'],
                        ['tanh', 'swish'],
                        ['tanh', 'tanh']],
        "noise_std": 0.1,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 200,
        "hidden_size": 256,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "solver_samples": 128,
        "solver_lr": 0.005,
        "solver_steps": 200},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='cbas-molecule')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_molecule(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": True,
        "task": "MoleculeActivity600885-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 128,
        "vae_batch_size": 32,
        "hidden_size": 256,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "latent_size": 32,
        "vae_lr": 0.001,
        "vae_beta": 5.0,
        "offline_epochs": 100,
        "online_batches": 50,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='cbas-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": True,
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 128,
        "vae_batch_size": 10,
        "hidden_size": 50,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "latent_size": 20,
        "vae_lr": 0.001,
        "vae_beta": 1.0,
        "offline_epochs": 100,
        "online_batches": 70,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='cbas-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "HopperController-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "vae_batch_size": 50,
        "hidden_size": 2048,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "latent_size": 256,
        "vae_lr": 0.001,
        "vae_beta": 1000.0,
        "offline_epochs": 100,
        "online_batches": 24,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='cbas-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 256,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "latent_size": 32,
        "vae_lr": 0.005,
        "vae_beta": 20.0,
        "offline_epochs": 200,
        "online_batches": 128,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='cbas-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "AntMorphology-v0",
        "task_kwargs": {},
        "bootstraps": 1,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 50,
        "latent_size": 32,
        "vae_lr": 0.0001,
        "vae_beta": 10.0,
        "offline_epochs": 100,
        "online_batches": 10,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='cbas-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def cbas_dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.cbas import condition_by_adaptive_sampling
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(condition_by_adaptive_sampling, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "DKittyMorphology-v0",
        "task_kwargs": {},
        "bootstraps": 1,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 500,
        "latent_size": 32,
        "vae_lr": 0.0005,
        "vae_beta": 2.0,
        "offline_epochs": 200,
        "online_batches": 10,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-molecule')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_molecule(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": True,
        "task": "MoleculeActivity600885-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "oracle_batch_size": 128,
        "vae_batch_size": 32,
        "hidden_size": 256,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "oracle_lr": 0.001,
        "oracle_epochs": 100,
        "autofocus_epochs": 10,
        "latent_size": 32,
        "vae_lr": 0.001,
        "vae_beta": 5.0,
        "offline_epochs": 100,
        "online_batches": 50,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": True,
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "bootstraps": 5,
        "val_size": 200,
        "oracle_batch_size": 128,
        "vae_batch_size": 10,
        "hidden_size": 50,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "oracle_lr": 0.001,
        "oracle_epochs": 100,
        "autofocus_epochs": 10,
        "latent_size": 20,
        "vae_lr": 0.001,
        "vae_beta": 1.0,
        "offline_epochs": 100,
        "online_batches": 70,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "HopperController-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "oracle_batch_size": 100,
        "vae_batch_size": 50,
        "hidden_size": 2048,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "oracle_lr": 0.001,
        "oracle_epochs": 100,
        "autofocus_epochs": 10,
        "latent_size": 256,
        "vae_lr": 0.001,
        "vae_beta": 10000.0,
        "offline_epochs": 100,
        "online_batches": 24,
        "online_epochs": 10,
        "iterations": 50,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "oracle_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 256,
        "initial_max_std": 1.5,
        "initial_min_std": 0.5,
        "oracle_lr": 0.001,
        "oracle_epochs": 100,
        "autofocus_epochs": 10,
        "latent_size": 32,
        "vae_lr": 0.005,
        "vae_beta": 30.0,
        "offline_epochs": 200,
        "online_batches": 128,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "AntMorphology-v0",
        "task_kwargs": {},
        "bootstraps": 1,
        "val_size": 200,
        "oracle_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_epochs": 50,
        "autofocus_epochs": 10,
        "latent_size": 32,
        "vae_lr": 0.0001,
        "vae_beta": 10.0,
        "offline_epochs": 100,
        "online_batches": 10,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='autofocused-cbas-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def autofocused_cbas_dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.autofocused_cbas import autofocused_cbas
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(autofocused_cbas, config={
        "logging_dir": "data",
        "is_discrete": False,
        "task": "DKittyMorphology-v0",
        "task_kwargs": {},
        "bootstraps": 1,
        "val_size": 200,
        "oracle_batch_size": 100,
        "vae_batch_size": 100,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_epochs": 500,
        "autofocus_epochs": 10,
        "latent_size": 32,
        "vae_lr": 0.0005,
        "vae_beta": 2.0,
        "offline_epochs": 200,
        "online_batches": 10,
        "online_epochs": 10,
        "iterations": 200,
        "percentile": 80.0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='mins-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": True,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 5.0,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 20,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.1,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.1,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 50,
        "epochs_per_iteration": 40,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": 20.,
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-molecule')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_molecule(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "MoleculeActivity-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": True,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 5.0,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 20,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.1,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.1,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 50,
        "epochs_per_iteration": 40,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": 20.,
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_policy(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "HopperController-v0",
        "task_kwargs": {},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": False,
        "noise_std": 0.01,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 32,
        "generator_lr": 2e-5,
        "generator_beta_1": 0.1,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-5,
        "discriminator_beta_1": 0.1,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 200,
        "epochs_per_iteration": 20,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": tune.grid_search([0.002, 0.004, 0.006, 0.01, 0.05]),
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "Superconductor-v0",
        "task_kwargs": {},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": False,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 32,
        "generator_lr": 2e-5,
        "generator_beta_1": 0.5,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.5,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 200,
        "epochs_per_iteration": 20,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": 0.1,
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "AntMorphology-v0",
        "task_kwargs": {},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": False,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 32,
        "flip_frac": 0.,
        "pool_size": 0,
        "pool_frac": 0.,
        "pool_save": 0,
        "fake_pair_frac": 0.,
        "penalty_weight": 0.0,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.5,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.5,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 1000,
        "epochs_per_iteration": 20,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": 0.1,
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def mins_dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.mins import model_inversion
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(model_inversion, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-v0",
        "task_kwargs": {},
        "val_size": 200,
        "fully_offline": False,
        "is_discrete": False,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "gan_batch_size": 128,
        "hidden_size": 2048,
        "latent_size": 32,
        "generator_lr": 2e-5,
        "generator_beta_1": 0.5,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-5,
        "discriminator_beta_1": 0.2,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 200,
        "epochs_per_iteration": 20,
        "iterations": 100,
        "exploration_samples": 100,
        "exploration_rate": 0.1,
        "thompson_samples": 100,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='lsgan-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def lsgan_gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Train a forward model using various regularization methods and
    solve a model-based optimization problem

    Args:

    local_dir: str
        the path where model weights and tf events wil be saved
    cpus: int
        the number of cpu cores on the host machine to use
    gpus: int
        the number of gpu nodes on the host machine to use
    num_parallel: int
        the number of processes to run at once
    num_samples: int
        the number of samples to take per configuration
    """

    from design_baselines.lsgan import least_squares_gan
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             temp_dir=os.path.expanduser('~/tmp'))
    tune.run(least_squares_gan, config={
        "logging_dir": "data",
        "task": "GFP-v0",
        "task_kwargs": {'seed': tune.randint(1000)},
        "val_size": 200,
        "is_discrete": True,
        "keep": 0.9,
        "start_temp": 5.0,
        "final_temp": 1.0,
        "gan_batch_size": 128,
        "hidden_size": 256,
        "latent_size": 20,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.5,
        "generator_beta_2": 0.999,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.5,
        "discriminator_beta_2": 0.999,
        "initial_epochs": 200,
        "solver_samples": 100},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--dir', type=str)
@click.option('--tag', type=str)
@click.option('--xlabel', type=str)
@click.option('--ylabel', type=str)
@click.option('--separate-runs', is_flag=True)
def plot(dir, tag, xlabel, ylabel, separate_runs):

    from collections import defaultdict
    import glob
    import os
    import re
    import pickle as pkl
    import pandas as pd
    import tensorflow as tf
    import tqdm
    import seaborn as sns
    import matplotlib.pyplot as plt

    def pretty(s):
        return s.replace('_', ' ').title()

    # get the experiment ids
    pattern = re.compile(r'.*/(\w+)_(\d+)_(\w+=[\w.+-]+[,_])*(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\w{10})$')
    dirs = [d for d in glob.glob(os.path.join(dir, '*')) if pattern.search(d) is not None]
    matches = [pattern.search(d) for d in dirs]
    ids = [int(m.group(2)) for m in matches]

    # sort the files by the experiment ids
    zipped_lists = zip(ids, dirs)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    ids, dirs = [list(tuple) for tuple in tuples]

    # get the hyper parameters for each experiment
    params = []
    for d in dirs:
        with open(os.path.join(d, 'params.pkl'), 'rb') as f:
            params.append(pkl.load(f))

    # concatenate all params along axis 1
    all_params = defaultdict(list)
    for p in params:
        for key, val in p.items():
            if val not in all_params[key]:
                all_params[key].append(val)

    # locate the params of variation in this experiment
    params_of_variation = []
    for key, val in all_params.items():
        if len(val) > 1 and not isinstance(val[0], dict):
            params_of_variation.append(key)

    # get the task and algorithm name
    task_name = params[0]['task']
    algo_name = matches[0].group(1)
    if len(params_of_variation) == 0:
        params_of_variation.append('task')

    # read data from tensor board
    data = pd.DataFrame(columns=['id', xlabel, ylabel] + params_of_variation)
    for i, (d, p) in enumerate(tqdm.tqdm(zip(dirs, params))):
        for f in glob.glob(os.path.join(d, '*/events.out*')):
            for e in tf.compat.v1.train.summary_iterator(f):
                for v in e.summary.value:
                    if v.tag == tag:
                        row = {'id': i,
                               ylabel: tf.make_ndarray(v.tensor).tolist(),
                               xlabel: e.step}
                        for key in params_of_variation:
                            row[key] = f'{pretty(key)} = {p[key]}'
                        data = data.append(row, ignore_index=True)

    if separate_runs:
        params_of_variation.append('id')

    # save a separate plot for every hyper parameter
    for key in params_of_variation:
        plt.clf()
        g = sns.relplot(x=xlabel, y=ylabel, hue=key, data=data,
                        kind="line", height=5, aspect=2,
                        facet_kws={"legend_out": True})
        g.set(title=f'Evaluating {pretty(algo_name)} On {task_name}')
        plt.savefig(f'{algo_name}_{task_name}_{key}_{tag.replace("/", "_")}.png',
                    bbox_inches='tight')
